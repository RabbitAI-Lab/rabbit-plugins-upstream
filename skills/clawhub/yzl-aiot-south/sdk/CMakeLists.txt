cmake_minimum_required(VERSION 3.10)
project(aiot_c_sdk C)

set(CMAKE_C_STANDARD 90)
set(CMAKE_C_STANDARD_REQUIRED ON)
set(CMAKE_C_EXTENSIONS OFF)

if(MSVC)
    add_compile_options(/W4)
else()
    add_compile_options(-Wall -Wextra)
endif()

add_library(aiot STATIC
    src/aiot.c
    src/aiot_json.c
)
target_include_directories(aiot PUBLIC include)

add_library(aiot_port STATIC port/aiot_port_posix.c)
target_include_directories(aiot_port PUBLIC port)
target_link_libraries(aiot_port PUBLIC aiot)
if(WIN32)
    target_link_libraries(aiot_port PUBLIC ws2_32)
endif()

add_library(aiot_mqtt STATIC port/aiot_mqtt_client.c)
target_link_libraries(aiot_mqtt PUBLIC aiot aiot_port)

add_executable(host_tcp_demo examples/host_tcp_demo.c)
target_link_libraries(host_tcp_demo PRIVATE aiot_port)

add_executable(host_udp_demo examples/host_udp_demo.c)
target_link_libraries(host_udp_demo PRIVATE aiot_port)

add_executable(host_mqtt_demo examples/host_mqtt_demo.c)
target_link_libraries(host_mqtt_demo PRIVATE aiot_mqtt)

enable_testing()
add_executable(test_all tests/test_all.c src/aiot.c src/aiot_json.c)
target_include_directories(test_all PRIVATE include src)
add_test(NAME test_all COMMAND test_all)
