template = """cmake_minimum_required(VERSION {cmake_version})
project({project_name} LANGUAGES CXX)

set(CMAKE_EXPORT_COMPILE_COMMANDS ON)
set(CMAKE_CXX_STANDARD {std})

if(CMAKE_BUILD_TYPE STREQUAL "Debug")
    message(STATUS "Sanitizer is enabled")
    set(CMAKE_CXX_FLAGS "${{CMAKE_CXX_FLAGS}} -Wall -pedantic -O0 -g -fsanitize=address")
    add_subdirectory(security)
else()
    set(CMAKE_CXX_FLAGS "${{CMAKE_CXX_FLAGS}} -Wall -pedantic -O3")
endif()

add_subdirectory(tests)
add_subdirectory(benchmarks)
add_subdirectory({project_name})
"""
