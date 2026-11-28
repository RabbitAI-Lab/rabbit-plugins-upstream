/*
 * app_aiot.c - Keil MDK / 裸机接入骨架
 *
 * 这个文件不依赖具体 MCU，只依赖你在 bsp_aiot.c 中实现的：
 *   int      bsp_tcp_send(const aiot_u8 *data, aiot_u32 len);
 *   aiot_u32 bsp_ms(void);
 *   void     bsp_tcp_close(void);
 *   int      bsp_tcp_connect(const char *host, aiot_u16 port);
 *
 * 把本文件和 dist/aiot_sdk.c 一起加入 Keil 工程即可。
 */

#include "aiot.h"

#include <string.h>

/* ------------------------- 需要在 BSP 中实现 ------------------------- */
extern int bsp_tcp_send(const aiot_u8 *data, aiot_u32 len);
extern aiot_u32 bsp_ms(void);
extern void bsp_tcp_close(void);
extern int bsp_tcp_connect(const char *host, aiot_u16 port);

/* ------------------------- 全局对象 ---------------------------------- */
static aiot_client_t g_aiot;
static aiot_u8 g_tx[2048];
static aiot_u8 g_rx[4096];
static volatile int g_reconnect;
static int g_started;

/* ------------------------- SDK 回调 ---------------------------------- */
static int sdk_send(void *user, const aiot_u8 *data, size_t len)
{
    (void)user;
    return bsp_tcp_send(data, (aiot_u32)len) == (int)len ? 0 : -1;
}

static aiot_u32 sdk_now(void *user)
{
    (void)user;
    return bsp_ms();
}

static void sdk_event(void *user, const aiot_event_t *ev)
{
    (void)user;

    switch (ev->type) {
    case AIOT_EV_CONNECTED:
        /* TCP 已建立，SDK 正在发 lgn */
        break;

    case AIOT_EV_LOGIN:
        if (ev->code == 0) {
            aiot_kv_t kv[] = {
                {"temp", "25.5"},
                {"hum",  "60"},
                {"ver",  "fw-1.0.0"},
            };
            (void)aiot_report(&g_aiot, kv, 3, NULL);
        } else {
            /* code=3 密码错误；置重连并按退避处理，不要死循环 */
            g_reconnect = 1;
        }
        break;

    case AIOT_EV_RESULT:
        /*
         * 平台回执。可按 ev->func / ev->fid 区分：
         *   get_time -> ev->result_text
         *   gfinfo/gfcet -> ev->result_json
         */
        break;

    case AIOT_EV_ORDER:
        /*
         * 默认 SDK 已自动回 order_conf。
         * 这里解析 args 并模拟执行；真实项目应操作 GPIO/PWM/继电器，
         * 再把实际值通过 aiot_order_reply() 回传。
         */
        if (strcmp(ev->cmd, "set") == 0) {
            char key[32];
            char value[32];
            if (aiot_args_get_str(ev->args_json, ev->args_len, 1,
                                  key, sizeof key) >= 0 &&
                aiot_args_get_str(ev->args_json, ev->args_len, 2,
                                  value, sizeof value) >= 0) {
                aiot_kv_t kv;
                kv.key = key;
                kv.value = value;
                (void)aiot_order_reply(&g_aiot, ev->tra, &kv, 1);
            }
        } else if (strcmp(ev->cmd, "get") == 0) {
            char key[32];
            if (aiot_args_get_str(ev->args_json, ev->args_len, 1,
                                  key, sizeof key) >= 0) {
                aiot_kv_t kv;
                kv.key = key;
                kv.value = "1"; /* 真实项目读取当前值 */
                (void)aiot_order_reply(&g_aiot, ev->tra, &kv, 1);
            }
        }
        break;

    case AIOT_EV_TIMEOUT:
    case AIOT_EV_ERROR:
        g_reconnect = 1;
        break;

    case AIOT_EV_DISCONNECTED:
        g_started = 0;
        break;

    default:
        break;
    }
}

/* ------------------------- 对外接口 ---------------------------------- */
void app_aiot_init(const char *device_id, const char *password)
{
    aiot_config_t cfg;
    memset(&cfg, 0, sizeof cfg);

    cfg.device_id     = device_id;
    cfg.password      = password;
    cfg.mode          = AIOT_MODE_TCP;
    cfg.send          = sdk_send;
    cfg.now_ms        = sdk_now;
    cfg.on_event      = sdk_event;
    cfg.keepalive_sec = 300;
    cfg.heartbeat_sec = 60;

    (void)aiot_init(&g_aiot, &cfg, g_tx, sizeof g_tx, g_rx, sizeof g_rx);
}

void app_aiot_on_connected(void)
{
    if (aiot_client_connected(&g_aiot) == 0) {
        g_started = 1;
        g_reconnect = 0;
    } else {
        g_reconnect = 1;
    }
}

void app_aiot_on_data(const aiot_u8 *data, aiot_u32 len)
{
    (void)aiot_client_rx(&g_aiot, data, (size_t)len);
}

void app_aiot_on_closed(void)
{
    (void)aiot_client_disconnected(&g_aiot);
    g_started = 0;
    g_reconnect = 1;
}

void app_aiot_loop(void)
{
    if (g_started) {
        (void)aiot_client_poll(&g_aiot, bsp_ms());
    }

    if (g_reconnect) {
        g_reconnect = 0;
        bsp_tcp_close();
        /* 建议在这里做 1s/2s/5s/10s 退避，不要立即重连 */
        (void)bsp_tcp_connect("ciot.yzlkj.com", 41032);
    }
}

/* 可选：主循环里每 10 秒上报一次 */
void app_aiot_report_demo(void)
{
    aiot_kv_t kv[] = {{"temp", "25.5"}, {"hum", "60"}};
    if (aiot_client_state(&g_aiot) == AIOT_STATE_ONLINE) {
        (void)aiot_report(&g_aiot, kv, 2, NULL);
    }
}
