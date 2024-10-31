_template_interface = """cmake_minimum_required(VERSION {cmake_version})
project({project_name}-lib LANGUAGES CXX)

add_library({project_name}-lib INTERFACE)
add_library({lib_name} ALIAS {project_name}-lib)

target_include_directories({project_name}-lib INTERFACE
    ${{CMAKE_CURRENT_SOURCE_DIR}}/include
)

target_include_directories({project_name}-lib PUBLIC
  $<INSTALL_INTERFACE:${{CMAKE_INSTALL_INCLUDEDIR}}>
  $<BUILD_INTERFACE:${{CMAKE_CURRENT_LIST_DIR}}/include>)"""


_template_static_or_shared = """cmake_minimum_required(VERSION {cmake_version})
project({project_name}-lib LANGUAGES CXX)

file(GLOB TARGET_SRC ${{CMAKE_CURRENT_SOURCE_DIR}}/src/*.cpp)

add_library({project_name}-lib {lib_type}
    ${{TARGET_SRC}}
)

add_library({lib_name} ALIAS {project_name}-lib)

target_include_directories({project_name}-lib PUBLIC
    ${{CMAKE_CURRENT_SOURCE_DIR}}/include
)
"""


class template:
    @staticmethod
    def format(**kwargs):
        if kwargs["lib_type"].lower() == "interface":
            return _template_interface.format(**kwargs)
        return _template_static_or_shared.format(**kwargs)
