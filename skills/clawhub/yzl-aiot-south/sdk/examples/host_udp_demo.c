/*
 * host_udp_demo.c - UDP 低功耗示例（Linux / Windows）
 *
 * 编译（MinGW）:
 *   gcc -std=c89 -Iinclude -Iport examples/host_udp_demo.c \
 *       src/aiot.c src/aiot_json.c port/aiot_port_posix.c \
 *       -lws2_32 -o host_udp_demo
 *
 * 运行:
 *   host_udp_demo ciot.yzlkj.com 40501 TD98-2011121433 <设备密码> 8
 */

#include "aiot.h"
#include "aiot_port.h"

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    aiot_client_t *cli;
    aiot_sock_t *sock;
} app_ctx_t;

static aiot_client_t g_cli;
static aiot_u8 g_tx[2048];
static aiot_u8 g_rx[4096];
static app_ctx_t g_ctx;
static int g_failed;
static int g_woken;
static int g_asked;

static int app_send(void *user, const aiot_u8 *data, size_t len)
{
    app_ctx_t *ctx = (app_ctx_t *)user;
    return aiot_udp_send(ctx->sock, data, len);
}

static aiot_u32 app_now(void *user)
{
    (void)user;
    return aiot_port_now_ms();
}

static void on_event(void *user, const aiot_event_t *ev)
{
    app_ctx_t *ctx = (app_ctx_t *)user;

    switch (ev->type) {
    case AIOT_EV_CONNECTED:
        printf("[udp] ready\n");
        break;
    case AIOT_EV_RESULT:
        printf("[udp] result func=%s code=%d ack=%s result=%s\n",
               ev->func, ev->code, ev->ack,
               ev->result_text[0] ? ev->result_text : "(json/null)");
        if (strcmp(ev->func, "lgn_facs") == 0 && ev->code == 0 && !g_woken) {
            g_woken = 1;
            printf("[udp] awake; pull order/time\n");
            (void)aiot_request_order(ctx->cli, "G1");
            (void)aiot_request_time(ctx->cli, "T1");
        }
        if (strcmp(ev->func, "get_order") == 0 && ev->code == 0) {
            g_asked = 1;
            printf("[udp] order payload=%.*s\n",
                   (int)ev->result_len, ev->result_json ? ev->result_json : "null");
        }
        if (ev->code != 0) {
            g_failed = 1;
        }
        break;
    case AIOT_EV_ERROR:
        printf("[udp] sdk error %d (%s)\n", ev->error, aiot_strerror(ev->error));
        g_failed = 1;
        break;
    default:
        break;
    }
}

int main(int argc, char **argv)
{
    aiot_config_t cfg;
    aiot_sock_t sock;
    aiot_kv_t kv[2];
    const char *host;
    const char *device;
    const char *password;
    unsigned long port;
    unsigned long duration;
    aiot_u32 start;
    int rc;

    if (argc < 5) {
        printf("usage: %s <host> <port> <device-id> <password> [seconds]\n", argv[0]);
        printf("  test: %s ciot.yzlkj.com 40501 TD98-2011121433 <password> 8\n", argv[0]);
        return 2;
    }
    host = argv[1];
    port = strtoul(argv[2], NULL, 10);
    device = argv[3];
    password = argv[4];
    duration = argc >= 6 ? strtoul(argv[5], NULL, 10) : 8;
    if (duration == 0) {
        duration = 8;
    }

    if (aiot_port_init() != 0) {
        printf("network init failed\n");
        return 1;
    }
    if (aiot_udp_open(&sock, host, (aiot_u16)port, 5000) != 0) {
        printf("open udp %s:%lu failed\n", host, port);
        aiot_port_cleanup();
        return 1;
    }

    g_ctx.cli = &g_cli;
    g_ctx.sock = &sock;

    memset(&cfg, 0, sizeof cfg);
    cfg.device_id = device;
    cfg.password = password;
    cfg.mode = AIOT_MODE_UDP;
    cfg.send = app_send;
    cfg.now_ms = app_now;
    cfg.on_event = on_event;
    cfg.user = &g_ctx;

    rc = aiot_init(&g_cli, &cfg, g_tx, sizeof g_tx, g_rx, sizeof g_rx);
    if (rc != 0) {
        printf("aiot_init failed: %s\n", aiot_strerror(rc));
        aiot_sock_close(&sock);
        aiot_port_cleanup();
        return 1;
    }

    (void)aiot_client_connected(&g_cli);

    kv[0].key = "wd";
    kv[0].value = "26.5";
    kv[1].key = "sf";
    kv[1].value = "61";
    rc = aiot_udp_wakeup(&g_cli, kv, 2, "W1");
    printf("[udp] lgn_facs -> %s\n", rc == 0 ? "sent" : aiot_strerror(rc));
    if (rc != 0) {
        g_failed = 1;
    }

    start = aiot_port_now_ms();
    while ((aiot_u32)(aiot_port_now_ms() - start) < duration * 1000u) {
        aiot_u8 buf[1024];
        int n = aiot_udp_recv(&sock, buf, sizeof buf, 500);
        if (n > 0) {
            (void)aiot_client_rx_datagram(&g_cli, buf, (size_t)n);
        } else if (n < 0) {
            printf("[udp] socket error\n");
            break;
        }
        if (g_failed) {
            break;
        }
    }

    (void)aiot_client_disconnected(&g_cli);
    aiot_sock_close(&sock);
    aiot_port_cleanup();
    printf("[udp] exit (failed=%d, woken=%d, order_reply=%d)\n",
           g_failed, g_woken, g_asked);
    return g_failed ? 1 : 0;
}
