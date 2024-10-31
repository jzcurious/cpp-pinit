cmake_minimum_required(VERSION 3.24...3.30)
project(myproj-tests LANGUAGES CXX)

include(GoogleTest)
include(FetchContent)

FetchContent_Declare(
  googletest
  GIT_REPOSITORY https://github.com/google/googletest.git
  GIT_TAG v1.15.2
)

FetchContent_MakeAvailable(googletest)

file(GLOB TESTS_SRC ${CMAKE_CURRENT_SOURCE_DIR}/src/*.cpp)

add_executable(myproj-tests
    ${TESTS_SRC}
)

target_include_directories(myproj-tests PRIVATE
    ${CMAKE_CURRENT_SOURCE_DIR}/include
    ${CMAKE_CURRENT_SOURCE_DIR}/../myproj/include
)

target_link_libraries(myproj-tests PRIVATE
    GTest::gtest_main
)

enable_testing()
gtest_discover_tests(myproj-tests)
