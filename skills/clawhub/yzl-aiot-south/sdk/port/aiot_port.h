/*
 * aiot_port.h - 可选的 POSIX / Windows socket 适配层（C89）
 *
 * 这层只服务于 PC 调试、网关程序和带 socket 的 RTOS。
 * 裸机 MCU 不需要它：直接实现 aiot_send_fn / aiot_now_fn 即可。
 */

#ifndef AIOT_PORT_H
#define AIOT_PORT_H

#include "aiot_types.h"

#include <stddef.h>

#ifdef __cplusplus
extern "C" {
#endif

typedef struct {
    void *fd;   /* 内部保存 SOCKET / int，避免在头文件引入平台 socket 类型 */
    int is_udp;
    int opened;
} aiot_sock_t;

/* Windows 下需要先调用；Linux/POSIX 下为空操作。 */
int aiot_port_init(void);
void aiot_port_cleanup(void);

/* 单调毫秒时钟（Windows: GetTickCount64，POSIX: CLOCK_MONOTONIC）。 */
aiot_u32 aiot_port_now_ms(void);

int aiot_tcp_open(aiot_sock_t *sock, const char *host, aiot_u16 port,
                  aiot_u32 timeout_ms);
int aiot_tcp_send(void *ctx, const aiot_u8 *data, size_t len);
/* 返回 >0 字节数，0 超时，<0 连接关闭/错误。 */
int aiot_tcp_recv(void *ctx, aiot_u8 *buf, size_t cap, aiot_u32 timeout_ms);

int aiot_udp_open(aiot_sock_t *sock, const char *host, aiot_u16 port,
                  aiot_u32 timeout_ms);
int aiot_udp_send(void *ctx, const aiot_u8 *data, size_t len);
int aiot_udp_recv(void *ctx, aiot_u8 *buf, size_t cap, aiot_u32 timeout_ms);

void aiot_sock_close(aiot_sock_t *sock);

#ifdef __cplusplus
}
#endif

#endif /* AIOT_PORT_H */
