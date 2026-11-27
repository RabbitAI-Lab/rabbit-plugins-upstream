CC      ?= cc
CFLAGS  ?= -std=c89 -pedantic -O2 -Wall -Wextra
CPPFLAGS += -Iinclude -Iport
LDLIBS  ?=

ifeq ($(OS),Windows_NT)
    LDLIBS += -lws2_32
    EXE := .exe
endif

CORE = src/aiot.c src/aiot_json.c
PORT = port/aiot_port_posix.c
MQTT = port/aiot_mqtt_client.c

.PHONY: all test clean demos

all: test host_tcp_demo host_udp_demo host_mqtt_demo

test: test_all$(EXE)
	./test_all$(EXE)

test_all$(EXE): tests/test_all.c $(CORE)
	$(CC) $(CFLAGS) $(CPPFLAGS) -Isrc $^ -o $@

host_tcp_demo$(EXE): examples/host_tcp_demo.c $(CORE) $(PORT)
	$(CC) $(CFLAGS) $(CPPFLAGS) $^ $(LDLIBS) -o $@

host_udp_demo$(EXE): examples/host_udp_demo.c $(CORE) $(PORT)
	$(CC) $(CFLAGS) $(CPPFLAGS) $^ $(LDLIBS) -o $@

host_mqtt_demo$(EXE): examples/host_mqtt_demo.c $(CORE) $(PORT) $(MQTT)
	$(CC) $(CFLAGS) $(CPPFLAGS) $^ $(LDLIBS) -o $@

clean:
	rm -f test_all test_all.exe host_tcp_demo host_tcp_demo.exe \
	      host_udp_demo host_udp_demo.exe host_mqtt_demo host_mqtt_demo.exe
