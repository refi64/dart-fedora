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

Source0: https://dart.googlesource.com/sdk.git/+archive/2.4.0.tar.gz#/sdk-2.4.0.tar.gz
Source1: https://chromium.googlesource.com/chromium/llvm-project/cfe/tools/clang-format.git/+archive/c09c8deeac31f05bd801995c475e7c8070f9ecda.tar.gz#/sdk_buildtools_clang_format_script-c09c8deeac31f05bd801995c475e7c8070f9ecda.tar.gz
Source2: https://gn.googlesource.com/gn/+archive/bdb0fd02324b120cacde634a9235405061c8ea06.tar.gz#/sdk_gn-bdb0fd02324b120cacde634a9235405061c8ea06.tar.gz
Source3: https://dart.googlesource.com/boringssl_gen.git/+archive/bbf52f18f425e29b1185f2f6753bec02ed8c5880.tar.gz#/sdk_third_party_boringssl-bbf52f18f425e29b1185f2f6753bec02ed8c5880.tar.gz
Source4: https://boringssl.googlesource.com/boringssl.git/+archive/702e2b6d3831486535e958f262a05c75a5cb312e.tar.gz#/sdk_third_party_boringssl_src-702e2b6d3831486535e958f262a05c75a5cb312e.tar.gz
Source5: https://dart.googlesource.com/observatory_pub_packages.git/+archive/0894122173b0f98eb08863a7712e78407d4477bc.tar.gz#/sdk_third_party_observatory_pub_packages-0894122173b0f98eb08863a7712e78407d4477bc.tar.gz
Source6: https://dart.googlesource.com/args.git/+archive/1.4.4.tar.gz#/sdk_third_party_pkg_args-1.4.4.tar.gz
Source7: https://dart.googlesource.com/async.git/+archive/2.0.8.tar.gz#/sdk_third_party_pkg_async-2.0.8.tar.gz
Source8: https://dart.googlesource.com/bazel_worker.git/+archive/bazel_worker-v0.1.20.tar.gz#/sdk_third_party_pkg_bazel_worker-bazel_worker-v0.1.20.tar.gz
Source9: https://dart.googlesource.com/boolean_selector.git/+archive/1.0.4.tar.gz#/sdk_third_party_pkg_boolean_selector-1.0.4.tar.gz
Source10: https://dart.googlesource.com/charcode.git/+archive/v1.1.2.tar.gz#/sdk_third_party_pkg_charcode-v1.1.2.tar.gz
Source11: https://dart.googlesource.com/cli_util.git/+archive/4ad7ccbe3195fd2583b30f86a86697ef61e80f41.tar.gz#/sdk_third_party_pkg_cli_util-4ad7ccbe3195fd2583b30f86a86697ef61e80f41.tar.gz
Source12: https://dart.googlesource.com/collection.git/+archive/1.14.11.tar.gz#/sdk_third_party_pkg_collection-1.14.11.tar.gz
Source13: https://dart.googlesource.com/convert.git/+archive/2.0.2.tar.gz#/sdk_third_party_pkg_convert-2.0.2.tar.gz
Source14: https://dart.googlesource.com/crypto.git/+archive/2.0.6.tar.gz#/sdk_third_party_pkg_crypto-2.0.6.tar.gz
Source15: https://dart.googlesource.com/csslib.git/+archive/0.15.0.tar.gz#/sdk_third_party_pkg_csslib-0.15.0.tar.gz
Source16: https://dart.googlesource.com/dart2js_info.git/+archive/0.6.0.tar.gz#/sdk_third_party_pkg_dart2js_info-0.6.0.tar.gz
Source17: https://dart.googlesource.com/dartdoc.git/+archive/v0.28.2.tar.gz#/sdk_third_party_pkg_dartdoc-v0.28.2.tar.gz
Source18: https://dart.googlesource.com/fixnum.git/+archive/0.10.9.tar.gz#/sdk_third_party_pkg_fixnum-0.10.9.tar.gz
Source19: https://dart.googlesource.com/glob.git/+archive/1.1.7.tar.gz#/sdk_third_party_pkg_glob-1.1.7.tar.gz
Source20: https://dart.googlesource.com/html.git/+archive/0.14.0+1.tar.gz#/sdk_third_party_pkg_html-0.14.0+1.tar.gz
Source21: https://dart.googlesource.com/http.git/+archive/0.12.0+2.tar.gz#/sdk_third_party_pkg_http-0.12.0+2.tar.gz
Source22: https://dart.googlesource.com/http_multi_server.git/+archive/2.0.5.tar.gz#/sdk_third_party_pkg_http_multi_server-2.0.5.tar.gz
Source23: https://dart.googlesource.com/http_parser.git/+archive/3.1.3.tar.gz#/sdk_third_party_pkg_http_parser-3.1.3.tar.gz
Source24: https://dart.googlesource.com/http_retry.git/+archive/0.1.1.tar.gz#/sdk_third_party_pkg_http_retry-0.1.1.tar.gz
Source25: https://dart.googlesource.com/http_throttle.git/+archive/1.0.2.tar.gz#/sdk_third_party_pkg_http_throttle-1.0.2.tar.gz
Source26: https://dart.googlesource.com/intl.git/+archive/0.15.7.tar.gz#/sdk_third_party_pkg_intl-0.15.7.tar.gz
Source27: https://dart.googlesource.com/json_rpc_2.git/+archive/2.0.9.tar.gz#/sdk_third_party_pkg_json_rpc_2-2.0.9.tar.gz
Source28: https://dart.googlesource.com/linter.git/+archive/0.1.91.tar.gz#/sdk_third_party_pkg_linter-0.1.91.tar.gz
Source29: https://dart.googlesource.com/logging.git/+archive/0.11.3+2.tar.gz#/sdk_third_party_pkg_logging-0.11.3+2.tar.gz
Source30: https://dart.googlesource.com/markdown.git/+archive/2.0.3.tar.gz#/sdk_third_party_pkg_markdown-2.0.3.tar.gz
Source31: https://dart.googlesource.com/matcher.git/+archive/0.12.3.tar.gz#/sdk_third_party_pkg_matcher-0.12.3.tar.gz
Source32: https://dart.googlesource.com/mime.git/+archive/0.9.6+2.tar.gz#/sdk_third_party_pkg_mime-0.9.6+2.tar.gz
Source33: https://dart.googlesource.com/mockito.git/+archive/d39ac507483b9891165e422ec98d9fb480037c8b.tar.gz#/sdk_third_party_pkg_mockito-d39ac507483b9891165e422ec98d9fb480037c8b.tar.gz
Source34: https://dart.googlesource.com/external/github.com/xxgreg/mustache/+archive/5e81b12215566dbe2473b2afd01a8a8aedd56ad9.tar.gz#/sdk_third_party_pkg_mustache-5e81b12215566dbe2473b2afd01a8a8aedd56ad9.tar.gz
Source35: https://dart.googlesource.com/oauth2.git/+archive/1.2.1.tar.gz#/sdk_third_party_pkg_oauth2-1.2.1.tar.gz
Source36: https://dart.googlesource.com/path.git/+archive/1.6.2.tar.gz#/sdk_third_party_pkg_path-1.6.2.tar.gz
Source37: https://dart.googlesource.com/pedantic.git/+archive/v1.5.0.tar.gz#/sdk_third_party_pkg_pedantic-v1.5.0.tar.gz
Source38: https://dart.googlesource.com/pool.git/+archive/1.3.6.tar.gz#/sdk_third_party_pkg_pool-1.3.6.tar.gz
Source39: https://dart.googlesource.com/protobuf.git/+archive/7d34c9e4e552a4f66acce32e4344ae27756a1949.tar.gz#/sdk_third_party_pkg_protobuf-7d34c9e4e552a4f66acce32e4344ae27756a1949.tar.gz
Source40: https://dart.googlesource.com/pub.git/+archive/ecd5b413271f2699f8cd9e23aa4eebb5030c964f.tar.gz#/sdk_third_party_pkg_pub-ecd5b413271f2699f8cd9e23aa4eebb5030c964f.tar.gz
Source41: https://dart.googlesource.com/pub_semver.git/+archive/1.4.2.tar.gz#/sdk_third_party_pkg_pub_semver-1.4.2.tar.gz
Source42: https://chromium.googlesource.com/external/github.com/google/quiver-dart.git/+archive/2.0.0+1.tar.gz#/sdk_third_party_pkg_quiver-2.0.0+1.tar.gz
Source43: https://dart.googlesource.com/resource.git/+archive/2.1.5.tar.gz#/sdk_third_party_pkg_resource-2.1.5.tar.gz
Source44: https://dart.googlesource.com/shelf.git/+archive/0.7.3+3.tar.gz#/sdk_third_party_pkg_shelf-0.7.3+3.tar.gz
Source45: https://dart.googlesource.com/shelf_packages_handler.git/+archive/1.0.4.tar.gz#/sdk_third_party_pkg_shelf_packages_handler-1.0.4.tar.gz
Source46: https://dart.googlesource.com/shelf_static.git/+archive/v0.2.8.tar.gz#/sdk_third_party_pkg_shelf_static-v0.2.8.tar.gz
Source47: https://dart.googlesource.com/shelf_web_socket.git/+archive/0.2.2+3.tar.gz#/sdk_third_party_pkg_shelf_web_socket-0.2.2+3.tar.gz
Source48: https://dart.googlesource.com/source_map_stack_trace.git/+archive/1.1.5.tar.gz#/sdk_third_party_pkg_source_map_stack_trace-1.1.5.tar.gz
Source49: https://dart.googlesource.com/source_maps.git/+archive/8af7cc1a1c3a193c1fba5993ce22a546a319c40e.tar.gz#/sdk_third_party_pkg_source_maps-8af7cc1a1c3a193c1fba5993ce22a546a319c40e.tar.gz
Source50: https://dart.googlesource.com/source_span.git/+archive/1.5.5.tar.gz#/sdk_third_party_pkg_source_span-1.5.5.tar.gz
Source51: https://dart.googlesource.com/stack_trace.git/+archive/1.9.3.tar.gz#/sdk_third_party_pkg_stack_trace-1.9.3.tar.gz
Source52: https://dart.googlesource.com/stream_channel.git/+archive/2.0.0.tar.gz#/sdk_third_party_pkg_stream_channel-2.0.0.tar.gz
Source53: https://dart.googlesource.com/string_scanner.git/+archive/1.0.3.tar.gz#/sdk_third_party_pkg_string_scanner-1.0.3.tar.gz
Source54: https://dart.googlesource.com/term_glyph.git/+archive/1.0.1.tar.gz#/sdk_third_party_pkg_term_glyph-1.0.1.tar.gz
Source55: https://dart.googlesource.com/test.git/+archive/test-v1.6.4.tar.gz#/sdk_third_party_pkg_test-test-v1.6.4.tar.gz
Source56: https://dart.googlesource.com/test_descriptor.git/+archive/1.1.1.tar.gz#/sdk_third_party_pkg_test_descriptor-1.1.1.tar.gz
Source57: https://dart.googlesource.com/test_process.git/+archive/1.0.3.tar.gz#/sdk_third_party_pkg_test_process-1.0.3.tar.gz
Source58: https://dart.googlesource.com/test_reflective_loader.git/+archive/0.1.8.tar.gz#/sdk_third_party_pkg_test_reflective_loader-0.1.8.tar.gz
Source59: https://dart.googlesource.com/typed_data.git/+archive/1.1.6.tar.gz#/sdk_third_party_pkg_typed_data-1.1.6.tar.gz
Source60: https://chromium.googlesource.com/external/github.com/dart-lang/test.git/+archive/2b8375bc98bb9dc81c539c91aaea6adce12e1072.tar.gz#/sdk_third_party_pkg_unittest-2b8375bc98bb9dc81c539c91aaea6adce12e1072.tar.gz
Source61: https://dart.googlesource.com/usage.git/+archive/3.4.0.tar.gz#/sdk_third_party_pkg_usage-3.4.0.tar.gz
Source62: https://dart.googlesource.com/watcher.git/+archive/0.9.7+12.tar.gz#/sdk_third_party_pkg_watcher-0.9.7+12.tar.gz
Source63: https://dart.googlesource.com/web-components.git/+archive/8f57dac273412a7172c8ade6f361b407e2e4ed02.tar.gz#/sdk_third_party_pkg_web_components-8f57dac273412a7172c8ade6f361b407e2e4ed02.tar.gz
Source64: https://dart.googlesource.com/web_socket_channel.git/+archive/1.0.9.tar.gz#/sdk_third_party_pkg_web_socket_channel-1.0.9.tar.gz
Source65: https://dart.googlesource.com/yaml.git/+archive/2.1.15.tar.gz#/sdk_third_party_pkg_yaml-2.1.15.tar.gz
Source66: https://dart.googlesource.com/dart_style.git/+archive/1.2.8.tar.gz#/sdk_third_party_pkg_tested_dart_style-1.2.8.tar.gz
Source67: https://dart.googlesource.com/http_io.git/+archive/57da05a66f5bf7df3dd7aebe7b7efe0dfc477baa.tar.gz#/sdk_third_party_pkg_tested_http_io-57da05a66f5bf7df3dd7aebe7b7efe0dfc477baa.tar.gz
Source68: https://dart.googlesource.com/package_config.git/+archive/1.0.5.tar.gz#/sdk_third_party_pkg_tested_package_config-1.0.5.tar.gz
Source69: https://dart.googlesource.com/package_resolver.git/+archive/1.0.10.tar.gz#/sdk_third_party_pkg_tested_package_resolver-1.0.10.tar.gz
Source70: https://dart.googlesource.com/root_certificates.git/+archive/16ef64be64c7dfdff2b9f4b910726e635ccc519e.tar.gz#/sdk_third_party_root_certificates-16ef64be64c7dfdff2b9f4b910726e635ccc519e.tar.gz
Source71: https://chromium.googlesource.com/chromium/src/tools/idl_parser.git/+archive/5fb1ebf49d235b5a70c9f49047e83b0654031eb7.tar.gz#/sdk_tools_idl_parser-5fb1ebf49d235b5a70c9f49047e83b0654031eb7.tar.gz
Source72: https://storage.googleapis.com/dart-archive/channels/stable/release/2.3.0/sdk/dartsdk-linux-x64-release.zip#/sdk_tools_sdks_dart-sdk-5fb1ebf49d235b5a70c9f49047e83b0654031eb7.tar.gz

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
%setup -q -T -c -n deps/sdk_tools_sdks_dart-sdk -a 72
%setup -q -T -c -n deps/sdk_tools_idl_parser -a 71
%setup -q -T -c -n deps/sdk_third_party_root_certificates -a 70
%setup -q -T -c -n deps/sdk_third_party_pkg_tested_package_resolver -a 69
%setup -q -T -c -n deps/sdk_third_party_pkg_tested_package_config -a 68
%setup -q -T -c -n deps/sdk_third_party_pkg_tested_http_io -a 67
%setup -q -T -c -n deps/sdk_third_party_pkg_tested_dart_style -a 66
%setup -q -T -c -n deps/sdk_third_party_pkg_yaml -a 65
%setup -q -T -c -n deps/sdk_third_party_pkg_web_socket_channel -a 64
%setup -q -T -c -n deps/sdk_third_party_pkg_web_components -a 63
%setup -q -T -c -n deps/sdk_third_party_pkg_watcher -a 62
%setup -q -T -c -n deps/sdk_third_party_pkg_usage -a 61
%setup -q -T -c -n deps/sdk_third_party_pkg_unittest -a 60
%setup -q -T -c -n deps/sdk_third_party_pkg_typed_data -a 59
%setup -q -T -c -n deps/sdk_third_party_pkg_test_reflective_loader -a 58
%setup -q -T -c -n deps/sdk_third_party_pkg_test_process -a 57
%setup -q -T -c -n deps/sdk_third_party_pkg_test_descriptor -a 56
%setup -q -T -c -n deps/sdk_third_party_pkg_test -a 55
%setup -q -T -c -n deps/sdk_third_party_pkg_term_glyph -a 54
%setup -q -T -c -n deps/sdk_third_party_pkg_string_scanner -a 53
%setup -q -T -c -n deps/sdk_third_party_pkg_stream_channel -a 52
%setup -q -T -c -n deps/sdk_third_party_pkg_stack_trace -a 51
%setup -q -T -c -n deps/sdk_third_party_pkg_source_span -a 50
%setup -q -T -c -n deps/sdk_third_party_pkg_source_maps -a 49
%setup -q -T -c -n deps/sdk_third_party_pkg_source_map_stack_trace -a 48
%setup -q -T -c -n deps/sdk_third_party_pkg_shelf_web_socket -a 47
%setup -q -T -c -n deps/sdk_third_party_pkg_shelf_static -a 46
%setup -q -T -c -n deps/sdk_third_party_pkg_shelf_packages_handler -a 45
%setup -q -T -c -n deps/sdk_third_party_pkg_shelf -a 44
%setup -q -T -c -n deps/sdk_third_party_pkg_resource -a 43
%setup -q -T -c -n deps/sdk_third_party_pkg_quiver -a 42
%setup -q -T -c -n deps/sdk_third_party_pkg_pub_semver -a 41
%setup -q -T -c -n deps/sdk_third_party_pkg_pub -a 40
%setup -q -T -c -n deps/sdk_third_party_pkg_protobuf -a 39
%setup -q -T -c -n deps/sdk_third_party_pkg_pool -a 38
%setup -q -T -c -n deps/sdk_third_party_pkg_pedantic -a 37
%setup -q -T -c -n deps/sdk_third_party_pkg_path -a 36
%setup -q -T -c -n deps/sdk_third_party_pkg_oauth2 -a 35
%setup -q -T -c -n deps/sdk_third_party_pkg_mustache -a 34
%setup -q -T -c -n deps/sdk_third_party_pkg_mockito -a 33
%setup -q -T -c -n deps/sdk_third_party_pkg_mime -a 32
%setup -q -T -c -n deps/sdk_third_party_pkg_matcher -a 31
%setup -q -T -c -n deps/sdk_third_party_pkg_markdown -a 30
%setup -q -T -c -n deps/sdk_third_party_pkg_logging -a 29
%setup -q -T -c -n deps/sdk_third_party_pkg_linter -a 28
%setup -q -T -c -n deps/sdk_third_party_pkg_json_rpc_2 -a 27
%setup -q -T -c -n deps/sdk_third_party_pkg_intl -a 26
%setup -q -T -c -n deps/sdk_third_party_pkg_http_throttle -a 25
%setup -q -T -c -n deps/sdk_third_party_pkg_http_retry -a 24
%setup -q -T -c -n deps/sdk_third_party_pkg_http_parser -a 23
%setup -q -T -c -n deps/sdk_third_party_pkg_http_multi_server -a 22
%setup -q -T -c -n deps/sdk_third_party_pkg_http -a 21
%setup -q -T -c -n deps/sdk_third_party_pkg_html -a 20
%setup -q -T -c -n deps/sdk_third_party_pkg_glob -a 19
%setup -q -T -c -n deps/sdk_third_party_pkg_fixnum -a 18
%setup -q -T -c -n deps/sdk_third_party_pkg_dartdoc -a 17
%setup -q -T -c -n deps/sdk_third_party_pkg_dart2js_info -a 16
%setup -q -T -c -n deps/sdk_third_party_pkg_csslib -a 15
%setup -q -T -c -n deps/sdk_third_party_pkg_crypto -a 14
%setup -q -T -c -n deps/sdk_third_party_pkg_convert -a 13
%setup -q -T -c -n deps/sdk_third_party_pkg_collection -a 12
%setup -q -T -c -n deps/sdk_third_party_pkg_cli_util -a 11
%setup -q -T -c -n deps/sdk_third_party_pkg_charcode -a 10
%setup -q -T -c -n deps/sdk_third_party_pkg_boolean_selector -a 9
%setup -q -T -c -n deps/sdk_third_party_pkg_bazel_worker -a 8
%setup -q -T -c -n deps/sdk_third_party_pkg_async -a 7
%setup -q -T -c -n deps/sdk_third_party_pkg_args -a 6
%setup -q -T -c -n deps/sdk_third_party_observatory_pub_packages -a 5
%setup -q -T -c -n deps/sdk_third_party_boringssl_src -a 4
%setup -q -T -c -n deps/sdk_third_party_boringssl -a 3
%setup -q -T -c -n deps/sdk_gn -a 2
%setup -q -T -c -n deps/sdk_buildtools_clang_format_script -a 1
%setup -q -c -n sdk
! test -d %{_builddir}/sdk/buildtools/clang_format/script
mkdir -p %{_builddir}/sdk/buildtools/clang_format
mv %{_builddir}/deps/sdk_buildtools_clang_format_script %{_builddir}/sdk/buildtools/clang_format/script
! test -d %{_builddir}/sdk/gn
mkdir -p %{_builddir}/sdk
mv %{_builddir}/deps/sdk_gn %{_builddir}/sdk/gn
! test -d %{_builddir}/sdk/third_party/boringssl
mkdir -p %{_builddir}/sdk/third_party
mv %{_builddir}/deps/sdk_third_party_boringssl %{_builddir}/sdk/third_party/boringssl
! test -d %{_builddir}/sdk/third_party/boringssl/src
mkdir -p %{_builddir}/sdk/third_party/boringssl
mv %{_builddir}/deps/sdk_third_party_boringssl_src %{_builddir}/sdk/third_party/boringssl/src
! test -d %{_builddir}/sdk/third_party/observatory_pub_packages
mkdir -p %{_builddir}/sdk/third_party
mv %{_builddir}/deps/sdk_third_party_observatory_pub_packages %{_builddir}/sdk/third_party/observatory_pub_packages
! test -d %{_builddir}/sdk/third_party/pkg/args
mkdir -p %{_builddir}/sdk/third_party/pkg
mv %{_builddir}/deps/sdk_third_party_pkg_args %{_builddir}/sdk/third_party/pkg/args
! test -d %{_builddir}/sdk/third_party/pkg/async
mkdir -p %{_builddir}/sdk/third_party/pkg
mv %{_builddir}/deps/sdk_third_party_pkg_async %{_builddir}/sdk/third_party/pkg/async
! test -d %{_builddir}/sdk/third_party/pkg/bazel_worker
mkdir -p %{_builddir}/sdk/third_party/pkg
mv %{_builddir}/deps/sdk_third_party_pkg_bazel_worker %{_builddir}/sdk/third_party/pkg/bazel_worker
! test -d %{_builddir}/sdk/third_party/pkg/boolean_selector
mkdir -p %{_builddir}/sdk/third_party/pkg
mv %{_builddir}/deps/sdk_third_party_pkg_boolean_selector %{_builddir}/sdk/third_party/pkg/boolean_selector
! test -d %{_builddir}/sdk/third_party/pkg/charcode
mkdir -p %{_builddir}/sdk/third_party/pkg
mv %{_builddir}/deps/sdk_third_party_pkg_charcode %{_builddir}/sdk/third_party/pkg/charcode
! test -d %{_builddir}/sdk/third_party/pkg/cli_util
mkdir -p %{_builddir}/sdk/third_party/pkg
mv %{_builddir}/deps/sdk_third_party_pkg_cli_util %{_builddir}/sdk/third_party/pkg/cli_util
! test -d %{_builddir}/sdk/third_party/pkg/collection
mkdir -p %{_builddir}/sdk/third_party/pkg
mv %{_builddir}/deps/sdk_third_party_pkg_collection %{_builddir}/sdk/third_party/pkg/collection
! test -d %{_builddir}/sdk/third_party/pkg/convert
mkdir -p %{_builddir}/sdk/third_party/pkg
mv %{_builddir}/deps/sdk_third_party_pkg_convert %{_builddir}/sdk/third_party/pkg/convert
! test -d %{_builddir}/sdk/third_party/pkg/crypto
mkdir -p %{_builddir}/sdk/third_party/pkg
mv %{_builddir}/deps/sdk_third_party_pkg_crypto %{_builddir}/sdk/third_party/pkg/crypto
! test -d %{_builddir}/sdk/third_party/pkg/csslib
mkdir -p %{_builddir}/sdk/third_party/pkg
mv %{_builddir}/deps/sdk_third_party_pkg_csslib %{_builddir}/sdk/third_party/pkg/csslib
! test -d %{_builddir}/sdk/third_party/pkg/dart2js_info
mkdir -p %{_builddir}/sdk/third_party/pkg
mv %{_builddir}/deps/sdk_third_party_pkg_dart2js_info %{_builddir}/sdk/third_party/pkg/dart2js_info
! test -d %{_builddir}/sdk/third_party/pkg/dartdoc
mkdir -p %{_builddir}/sdk/third_party/pkg
mv %{_builddir}/deps/sdk_third_party_pkg_dartdoc %{_builddir}/sdk/third_party/pkg/dartdoc
! test -d %{_builddir}/sdk/third_party/pkg/fixnum
mkdir -p %{_builddir}/sdk/third_party/pkg
mv %{_builddir}/deps/sdk_third_party_pkg_fixnum %{_builddir}/sdk/third_party/pkg/fixnum
! test -d %{_builddir}/sdk/third_party/pkg/glob
mkdir -p %{_builddir}/sdk/third_party/pkg
mv %{_builddir}/deps/sdk_third_party_pkg_glob %{_builddir}/sdk/third_party/pkg/glob
! test -d %{_builddir}/sdk/third_party/pkg/html
mkdir -p %{_builddir}/sdk/third_party/pkg
mv %{_builddir}/deps/sdk_third_party_pkg_html %{_builddir}/sdk/third_party/pkg/html
! test -d %{_builddir}/sdk/third_party/pkg/http
mkdir -p %{_builddir}/sdk/third_party/pkg
mv %{_builddir}/deps/sdk_third_party_pkg_http %{_builddir}/sdk/third_party/pkg/http
! test -d %{_builddir}/sdk/third_party/pkg/http_multi_server
mkdir -p %{_builddir}/sdk/third_party/pkg
mv %{_builddir}/deps/sdk_third_party_pkg_http_multi_server %{_builddir}/sdk/third_party/pkg/http_multi_server
! test -d %{_builddir}/sdk/third_party/pkg/http_parser
mkdir -p %{_builddir}/sdk/third_party/pkg
mv %{_builddir}/deps/sdk_third_party_pkg_http_parser %{_builddir}/sdk/third_party/pkg/http_parser
! test -d %{_builddir}/sdk/third_party/pkg/http_retry
mkdir -p %{_builddir}/sdk/third_party/pkg
mv %{_builddir}/deps/sdk_third_party_pkg_http_retry %{_builddir}/sdk/third_party/pkg/http_retry
! test -d %{_builddir}/sdk/third_party/pkg/http_throttle
mkdir -p %{_builddir}/sdk/third_party/pkg
mv %{_builddir}/deps/sdk_third_party_pkg_http_throttle %{_builddir}/sdk/third_party/pkg/http_throttle
! test -d %{_builddir}/sdk/third_party/pkg/intl
mkdir -p %{_builddir}/sdk/third_party/pkg
mv %{_builddir}/deps/sdk_third_party_pkg_intl %{_builddir}/sdk/third_party/pkg/intl
! test -d %{_builddir}/sdk/third_party/pkg/json_rpc_2
mkdir -p %{_builddir}/sdk/third_party/pkg
mv %{_builddir}/deps/sdk_third_party_pkg_json_rpc_2 %{_builddir}/sdk/third_party/pkg/json_rpc_2
! test -d %{_builddir}/sdk/third_party/pkg/linter
mkdir -p %{_builddir}/sdk/third_party/pkg
mv %{_builddir}/deps/sdk_third_party_pkg_linter %{_builddir}/sdk/third_party/pkg/linter
! test -d %{_builddir}/sdk/third_party/pkg/logging
mkdir -p %{_builddir}/sdk/third_party/pkg
mv %{_builddir}/deps/sdk_third_party_pkg_logging %{_builddir}/sdk/third_party/pkg/logging
! test -d %{_builddir}/sdk/third_party/pkg/markdown
mkdir -p %{_builddir}/sdk/third_party/pkg
mv %{_builddir}/deps/sdk_third_party_pkg_markdown %{_builddir}/sdk/third_party/pkg/markdown
! test -d %{_builddir}/sdk/third_party/pkg/matcher
mkdir -p %{_builddir}/sdk/third_party/pkg
mv %{_builddir}/deps/sdk_third_party_pkg_matcher %{_builddir}/sdk/third_party/pkg/matcher
! test -d %{_builddir}/sdk/third_party/pkg/mime
mkdir -p %{_builddir}/sdk/third_party/pkg
mv %{_builddir}/deps/sdk_third_party_pkg_mime %{_builddir}/sdk/third_party/pkg/mime
! test -d %{_builddir}/sdk/third_party/pkg/mockito
mkdir -p %{_builddir}/sdk/third_party/pkg
mv %{_builddir}/deps/sdk_third_party_pkg_mockito %{_builddir}/sdk/third_party/pkg/mockito
! test -d %{_builddir}/sdk/third_party/pkg/mustache
mkdir -p %{_builddir}/sdk/third_party/pkg
mv %{_builddir}/deps/sdk_third_party_pkg_mustache %{_builddir}/sdk/third_party/pkg/mustache
! test -d %{_builddir}/sdk/third_party/pkg/oauth2
mkdir -p %{_builddir}/sdk/third_party/pkg
mv %{_builddir}/deps/sdk_third_party_pkg_oauth2 %{_builddir}/sdk/third_party/pkg/oauth2
! test -d %{_builddir}/sdk/third_party/pkg/path
mkdir -p %{_builddir}/sdk/third_party/pkg
mv %{_builddir}/deps/sdk_third_party_pkg_path %{_builddir}/sdk/third_party/pkg/path
! test -d %{_builddir}/sdk/third_party/pkg/pedantic
mkdir -p %{_builddir}/sdk/third_party/pkg
mv %{_builddir}/deps/sdk_third_party_pkg_pedantic %{_builddir}/sdk/third_party/pkg/pedantic
! test -d %{_builddir}/sdk/third_party/pkg/pool
mkdir -p %{_builddir}/sdk/third_party/pkg
mv %{_builddir}/deps/sdk_third_party_pkg_pool %{_builddir}/sdk/third_party/pkg/pool
! test -d %{_builddir}/sdk/third_party/pkg/protobuf
mkdir -p %{_builddir}/sdk/third_party/pkg
mv %{_builddir}/deps/sdk_third_party_pkg_protobuf %{_builddir}/sdk/third_party/pkg/protobuf
! test -d %{_builddir}/sdk/third_party/pkg/pub
mkdir -p %{_builddir}/sdk/third_party/pkg
mv %{_builddir}/deps/sdk_third_party_pkg_pub %{_builddir}/sdk/third_party/pkg/pub
! test -d %{_builddir}/sdk/third_party/pkg/pub_semver
mkdir -p %{_builddir}/sdk/third_party/pkg
mv %{_builddir}/deps/sdk_third_party_pkg_pub_semver %{_builddir}/sdk/third_party/pkg/pub_semver
! test -d %{_builddir}/sdk/third_party/pkg/quiver
mkdir -p %{_builddir}/sdk/third_party/pkg
mv %{_builddir}/deps/sdk_third_party_pkg_quiver %{_builddir}/sdk/third_party/pkg/quiver
! test -d %{_builddir}/sdk/third_party/pkg/resource
mkdir -p %{_builddir}/sdk/third_party/pkg
mv %{_builddir}/deps/sdk_third_party_pkg_resource %{_builddir}/sdk/third_party/pkg/resource
! test -d %{_builddir}/sdk/third_party/pkg/shelf
mkdir -p %{_builddir}/sdk/third_party/pkg
mv %{_builddir}/deps/sdk_third_party_pkg_shelf %{_builddir}/sdk/third_party/pkg/shelf
! test -d %{_builddir}/sdk/third_party/pkg/shelf_packages_handler
mkdir -p %{_builddir}/sdk/third_party/pkg
mv %{_builddir}/deps/sdk_third_party_pkg_shelf_packages_handler %{_builddir}/sdk/third_party/pkg/shelf_packages_handler
! test -d %{_builddir}/sdk/third_party/pkg/shelf_static
mkdir -p %{_builddir}/sdk/third_party/pkg
mv %{_builddir}/deps/sdk_third_party_pkg_shelf_static %{_builddir}/sdk/third_party/pkg/shelf_static
! test -d %{_builddir}/sdk/third_party/pkg/shelf_web_socket
mkdir -p %{_builddir}/sdk/third_party/pkg
mv %{_builddir}/deps/sdk_third_party_pkg_shelf_web_socket %{_builddir}/sdk/third_party/pkg/shelf_web_socket
! test -d %{_builddir}/sdk/third_party/pkg/source_map_stack_trace
mkdir -p %{_builddir}/sdk/third_party/pkg
mv %{_builddir}/deps/sdk_third_party_pkg_source_map_stack_trace %{_builddir}/sdk/third_party/pkg/source_map_stack_trace
! test -d %{_builddir}/sdk/third_party/pkg/source_maps
mkdir -p %{_builddir}/sdk/third_party/pkg
mv %{_builddir}/deps/sdk_third_party_pkg_source_maps %{_builddir}/sdk/third_party/pkg/source_maps
! test -d %{_builddir}/sdk/third_party/pkg/source_span
mkdir -p %{_builddir}/sdk/third_party/pkg
mv %{_builddir}/deps/sdk_third_party_pkg_source_span %{_builddir}/sdk/third_party/pkg/source_span
! test -d %{_builddir}/sdk/third_party/pkg/stack_trace
mkdir -p %{_builddir}/sdk/third_party/pkg
mv %{_builddir}/deps/sdk_third_party_pkg_stack_trace %{_builddir}/sdk/third_party/pkg/stack_trace
! test -d %{_builddir}/sdk/third_party/pkg/stream_channel
mkdir -p %{_builddir}/sdk/third_party/pkg
mv %{_builddir}/deps/sdk_third_party_pkg_stream_channel %{_builddir}/sdk/third_party/pkg/stream_channel
! test -d %{_builddir}/sdk/third_party/pkg/string_scanner
mkdir -p %{_builddir}/sdk/third_party/pkg
mv %{_builddir}/deps/sdk_third_party_pkg_string_scanner %{_builddir}/sdk/third_party/pkg/string_scanner
! test -d %{_builddir}/sdk/third_party/pkg/term_glyph
mkdir -p %{_builddir}/sdk/third_party/pkg
mv %{_builddir}/deps/sdk_third_party_pkg_term_glyph %{_builddir}/sdk/third_party/pkg/term_glyph
! test -d %{_builddir}/sdk/third_party/pkg/test
mkdir -p %{_builddir}/sdk/third_party/pkg
mv %{_builddir}/deps/sdk_third_party_pkg_test %{_builddir}/sdk/third_party/pkg/test
! test -d %{_builddir}/sdk/third_party/pkg/test_descriptor
mkdir -p %{_builddir}/sdk/third_party/pkg
mv %{_builddir}/deps/sdk_third_party_pkg_test_descriptor %{_builddir}/sdk/third_party/pkg/test_descriptor
! test -d %{_builddir}/sdk/third_party/pkg/test_process
mkdir -p %{_builddir}/sdk/third_party/pkg
mv %{_builddir}/deps/sdk_third_party_pkg_test_process %{_builddir}/sdk/third_party/pkg/test_process
! test -d %{_builddir}/sdk/third_party/pkg/test_reflective_loader
mkdir -p %{_builddir}/sdk/third_party/pkg
mv %{_builddir}/deps/sdk_third_party_pkg_test_reflective_loader %{_builddir}/sdk/third_party/pkg/test_reflective_loader
! test -d %{_builddir}/sdk/third_party/pkg/typed_data
mkdir -p %{_builddir}/sdk/third_party/pkg
mv %{_builddir}/deps/sdk_third_party_pkg_typed_data %{_builddir}/sdk/third_party/pkg/typed_data
! test -d %{_builddir}/sdk/third_party/pkg/unittest
mkdir -p %{_builddir}/sdk/third_party/pkg
mv %{_builddir}/deps/sdk_third_party_pkg_unittest %{_builddir}/sdk/third_party/pkg/unittest
! test -d %{_builddir}/sdk/third_party/pkg/usage
mkdir -p %{_builddir}/sdk/third_party/pkg
mv %{_builddir}/deps/sdk_third_party_pkg_usage %{_builddir}/sdk/third_party/pkg/usage
! test -d %{_builddir}/sdk/third_party/pkg/watcher
mkdir -p %{_builddir}/sdk/third_party/pkg
mv %{_builddir}/deps/sdk_third_party_pkg_watcher %{_builddir}/sdk/third_party/pkg/watcher
! test -d %{_builddir}/sdk/third_party/pkg/web_components
mkdir -p %{_builddir}/sdk/third_party/pkg
mv %{_builddir}/deps/sdk_third_party_pkg_web_components %{_builddir}/sdk/third_party/pkg/web_components
! test -d %{_builddir}/sdk/third_party/pkg/web_socket_channel
mkdir -p %{_builddir}/sdk/third_party/pkg
mv %{_builddir}/deps/sdk_third_party_pkg_web_socket_channel %{_builddir}/sdk/third_party/pkg/web_socket_channel
! test -d %{_builddir}/sdk/third_party/pkg/yaml
mkdir -p %{_builddir}/sdk/third_party/pkg
mv %{_builddir}/deps/sdk_third_party_pkg_yaml %{_builddir}/sdk/third_party/pkg/yaml
! test -d %{_builddir}/sdk/third_party/pkg_tested/dart_style
mkdir -p %{_builddir}/sdk/third_party/pkg_tested
mv %{_builddir}/deps/sdk_third_party_pkg_tested_dart_style %{_builddir}/sdk/third_party/pkg_tested/dart_style
! test -d %{_builddir}/sdk/third_party/pkg_tested/http_io
mkdir -p %{_builddir}/sdk/third_party/pkg_tested
mv %{_builddir}/deps/sdk_third_party_pkg_tested_http_io %{_builddir}/sdk/third_party/pkg_tested/http_io
! test -d %{_builddir}/sdk/third_party/pkg_tested/package_config
mkdir -p %{_builddir}/sdk/third_party/pkg_tested
mv %{_builddir}/deps/sdk_third_party_pkg_tested_package_config %{_builddir}/sdk/third_party/pkg_tested/package_config
! test -d %{_builddir}/sdk/third_party/pkg_tested/package_resolver
mkdir -p %{_builddir}/sdk/third_party/pkg_tested
mv %{_builddir}/deps/sdk_third_party_pkg_tested_package_resolver %{_builddir}/sdk/third_party/pkg_tested/package_resolver
! test -d %{_builddir}/sdk/third_party/root_certificates
mkdir -p %{_builddir}/sdk/third_party
mv %{_builddir}/deps/sdk_third_party_root_certificates %{_builddir}/sdk/third_party/root_certificates
! test -d %{_builddir}/sdk/tools/idl_parser
mkdir -p %{_builddir}/sdk/tools
mv %{_builddir}/deps/sdk_tools_idl_parser %{_builddir}/sdk/tools/idl_parser
! test -d %{_builddir}/sdk/tools/sdks/dart-sdk
mkdir -p %{_builddir}/sdk/tools/sdks
mv %{_builddir}/deps/sdk_tools_sdks_dart-sdk/dart-sdk %{_builddir}/sdk/tools/sdks/dart-sdk

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

# Create symlinks to the binaries.
for exe in %{buildroot}%{dart_path}/bin/*; do
  test -f $exe || continue
  name=${exe##*/}
  ln -s %{dart_path}/bin/$name %{buildroot}%{_bindir}/$name
done

# Fix the permissions on the snapshot directories & children to be world-readable.
find %{buildroot}%{dart_path}/bin -mindepth 1 -type d -exec chmod +rx {} \;

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
