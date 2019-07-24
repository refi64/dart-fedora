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
