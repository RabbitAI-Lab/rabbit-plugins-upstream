/*
 * host_mqtt_demo.c - MQTT 示例（Linux / Windows）
 *
 * 编译（MinGW）:
 *   gcc -std=c89 -Iinclude -Iport examples/host_mqtt_demo.c \
 *       src/aiot.c src/aiot_json.c port/aiot_port_posix.c \
 *       port/aiot_mqtt_client.c -lws2_32 -o host_mqtt_demo
 *
 * 运行:
 *   host_mqtt_demo ciot.yzlkj.com 1883 AIOTMQ AIOTMQ-0001 <设备密码> 12
 */

#include "aiot.h"
#include "aiot_port.h"
#include "aiot_mqtt.h"

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    aiot_client_t *cli;
    aiot_mqtt_t *mqtt;
} app_ctx_t;

static aiot_client_t g_cli;
static aiot_mqtt_t g_mqtt;
static aiot_u8 g_tx[2048];
static aiot_u8 g_rx[4096];
static app_ctx_t g_ctx;
static int g_failed;
static int g_started;
static aiot_u32 g_last_report;

static int app_send(void *user, const aiot_u8 *data, size_t len)
{
    app_ctx_t *ctx = (app_ctx_t *)user;
    return aiot_mqtt_publish(ctx->mqtt, data, len);
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
    kv[0].value = "24.5";
    kv[1].key = "hum";
    kv[1].value = "55";
    kv[2].key = "sw";
    kv[2].value = "0";
    kv[3].key = "ver";
    kv[3].value = "aiot-c-sdk/1.0 mqtt";
    rc = aiot_report(cli, kv, 4, NULL);
    printf("[mqtt] report -> %s\n", rc == 0 ? "sent" : aiot_strerror(rc));
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
        printf("[mqtt] sdk ready\n");
        break;
    case AIOT_EV_LOGIN:
        printf("[mqtt] login code=%d\n", ev->code);
        break;
    case AIOT_EV_RESULT:
        printf("[mqtt] result func=%s code=%d fid=%s result=%s\n",
               ev->func, ev->code, ev->fid,
               ev->result_text[0] ? ev->result_text : "(json/null)");
        if (ev->code != 0) {
            g_failed = 1;
        }
        break;
    case AIOT_EV_ORDER: {
        aiot_kv_t reply;
        printf("[mqtt] ORDER cmd=%s tra=%s args=%.*s\n",
               ev->cmd, ev->tra, (int)ev->args_len, ev->args_json);
        reply.key = "sw";
        reply.value = "0";
        if (strcmp(ev->cmd, "set") == 0 || strcmp(ev->cmd, "get") == 0) {
            (void)aiot_order_reply(cli, ev->tra, &reply, 1);
        }
        break;
    }
    case AIOT_EV_ERROR:
        printf("[mqtt] sdk error %d (%s)\n", ev->error, aiot_strerror(ev->error));
        g_failed = 1;
        break;
    case AIOT_EV_TIMEOUT:
        printf("[mqtt] timeout\n");
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
    const char *host;
    const char *product;
    const char *device;
    const char *password;
    unsigned long port;
    unsigned long duration;
    aiot_u32 start;
    int rc;

    if (argc < 6) {
        printf("usage: %s <host> <port> <product> <device-id> <password> [seconds]\n", argv[0]);
        printf("  test: %s ciot.yzlkj.com 1883 AIOTMQ AIOTMQ-0001 <password> 12\n", argv[0]);
        return 2;
    }
    host = argv[1];
    port = strtoul(argv[2], NULL, 10);
    product = argv[3];
    device = argv[4];
    password = argv[5];
    duration = argc >= 7 ? strtoul(argv[6], NULL, 10) : 12;
    if (duration == 0) {
        duration = 12;
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
    g_ctx.mqtt = &g_mqtt;

    memset(&cfg, 0, sizeof cfg);
    cfg.device_id = device;
    cfg.product_id = product;
    cfg.password = password;
    cfg.mode = AIOT_MODE_MQTT;
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
    rc = aiot_mqtt_init(&g_mqtt, &sock, &g_cli);
    if (rc != 0) {
        printf("aiot_mqtt_init failed: %s\n", aiot_strerror(rc));
        aiot_sock_close(&sock);
        aiot_port_cleanup();
        return 1;
    }
    rc = aiot_mqtt_connect(&g_mqtt);
    if (rc != 0) {
        printf("mqtt connect failed: %s\n", aiot_strerror(rc));
        aiot_sock_close(&sock);
        aiot_port_cleanup();
        return 1;
    }

    printf("mqtt connecting %s:%lu as %s ...\n", host, port, device);
    start = aiot_port_now_ms();
    while ((aiot_u32)(aiot_port_now_ms() - start) < duration * 1000u) {
        rc = aiot_mqtt_poll(&g_mqtt);
        if (rc != 0) {
            printf("[mqtt] poll error %s (code=%d)\n",
                   aiot_strerror(rc), aiot_mqtt_last_error(&g_mqtt));
            break;
        }
        if (!g_started && aiot_mqtt_is_connected(&g_mqtt)) {
            g_started = 1;
            printf("[mqtt] connected, subscribe sent; start sdk\n");
            (void)aiot_client_connected(&g_cli);
            send_sample(&g_cli);
            (void)aiot_request_time(&g_cli, "T1");
            g_last_report = aiot_port_now_ms();
        }
        if (g_started) {
            (void)aiot_client_poll(&g_cli, aiot_port_now_ms());
            if ((aiot_u32)(aiot_port_now_ms() - g_last_report) >= 10000u) {
                send_sample(&g_cli);
                g_last_report = aiot_port_now_ms();
            }
        }
        if (g_failed) {
            break;
        }
    }

    if (g_started) {
        (void)aiot_client_disconnected(&g_cli);
    }
    aiot_mqtt_close(&g_mqtt);
    aiot_sock_close(&sock);
    aiot_port_cleanup();
    printf("[mqtt] exit (failed=%d, started=%d)\n", g_failed, g_started);
    return g_failed ? 1 : 0;
}
