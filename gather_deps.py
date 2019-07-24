#!/usr/bin/env python3

from pathlib import Path

import argparse
import fnmatch
import importlib
import json
import platform
import shutil
import subprocess
import sys


def load_module_from_path(module, path):
    spec = importlib.util.spec_from_file_location(module, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def get_host_arch():
    gclient_bin = shutil.which('gclient')
    assert gclient_bin is not None, 'Cannot find gclient'

    detect_host_arch = load_module_from_path('detect_host_arch',
                                             Path(gclient_bin).parent / 'detect_host_arch.py')
    return detect_host_arch.HostArch()


def load_deps(gclient_dir):
    deps_process = subprocess.run(['gclient', 'flatten'], cwd=gclient_dir,
                                  stdout=subprocess.PIPE, universal_newlines=True)
    if deps_process.returncode:
        sys.exit(deps_process.returncode)

    deps_scope = {}
    exec(deps_process.stdout, None, deps_scope)
    return deps_scope['deps']


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('gclient_dir', help='Path to a Dart SDK gclient root', type=Path)
    parser.add_argument('master_ref', help='The main Git ref to process deps for')
    args = parser.parse_args()

    if not (args.gclient_dir / '.gclient').exists():
        sys.exit('Invalid gclient directory.')

    deps = load_deps(args.gclient_dir)

    sources = []
    setup = []
    post_setup = []

    depot_arch = get_host_arch()

    SKIP = {
        # We're not using prebuilt Clang.
        f'sdk/buildtools/linux-{depot_arch}/clang',

        # Manually unbundled deps.
        'sdk/third_party/icu',
        'sdk/third_party/tcmalloc/gperftools',
        'sdk/third_party/zlib',

        # Only needed for tests or build steps we don't have to run.
        'sdk/third_party/babel',
        'sdk/third_party/d8',
        'sdk/third_party/gsutil',
        'sdk/third_party/jinja2',
        'sdk/third_party/markupsafe',
        'sdk/third_party/ply',
        'sdk/third_party/WebCore',
        'sdk/tests/co19_2/src',
    }

    THIRD_PARTY_WHITELIST = {
        'sdk/third_party/boringssl',
        'sdk/third_party/boringssl/src',
        'sdk/third_party/observatory_pub_packages',
        'sdk/third_party/root_certificates',
    }

    DEPOT_TO_DART_ARCH_MAP = {
        'x86': 'ia32',
        'x64': 'x64',
        'arm': 'armv7',
        'arm64': 'arm64',
    }

    dart_arch = DEPOT_TO_DART_ARCH_MAP[depot_arch]

    for name, dep in deps.items():
        condition = dep.get('condition')
        if name in SKIP or condition == 'checkout_win':
            continue

        if (name.startswith('sdk/third_party') and not name.startswith('sdk/third_party/pkg')
                and name not in THIRD_PARTY_WHITELIST):
            print(f'NOTE: third_party dep: {name}')

        if condition is not None:
            print(f'NOTE: unhandled condition: {name} {condition}')

        archive_url = None

        if name == 'sdk/buildtools':
            package = dep['packages'][0]
            assert package['package'].startswith('gn/'), dep
            gn_version = package['version']
            assert gn_version.startswith('git_revision:')

            name = 'sdk/gn'
            repo = 'https://gn.googlesource.com/gn'
            ref = gn_version[len('git_revision:'):]
        elif name == 'sdk/tools/sdks':
            package = dep['packages'][0]
            assert package['package'].startswith('dart/dart-sdk/'), dep
            prebuilt_sdk_version = package['version']
            assert prebuilt_sdk_version.startswith('version:')
            prebuilt_sdk_version = prebuilt_sdk_version[len('version:'):]

            name = 'sdk/tools/sdks/dart-sdk'
            archive_url = 'https://storage.googleapis.com/dart-archive/channels/stable/release' \
                          f'/{prebuilt_sdk_version}/sdk/dartsdk-linux-{dart_arch}-release.zip'
        elif 'dep_type' in dep:
            print(f'WARNING: skipping {name}: {dep}')
            continue
        else:
            if archive_url is None:
                dep_url = dep['url']
                if '@' in dep_url:
                    repo, ref = dep['url'].split('@')
                else:
                    assert name == 'sdk', (name, dep)
                    repo = dep_url
                    ref = args.master_ref

            archive_url = f'{repo}/+archive/{ref}.tar.gz'

        escaped_name = name.replace('/', '_')
        filename = f'{escaped_name}-{ref}.tar.gz'
        sources.append(f'Source{len(sources)}: {archive_url}#/{filename}')

        if name == 'sdk':
            target_dir = name
        else:
            target_dir = f'deps/{escaped_name}'

        if not setup:
            setup.append(f'%setup -q -c -n {target_dir}')
        else:
            setup.append(f'%setup -q -T -c -n {target_dir} -a {len(setup)}')

        if name != 'sdk':
            if name == 'sdk/tools/sdks/dart-sdk':
                escaped_name += '/dart-sdk'

            post_setup.append(f'! test -d %{{_builddir}}/{name}')
            post_setup.append(f'mkdir -p %{{_builddir}}/{Path(name).parent}')
            post_setup.append(f'mv %{{_builddir}}/deps/{escaped_name} %{{_builddir}}/{name}')

    # Flip the setup list so we end up in the sdk directory at the end.
    assert setup[0].endswith('sdk')
    setup.reverse()

    with open('sources.spec', 'w') as fp:
        print('\n'.join(sources), file=fp)

    with open('prep.spec', 'w') as fp:
        print('\n'.join(setup + post_setup), file=fp)


if __name__ == '__main__':
    main()
