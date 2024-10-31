template = """cmake_minimum_required(VERSION {cmake_version})
project({project_name}-tests LANGUAGES CXX)

include(GoogleTest)
include(FetchContent)

FetchContent_Declare(
  googletest
  GIT_REPOSITORY https://github.com/google/googletest.git
  GIT_TAG {test_version}
)

FetchContent_MakeAvailable(googletest)

file(GLOB TESTS_SRC ${{CMAKE_CURRENT_SOURCE_DIR}}/src/*.cpp)

add_executable({project_name}-tests
    ${{TESTS_SRC}}
)

target_include_directories({project_name}-tests PRIVATE
    ${{CMAKE_CURRENT_SOURCE_DIR}}/include
    ${{CMAKE_CURRENT_SOURCE_DIR}}/../{project_name}/include
)

target_link_libraries({project_name}-tests PRIVATE
    GTest::gtest_main
)

enable_testing()
gtest_discover_tests({project_name}-tests)
"""
