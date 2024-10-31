cmake_minimum_required(VERSION 3.24...3.30)
project(myproj-benchmarks LANGUAGES CXX)

include(GoogleTest)
include(FetchContent)

FetchContent_Declare(
  benchmark
  GIT_REPOSITORY https://github.com/google/benchmark.git
  GIT_TAG v1.9.0
)

FetchContent_MakeAvailable(benchmark)

file(GLOB BENCHMARK_SRC ${CMAKE_CURRENT_SOURCE_DIR}/src/*.cpp)

add_executable(myproj-benchmarks
    ${BENCHMARK_SRC}
)

target_include_directories(myproj-benchmarks PRIVATE
    ${CMAKE_CURRENT_SOURCE_DIR}/../myproj/include
    ${CMAKE_CURRENT_SOURCE_DIR}/include
)

target_link_libraries(myproj-benchmarks PRIVATE
    benchmark::benchmark
)
