%global dart_path %{_libdir}/dart

Name:    dart
Version: 2.4.0
Release: 1%{?dist}
Summary: The Dart Programming Language

License: BSD-3-Clause
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: git
BuildRequires: gperftools-devel
BuildRequires: libicu-devel
BuildRequires: ninja-build
BuildRequires: python2
BuildRequires: zlib-devel

Requires: %{name}-libs%{?_isa} = %{version}-%{release}

%include sources.spec

%description
Dart is a client-optimized language for fast apps on any platform.

This package includes the base Dart interpreter.

%package libs
Summary: Dart runtime libraries

%description libs
This package contains the runtime libraries for use by Dart.

%package devel
Summary: Headers for Dart native development

%description devel
This package contains the headers for Dart native development and embedding.

%package tools
Summary: Tools for Dart development
Requires: %{name}

%description tools
This package contains Pub and other tools for Dart language development.

%prep
%include prep.spec

sed -i 's/sys.stderr.write(str(inst))/raise/' tools/make_version.py

# Auto-detect the architecture.
sed -i "s/default='x64'/default=HOST_ARCH/" tools/gn.py

# Add unbundled helpers.
# Based on:
# https://chromium.googlesource.com/chromium/src/build/+/refs/heads/master/linux/unbundle
# See there for explanation of system_icu_defines.

mkdir -p third_party/{icu,tcmalloc,zlib}

cat > third_party/icu/BUILD.gn <<'EOF'
import("//build/config/linux/pkg_config.gni")

pkg_config("system_icu") {
  packages = [
    "icu-i18n",
    "icu-uc",
  ]
}

config("system_icu_defines") {
  defines = [
    "UCHAR_TYPE=uint16_t",
    "U_IMPORT=U_EXPORT",
  ]
}

source_set("icu") {
  public_configs = [ ":system_icu", ":system_icu_defines" ]
}
EOF

cat > third_party/tcmalloc/BUILD.gn <<'EOF'
import("//build/config/linux/pkg_config.gni")

pkg_config("system_tcmalloc") {
  packages = [
    "libtcmalloc",
  ]
}

source_set("tcmalloc") {
  public_configs = [ ":system_tcmalloc" ]
}
EOF

cat > third_party/zlib/BUILD.gn <<'EOF'
import("//build/config/linux/pkg_config.gni")

pkg_config("system_zlib") {
  packages = [
    "zlib",
  ]
}

source_set("zlib") {
  public_configs = [ ":system_zlib" ]
}
EOF

# Remove some dependencies on a Git revision.
sed -i '/git\/logs\/HEAD/d;/:write_revision_file/d;/:write_version_file/d' sdk/BUILD.gn

# Remove some flags we don't want:
# - Werror because upstream doesn't seem test with GCC so a ton of warnings will break the build.
# - Wno-unused-private-field because it's a Clang-only warning.
# - build-id=None because it breaks debuginfo package generation.
# - Anything that turns absolute source paths into relative because they also break debuginfo.
sed -i '/:relative_paths/d' build/config/BUILDCONFIG.gn
sed -i '/Werror/d;/build-id=none/d' build/config/compiler/BUILD.gn
sed -i '/Werror/d;/Wno-unused-private-field/d' runtime/BUILD.gn

# Fix the zlib include paths.
sed -i 's|"zlib/zlib.h"|<zlib.h>|g' runtime/bin/{gzip.cc,filter.h}

# Use a custom build config with our host cflags.
# NOTE: Upstream doesn't pass -fPIE/-fPIC flags to x86, but given encouraging of hardening flags
# and potential for dropping x86 support by Fedora anyway, we just ignore that here.
# XXX: What happens if one of these args has spaces? I don't think they can, so this is the
# easiest route. set_build_flags would also break if they had spaces / quotes AFAIK.

cat > build/config/linux/dump-fedora-toolchain-args.py <<'EOF'
import json
print(json.dumps(["%{build_cflags}".split(), "%{build_cxxflags}".split(),
                  "%{build_ldflags}".split()]))
EOF
cat > build/config/linux/BUILD.gn <<'EOF'
config("sdk") {
  flags = exec_script("//build/config/linux/dump-fedora-toolchain-args.py", [], "json")
  cflags_c = flags[0]
  cflags_cc = flags[1]
  ldflags = flags[2]
}

config("executable_config") {}
EOF

# Force the use of Python 2.
echo 'script_executable = "python2"' >> .gn
sed -i 's/python$suffix/python2/' utils/compiler/create_snapshot_entry.dart

%build
%set_build_flags
export CC=gcc
export CXX=g++

cd gn
# last_commit_position.h generation wants Git, so write it manually.
python2 build/gen.py --no-sysroot --no-last-commit-position
echo -e '#pragma once\n#define LAST_COMMIT_POSITION ""' > out/last_commit_position.h
# Don't statically link libstdc++.
sed -i 's/-static-libstdc++//g' out/build.ninja
ninja -C out gn
cd ..
mv gn/out/gn buildtools

export DART_GN_ARGS=
DART_GN_ARGS+=' dart_version_git_info=false'
DART_GN_ARGS+=' dart_use_debian_sysroot=false'
DART_GN_ARGS+=' dart_component_kind="shared_library"'
python2 tools/gn.py -m product --no-clang --no-goma
python2 tools/build.py -m product create_sdk

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}{%{_libdir},%{_bindir}}
cp -r out/ProductX64/dart-sdk %{buildroot}%{dart_path}
mv %{buildroot}%{dart_path}/include %{buildroot}%{_includedir}
install -Dm 755 out/ProductX64/libdart_jit.so %{buildroot}%{_libdir}
rm %{buildroot}%{dart_path}/{README,LICENSE}
rm %{buildroot}%{dart_path}/lib/api_readme.md

for exe in %{buildroot}%{dart_path}/bin/*; do
  test -f $exe || continue
  name=${exe##*/}
  ln -s %{_bindir}/$name %{buildroot}%{_bindir}/$name
done

%files
%license LICENSE
%{_bindir}/dart
%{dart_path}/bin/dart

%files devel
%license LICENSE
%{_includedir}/dart_api.h
%{_includedir}/dart_native_api.h
%{_includedir}/dart_tools_api.h

%files libs
%license LICENSE
%{_libdir}/libdart_jit.so

%files tools
%license LICENSE
%{_bindir}/dart2js
%{_bindir}/dartanalyzer
%{_bindir}/dartdevc
%{_bindir}/dartdoc
%{_bindir}/dartfmt
%{_bindir}/pub
%{dart_path}/bin/dart2js
%{dart_path}/bin/dartanalyzer
%{dart_path}/bin/dartdevc
%{dart_path}/bin/dartdoc
%{dart_path}/bin/dartfmt
%{dart_path}/bin/pub
%{dart_path}/bin/snapshots
%{dart_path}/lib
%{dart_path}/dartdoc_options.yaml
