_template = """cmake_minimum_required(VERSION {cmake_version})
project({project_name} LANGUAGES CXX)

set(CMAKE_EXPORT_COMPILE_COMMANDS ON)
set(CMAKE_CXX_STANDARD {std})

if(CMAKE_BUILD_TYPE STREQUAL "Debug")
    set(CMAKE_CXX_FLAGS "${{CMAKE_CXX_FLAGS}} {debug_flags}")
else()
    set(CMAKE_CXX_FLAGS "${{CMAKE_CXX_FLAGS}} {release_flags}")
endif()

add_subdirectory({project_name})
"""


class template:
    @staticmethod
    def format(**kwargs):
        tmpl = _template
        if kwargs["enable_tests"]:
            tmpl += "\nadd_subdirectory(tests)"
        if kwargs["enable_benchmarks"]:
            tmpl += "\nadd_subdirectory(benchmarks)"
        if kwargs["enable_security"]:
            tmpl += "\nadd_subdirectory(security)"
        return tmpl.format(**kwargs)
