cmake_minimum_required(VERSION 3.24...3.30)
project(myproj-security LANGUAGES CXX)

file(GLOB SECURITY_SRC ${CMAKE_CURRENT_SOURCE_DIR}/src/*.cpp)

add_executable(myproj-security
    ${SECURITY_SRC}
)

target_include_directories(myproj-security PRIVATE
    ${CMAKE_CURRENT_SOURCE_DIR}/../myproj/include
    ${CMAKE_CURRENT_SOURCE_DIR}/include
)

target_link_libraries(myproj-security PRIVATE
    myproj
)