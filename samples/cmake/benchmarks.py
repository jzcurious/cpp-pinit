template = """cmake_minimum_required(VERSION {cmake_version})
project({project_name}-benchmarks LANGUAGES CXX)

include(GoogleTest)
include(FetchContent)

FetchContent_Declare(
  benchmark
  GIT_REPOSITORY https://github.com/google/benchmark.git
  GIT_TAG {benchmark_version}
)

FetchContent_MakeAvailable(benchmark)

file(GLOB BENCHMARK_SRC ${{CMAKE_CURRENT_SOURCE_DIR}}/src/*.cpp)

add_executable({project_name}-benchmarks
    ${{BENCHMARK_SRC}}
)

target_include_directories({project_name}-benchmarks PRIVATE
    ${{CMAKE_CURRENT_SOURCE_DIR}}/../{project_name}/include
    ${{CMAKE_CURRENT_SOURCE_DIR}}/include
)

target_link_libraries({project_name}-benchmarks PRIVATE
    benchmark::benchmark
    {lib_name}
)
"""
