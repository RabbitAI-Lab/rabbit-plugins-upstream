/*
 * aiot_port_posix.c - POSIX / Windows socket 适配层实现
 *
 * 编译:
 *   Linux/macOS:  cc ... aiot_port_posix.c
 *   Windows MinGW: gcc ... aiot_port_posix.c -lws2_32
 *   MSVC:          cl ... aiot_port_posix.c ws2_32.lib
 */

#if !defined(_WIN32)
#ifndef _POSIX_C_SOURCE
#define _POSIX_C_SOURCE 200809L
#endif
#endif

#include "aiot_port.h"

#include <errno.h>
#include <limits.h>
#include <stdio.h>
#include <string.h>

#if defined(_WIN32)
#define WIN32_LEAN_AND_MEAN
#include <winsock2.h>
#include <ws2tcpip.h>
#include <windows.h>
typedef SOCKET aiot_os_sock_t;
typedef int aiot_socklen_t;
#define AIOT_BAD_SOCK INVALID_SOCKET
#define AIOT_SOCK_ERR() WSAGetLastError()
#define AIOT_EWOULDBLOCK(e) ((e) == WSAEWOULDBLOCK)
#define AIOT_EINPROGRESS(e) ((e) == WSAEWOULDBLOCK || (e) == WSAEINPROGRESS)
#define AIOT_EINTR(e) ((e) == WSAEINTR)
#else
#include <arpa/inet.h>
#include <fcntl.h>
#include <netdb.h>
#include <netinet/in.h>
#include <netinet/tcp.h>
#include <sys/select.h>
#include <sys/socket.h>
#include <sys/types.h>
#include <sys/time.h>
#include <unistd.h>
typedef int aiot_os_sock_t;
typedef socklen_t aiot_socklen_t;
#define AIOT_BAD_SOCK (-1)
#define AIOT_SOCK_ERR() errno
#define AIOT_EWOULDBLOCK(e) ((e) == EAGAIN || (e) == EWOULDBLOCK)
#define AIOT_EINPROGRESS(e) ((e) == EINPROGRESS)
#define AIOT_EINTR(e) ((e) == EINTR)
#endif

#if defined(_WIN32)
static int g_wsa_started = 0;
#endif

#ifndef MSG_NOSIGNAL
#define MSG_NOSIGNAL 0
#endif

int aiot_port_init(void)
{
#if defined(_WIN32)
    WSADATA wsa;
    if (g_wsa_started) {
        return 0;
    }
    if (WSAStartup(MAKEWORD(2, 2), &wsa) != 0) {
        return -1;
    }
    g_wsa_started = 1;
#endif
    return 0;
}

void aiot_port_cleanup(void)
{
#if defined(_WIN32)
    if (g_wsa_started) {
        WSACleanup();
        g_wsa_started = 0;
    }
#endif
}

aiot_u32 aiot_port_now_ms(void)
{
#if defined(_WIN32)
    return (aiot_u32)GetTickCount64();
#else
    struct timeval tv;
    if (gettimeofday(&tv, NULL) != 0) {
        return 0;
    }
    return (aiot_u32)((unsigned long)tv.tv_sec * 1000UL +
                      (unsigned long)tv.tv_usec / 1000UL);
#endif
}

static aiot_os_sock_t sock_of(const aiot_sock_t *s)
{
#if defined(_WIN32)
    return (aiot_os_sock_t)s->fd;
#else
    return (aiot_os_sock_t)(long)s->fd;
#endif
}

static void *sock_ptr(aiot_os_sock_t fd)
{
#if defined(_WIN32)
    return (void *)fd;
#else
    return (void *)(long)fd;
#endif
}

static int set_nonblock(aiot_os_sock_t fd)
{
#if defined(_WIN32)
    u_long mode = 1;
    return ioctlsocket(fd, FIONBIO, &mode) == 0 ? 0 : -1;
#else
    int flags = fcntl(fd, F_GETFL, 0);
    if (flags < 0) {
        return -1;
    }
    return fcntl(fd, F_SETFL, flags | O_NONBLOCK) == 0 ? 0 : -1;
#endif
}

static int wait_fd(aiot_os_sock_t fd, int for_write, aiot_u32 timeout_ms)
{
    fd_set set;
    struct timeval tv;
    int rc;

    FD_ZERO(&set);
    FD_SET(fd, &set);
    tv.tv_sec = (long)(timeout_ms / 1000u);
    tv.tv_usec = (long)((timeout_ms % 1000u) * 1000u);
#if defined(_WIN32)
    rc = select(0, for_write ? NULL : &set, for_write ? &set : NULL, NULL, &tv);
#else
    rc = select(fd + 1, for_write ? NULL : &set, for_write ? &set : NULL, NULL, &tv);
#endif
    if (rc < 0) {
        int e = AIOT_SOCK_ERR();
        if (AIOT_EINTR(e)) {
            return 0;
        }
        return -1;
    }
    return rc > 0 ? 1 : 0;
}

int aiot_tcp_open(aiot_sock_t *sock, const char *host, aiot_u16 port,
                  aiot_u32 timeout_ms)
{
    struct addrinfo hints;
    struct addrinfo *res = NULL;
    struct addrinfo *it;
    char portstr[8];
    int rc = -1;

    if (sock == NULL || host == NULL) {
        return -1;
    }
    memset(sock, 0, sizeof *sock);
    sock->fd = sock_ptr(AIOT_BAD_SOCK);
    (void)sprintf(portstr, "%u", (unsigned)port);

    memset(&hints, 0, sizeof hints);
    hints.ai_family = AF_UNSPEC;
    hints.ai_socktype = SOCK_STREAM;
    if (getaddrinfo(host, portstr, &hints, &res) != 0) {
        return -1;
    }

    for (it = res; it != NULL; it = it->ai_next) {
        aiot_os_sock_t fd = socket(it->ai_family, it->ai_socktype, it->ai_protocol);
        int yes = 1;
        if (fd == AIOT_BAD_SOCK) {
            continue;
        }
        (void)setsockopt(fd, IPPROTO_TCP, TCP_NODELAY, (const char *)&yes, sizeof yes);
        if (set_nonblock(fd) != 0) {
#if defined(_WIN32)
            closesocket(fd);
#else
            close(fd);
#endif
            continue;
        }
        if (connect(fd, it->ai_addr, (int)it->ai_addrlen) != 0) {
            int e = AIOT_SOCK_ERR();
            if (!AIOT_EINPROGRESS(e)) {
#if defined(_WIN32)
                closesocket(fd);
#else
                close(fd);
#endif
                continue;
            }
            if (wait_fd(fd, 1, timeout_ms) != 1) {
#if defined(_WIN32)
                closesocket(fd);
#else
                close(fd);
#endif
                continue;
            }
            {
                int err = 0;
                aiot_socklen_t elen = (aiot_socklen_t)sizeof err;
                if (getsockopt(fd, SOL_SOCKET, SO_ERROR, (char *)&err, &elen) != 0 || err != 0) {
#if defined(_WIN32)
                    closesocket(fd);
#else
                    close(fd);
#endif
                    continue;
                }
            }
        }
        sock->fd = sock_ptr(fd);
        sock->is_udp = 0;
        sock->opened = 1;
        rc = 0;
        break;
    }
    freeaddrinfo(res);
    return rc;
}

int aiot_udp_open(aiot_sock_t *sock, const char *host, aiot_u16 port,
                  aiot_u32 timeout_ms)
{
    struct addrinfo hints;
    struct addrinfo *res = NULL;
    struct addrinfo *it;
    char portstr[8];
    int rc = -1;

    (void)timeout_ms;
    if (sock == NULL || host == NULL) {
        return -1;
    }
    memset(sock, 0, sizeof *sock);
    sock->fd = sock_ptr(AIOT_BAD_SOCK);
    (void)sprintf(portstr, "%u", (unsigned)port);

    memset(&hints, 0, sizeof hints);
    hints.ai_family = AF_UNSPEC;
    hints.ai_socktype = SOCK_DGRAM;
    if (getaddrinfo(host, portstr, &hints, &res) != 0) {
        return -1;
    }

    for (it = res; it != NULL; it = it->ai_next) {
        aiot_os_sock_t fd = socket(it->ai_family, it->ai_socktype, it->ai_protocol);
        if (fd == AIOT_BAD_SOCK) {
            continue;
        }
        if (set_nonblock(fd) != 0) {
#if defined(_WIN32)
            closesocket(fd);
#else
            close(fd);
#endif
            continue;
        }
        if (connect(fd, it->ai_addr, (int)it->ai_addrlen) != 0) {
#if defined(_WIN32)
            closesocket(fd);
#else
            close(fd);
#endif
            continue;
        }
        sock->fd = sock_ptr(fd);
        sock->is_udp = 1;
        sock->opened = 1;
        rc = 0;
        break;
    }
    freeaddrinfo(res);
    return rc;
}

int aiot_tcp_send(void *ctx, const aiot_u8 *data, size_t len)
{
    aiot_sock_t *s = (aiot_sock_t *)ctx;
    aiot_os_sock_t fd;
    size_t sent = 0;

    if (s == NULL || !s->opened || (data == NULL && len > 0)) {
        return -1;
    }
    fd = sock_of(s);
    while (sent < len) {
        int chunk = (len - sent > 65536u) ? 65536 : (int)(len - sent);
        int n = send(fd, (const char *)data + sent, chunk, MSG_NOSIGNAL);
        if (n > 0) {
            sent += (size_t)n;
            continue;
        }
        {
            int e = AIOT_SOCK_ERR();
            if (AIOT_EINTR(e)) {
                continue;
            }
            if (AIOT_EWOULDBLOCK(e)) {
                if (wait_fd(fd, 1, 5000) == 1) {
                    continue;
                }
            }
        }
        return -1;
    }
    return 0;
}

int aiot_tcp_recv(void *ctx, aiot_u8 *buf, size_t cap, aiot_u32 timeout_ms)
{
    aiot_sock_t *s = (aiot_sock_t *)ctx;
    aiot_os_sock_t fd;
    int n;

    if (s == NULL || !s->opened || buf == NULL || cap == 0) {
        return -1;
    }
    if (wait_fd(sock_of(s), 0, timeout_ms) != 1) {
        return 0;
    }
    fd = sock_of(s);
    n = recv(fd, (char *)buf, (int)(cap > 65536u ? 65536u : cap), 0);
    if (n > 0) {
        return n;
    }
    if (n == 0) {
        return -1;
    }
    {
        int e = AIOT_SOCK_ERR();
        if (AIOT_EWOULDBLOCK(e) || AIOT_EINTR(e)) {
            return 0;
        }
    }
    return -1;
}

int aiot_udp_send(void *ctx, const aiot_u8 *data, size_t len)
{
    aiot_sock_t *s = (aiot_sock_t *)ctx;
    int n;

    if (s == NULL || !s->opened || s->is_udp == 0 ||
        (data == NULL && len > 0) || len > 65507u) {
        return -1;
    }
    n = send(sock_of(s), (const char *)data, (int)len, 0);
    return n == (int)len ? 0 : -1;
}

int aiot_udp_recv(void *ctx, aiot_u8 *buf, size_t cap, aiot_u32 timeout_ms)
{
    aiot_sock_t *s = (aiot_sock_t *)ctx;
    int n;

    if (s == NULL || !s->opened || s->is_udp == 0 || buf == NULL || cap == 0) {
        return -1;
    }
    if (wait_fd(sock_of(s), 0, timeout_ms) != 1) {
        return 0;
    }
    n = recv(sock_of(s), (char *)buf, (int)(cap > 65507u ? 65507u : cap), 0);
    if (n > 0) {
        return n;
    }
    if (n < 0) {
        int e = AIOT_SOCK_ERR();
        if (AIOT_EWOULDBLOCK(e) || AIOT_EINTR(e)) {
            return 0;
        }
    }
    return -1;
}

void aiot_sock_close(aiot_sock_t *sock)
{
    if (sock == NULL || !sock->opened) {
        return;
    }
#if defined(_WIN32)
    closesocket((SOCKET)sock->fd);
#else
    close((int)(long)sock->fd);
#endif
    sock->opened = 0;
    sock->fd = sock_ptr(AIOT_BAD_SOCK);
}
