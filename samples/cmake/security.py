template = """cmake_minimum_required(VERSION {cmake_version})
project({project_name}-security LANGUAGES CXX)

file(GLOB SECURITY_SRC ${{CMAKE_CURRENT_SOURCE_DIR}}/src/*.cpp)

add_executable({project_name}-security
    ${{SECURITY_SRC}}
)

target_include_directories({project_name}-security PRIVATE
    ${{CMAKE_CURRENT_SOURCE_DIR}}/../{project_name}/include
)
"""
