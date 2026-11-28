/*
 * host_tcp_demo.c - TCP 长连接示例（Linux / Windows）
 *
 * 编译（MinGW）:
 *   gcc -std=c89 -Iinclude -Iport examples/host_tcp_demo.c \
 *       src/aiot.c src/aiot_json.c port/aiot_port_posix.c \
 *       -lws2_32 -o host_tcp_demo
 *
 * 运行:
 *   host_tcp_demo ciot.yzlkj.com 41032 AIOTSDK-0001 <设备密码> 30
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
static int g_logged_in;
static aiot_u32 g_last_report;

static int app_send(void *user, const aiot_u8 *data, size_t len)
{
    app_ctx_t *ctx = (app_ctx_t *)user;
    return aiot_tcp_send(ctx->sock, data, len);
}

static aiot_u32 app_now(void *user)
{
    (void)user;
    return aiot_port_now_ms();
}

static void send_sample(aiot_client_t *cli)
{
    aiot_kv_t kv[4];
    int rc;

    kv[0].key = "temp";
    kv[0].value = "25.5";
    kv[1].key = "hum";
    kv[1].value = "60";
    kv[2].key = "sw";
    kv[2].value = "1";
    kv[3].key = "ver";
    kv[3].value = "aiot-c-sdk/1.0 \"demo\"";

    rc = aiot_report(cli, kv, 4, NULL);
    printf("[demo] report -> %s\n", rc == 0 ? "sent" : aiot_strerror(rc));
    if (rc != 0) {
        g_failed = 1;
    }
}

static void on_event(void *user, const aiot_event_t *ev)
{
    app_ctx_t *ctx = (app_ctx_t *)user;
    aiot_client_t *cli = ctx->cli;

    switch (ev->type) {
    case AIOT_EV_CONNECTED:
        printf("[demo] connected, waiting for login...\n");
        break;
    case AIOT_EV_LOGIN:
        printf("[demo] login func=%s code=%d result=%s\n",
               ev->func, ev->code, ev->result_text);
        if (ev->code == 0) {
            g_logged_in = 1;
            send_sample(cli);
            (void)aiot_request_time(cli, "T1");
            g_last_report = aiot_port_now_ms();
        } else {
            g_failed = 1;
        }
        break;
    case AIOT_EV_RESULT:
        printf("[demo] result func=%s code=%d fid=%s result=%s\n",
               ev->func, ev->code, ev->fid,
               ev->result_text[0] ? ev->result_text : "(json)");
        if (ev->code != 0) {
            printf("[demo] platform error code=%d\n", ev->code);
        }
        break;
    case AIOT_EV_ORDER: {
        aiot_kv_t reply;
        int rc;

        printf("[demo] ORDER cmd=%s tra=%s args=%.*s\n",
               ev->cmd, ev->tra, (int)ev->args_len, ev->args_json);

        /*
         * 示例设备只有 sw 一个可写测点。真实项目应解析 args，
         * 执行对应动作，再把实际值回传。
         */
        if (strcmp(ev->cmd, "get") == 0 || strcmp(ev->cmd, "set") == 0) {
            reply.key = "sw";
            reply.value = "1";
            rc = aiot_order_reply(cli, ev->tra, &reply, 1);
            printf("[demo] order_reply -> %s\n", rc == 0 ? "sent" : aiot_strerror(rc));
        }
        break;
    }
    case AIOT_EV_TIMEOUT:
        printf("[demo] timeout / link lost\n");
        g_failed = 1;
        break;
    case AIOT_EV_ERROR:
        printf("[demo] sdk error %d (%s)\n", ev->error, aiot_strerror(ev->error));
        g_failed = 1;
        break;
    case AIOT_EV_DISCONNECTED:
        printf("[demo] disconnected\n");
        break;
    default:
        break;
    }
}

int main(int argc, char **argv)
{
    aiot_config_t cfg;
    aiot_sock_t sock;
    const char *host;
    const char *device;
    const char *password;
    unsigned long port;
    unsigned long duration;
    aiot_u32 start;
    int rc;

    if (argc < 5) {
        printf("usage: %s <host> <port> <device-id> <password> [seconds]\n", argv[0]);
        printf("  test: %s ciot.yzlkj.com 41032 AIOTSDK-0001 <password> 30\n", argv[0]);
        return 2;
    }
    host = argv[1];
    port = strtoul(argv[2], NULL, 10);
    device = argv[3];
    password = argv[4];
    duration = argc >= 6 ? strtoul(argv[5], NULL, 10) : 30;
    if (duration == 0) {
        duration = 30;
    }

    if (aiot_port_init() != 0) {
        printf("network init failed\n");
        return 1;
    }
    if (aiot_tcp_open(&sock, host, (aiot_u16)port, 5000) != 0) {
        printf("connect %s:%lu failed\n", host, port);
        aiot_port_cleanup();
        return 1;
    }

    g_ctx.cli = &g_cli;
    g_ctx.sock = &sock;

    memset(&cfg, 0, sizeof cfg);
    cfg.device_id = device;
    cfg.password = password;
    cfg.mode = AIOT_MODE_TCP;
    cfg.send = app_send;
    cfg.now_ms = app_now;
    cfg.on_event = on_event;
    cfg.user = &g_ctx;
    cfg.keepalive_sec = 300;
    cfg.heartbeat_sec = 60;

    rc = aiot_init(&g_cli, &cfg, g_tx, sizeof g_tx, g_rx, sizeof g_rx);
    if (rc != 0) {
        printf("aiot_init failed: %s\n", aiot_strerror(rc));
        aiot_sock_close(&sock);
        aiot_port_cleanup();
        return 1;
    }

    printf("connecting %s:%lu as %s ...\n", host, port, device);
    start = aiot_port_now_ms();
    rc = aiot_client_connected(&g_cli);
    if (rc != 0) {
        printf("connected callback failed: %s\n", aiot_strerror(rc));
        aiot_sock_close(&sock);
        aiot_port_cleanup();
        return 1;
    }

    while ((aiot_u32)(aiot_port_now_ms() - start) < duration * 1000u) {
        aiot_u8 buf[1024];
        int n;
        aiot_u32 now = aiot_port_now_ms();

        (void)aiot_client_poll(&g_cli, now);
        n = aiot_tcp_recv(&sock, buf, sizeof buf, 100);
        if (n > 0) {
            (void)aiot_client_rx(&g_cli, buf, (size_t)n);
        } else if (n < 0) {
            printf("[demo] socket closed\n");
            break;
        }
        /* 回调里可能刚发过数据，重新取时间，避免无符号回绕误判 */
        now = aiot_port_now_ms();
        if (g_logged_in && (aiot_u32)(now - g_last_report) >= 10000u) {
            send_sample(&g_cli);
            g_last_report = now;
        }
        if (g_failed) {
            break;
        }
    }

    (void)aiot_client_disconnected(&g_cli);
    aiot_sock_close(&sock);
    aiot_port_cleanup();
    printf("[demo] exit (failed=%d)\n", g_failed);
    return g_failed ? 1 : 0;
}
