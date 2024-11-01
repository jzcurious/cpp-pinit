cmake_minimum_required(VERSION 3.24...3.30)
project(myproj-lib LANGUAGES CXX)

file(GLOB TARGET_SRC ${CMAKE_CURRENT_SOURCE_DIR}/src/*.cpp)

add_library(myproj-lib STATIC
    ${TARGET_SRC}
)

add_library(myproj ALIAS myproj-lib)

target_include_directories(myproj-lib PUBLIC
    ${CMAKE_CURRENT_SOURCE_DIR}/include
)
