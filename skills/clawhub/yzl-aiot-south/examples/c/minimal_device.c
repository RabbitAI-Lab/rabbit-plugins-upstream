/*
 * 南向示例（C）：最小设备骨架 —— lgn 登录、实时上报、下行指令回执。
 *
 * 说明：
 *   - 这是“接线骨架”，不是可直接量产的固件；my_send / my_now_ms 需要按你的
 *     网络层（4G/WiFi AT 模组、lwIP、W5500、POSIX socket）补全。
 *   - PC 上联调可直接用 SDK 自带的 port/aiot_port_posix.c（见 aiot-c-sdk/README.md）。
 *   - 编译：把 dist/aiot_sdk.c + include/ 加进工程；本文件仅作参考。
 */
#include <stdio.h>
#include <string.h>

#include "aiot.h"

static aiot_client_t g_cli;
static aiot_u8 g_tx[2048];
static aiot_u8 g_rx[4096];

/* 把一帧数据发到网络。TCP 模式带 '\n'；UDP 是一个完整数据报；MQTT 是 payload。 */
static int my_send(void *user, const aiot_u8 *data, size_t len)
{
    (void)user;
    /* TODO: 你的 socket / AT 模组发送实现 */
    (void)data;
    (void)len;
    return 0;
}

/* 单调递增毫秒时钟（允许 32 位回绕）。 */
static aiot_u32 my_now_ms(void *user)
{
    (void)user;
    /* TODO: HAL_GetTick() / xTaskGetTickCount() / clock_gettime() */
    return 0;
}

static void on_event(void *user, const aiot_event_t *ev)
{
    (void)user;
    switch (ev->type) {
    case AIOT_EV_LOGIN:
        if (ev->code == 0) {
            printf("[demo] ONLINE\n");
        } else {
            printf("[demo] login failed code=%d\n", ev->code);
        }
        break;

    case AIOT_EV_ORDER:
        /* set / get / upfs：SDK 默认已自动回 order_conf，这里只需执行并回结果 */
        printf("[demo] ORDER cmd=%s tra=%s args=%s\n",
               ev->cmd, ev->tra, ev->args_json ? ev->args_json : "");
        {
            aiot_kv_t kv = {"sw", "1"}; /* 执行结果 + 实际值 */
            aiot_order_reply(&g_cli, ev->tra, &kv, 1);
        }
        break;

    case AIOT_EV_ERROR:
        printf("[demo] error %d (%s)\n", ev->error, aiot_strerror(ev->error));
        break;

    default:
        break;
    }
}

int main(void)
{
    aiot_config_t cfg;
    aiot_kv_t report_kv = {"wd", "25.3"};

    memset(&cfg, 0, sizeof(cfg));
    cfg.device_id = "WANCD1-0000000007"; /* 改成你的设备 ID */
    cfg.product_id = NULL;               /* MQTT 模式必填 */
    cfg.password = "PASSWORD";           /* 设备详情页“认证密钥” */
    cfg.mode = AIOT_MODE_TCP;            /* AIOT_MODE_TCP / UDP / MQTT */
    cfg.send = my_send;
    cfg.now_ms = my_now_ms;
    cfg.on_event = on_event;
    cfg.keepalive_sec = 300;
    cfg.heartbeat_sec = 60;              /* 必须 < keepalive_sec */

    if (aiot_init(&g_cli, &cfg, g_tx, sizeof(g_tx), g_rx, sizeof(g_rx)) != AIOT_OK) {
        printf("aiot_init failed\n");
        return 1;
    }

    /* 网络连接成功后调用；SDK 会自动发 lgn */
    aiot_client_connected(&g_cli);

    for (;;) {
        /* 收到任意字节就喂给 SDK（TCP 按 '\n' 拆帧由 SDK 处理） */
        /* aiot_client_rx(&g_cli, buf, n);            TCP  */
        /* aiot_client_rx_datagram(&g_cli, buf, n);   UDP  */
        /* aiot_mqtt_rx(&g_cli, payload, n);          MQTT */

        aiot_client_poll(&g_cli, my_now_ms(NULL));

        if (aiot_client_state(&g_cli) == AIOT_STATE_ONLINE) {
            /* 每 60s 上报一次，别按秒级压 */
            aiot_report(&g_cli, &report_kv, 1, NULL);
        }

        /* TODO: 10–100ms 的延时/调度 */
        break; /* 示例：只跑一轮；真实固件应持续循环 */
    }

    aiot_client_disconnected(&g_cli);
    return 0;
}
