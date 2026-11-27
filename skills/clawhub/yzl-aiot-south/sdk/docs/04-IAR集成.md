# 04 · IAR EWARM 集成

适用于 IAR Embedded Workbench for ARM 8.x/9.x。SDK 是纯 C89，不依赖 IAR 特有扩展。

---

## 1. 添加文件

1. 在 IAR 工程窗口右键 `Add` → `Add Files...`；
2. 加入 `dist/aiot_sdk.c`；
3. `Project` → `Options` → `C/C++ Compiler` → `Preprocessor`；
4. 在 `Additional include directories` 加入 `dist`（或 `include`）；
5. `C/C++ Compiler` → `Language` → 选择 `C89`/`C90`（IAR 支持）。

只需要 `aiot_sdk.c` + `aiot.h` + `aiot_types.h`。不要加 `port/aiot_port_posix.c`（PC socket 用）。

---

## 2. 两个回调

```c
#include "aiot.h"

static aiot_client_t g_aiot;
static aiot_u8 g_tx[2048];
static aiot_u8 g_rx[4096];

static int aiot_send(void *user, const aiot_u8 *data, size_t len)
{
    (void)user;
    return bsp_tcp_send(data, (aiot_u32)len) == (int)len ? 0 : -1;
}

static aiot_u32 aiot_now(void *user)
{
    (void)user;
    return bsp_ms();   /* 1 ms 单调时钟 */
}
```

`bsp_tcp_send` 可以是：

- lwIP `netconn_write` / `tcp_write`
- W5500 的 `send()`
- ESP8266/4G 模组的 AT 发送
- RT-Thread `send()` / FreeRTOS+TCP

---

## 3. 初始化和事件

```c
static void aiot_event(void *user, const aiot_event_t *ev)
{
    (void)user;
    switch (ev->type) {
    case AIOT_EV_LOGIN:
        if (ev->code == 0) {
            aiot_kv_t kv[] = {{"temp", "25.5"}, {"hum", "60"}};
            aiot_report(&g_aiot, kv, 2, NULL);
        }
        break;
    case AIOT_EV_ORDER: {
        aiot_kv_t kv = {"sw", "1"};
        aiot_order_reply(&g_aiot, ev->tra, &kv, 1);
        break;
    }
    case AIOT_EV_TIMEOUT:
    case AIOT_EV_ERROR:
        g_reconnect = 1;
        break;
    default:
        break;
    }
}

void app_aiot_init(void)
{
    aiot_config_t cfg;
    memset(&cfg, 0, sizeof cfg);
    cfg.device_id = "WANCD2-0000001008";
    cfg.password  = "设备密码";
    cfg.mode      = AIOT_MODE_TCP;
    cfg.send      = aiot_send;
    cfg.now_ms    = aiot_now;
    cfg.on_event  = aiot_event;
    aiot_init(&g_aiot, &cfg, g_tx, sizeof g_tx, g_rx, sizeof g_rx);
}
```

IAR 工程里如果开启了 `--aeabi` / `--no_lib`，确认 `memcpy`/`memmove`/`memset`/`strlen`/`strcmp` 可用；SDK 只用这几个 C 库函数。

---

## 4. FreeRTOS / RT-Thread 方式

### 4.1 单任务轮询（推荐）

```c
void aiot_task(void *arg)
{
    (void)arg;
    app_aiot_init();
    for (;;) {
        if (g_connected) {
            aiot_client_poll(&g_aiot, bsp_ms());
        }
        vTaskDelay(pdMS_TO_TICKS(20));
    }
}
```

网络接收在 socket 回调/独立任务里：

```c
void on_tcp_data(const aiot_u8 *data, size_t len)
{
    aiot_client_rx(&g_aiot, data, len);
}
```

> SDK 不是线程安全的。`aiot_client_rx()`、`aiot_client_poll()`、`aiot_report()` 建议都在同一个任务上下文调用；如果必须跨任务，请用互斥锁包住。

### 4.2 lwIP raw API

在 `tcp_recv` 回调里：

```c
static err_t on_recv(void *arg, struct tcp_pcb *pcb, struct pbuf *p, err_t err)
{
    if (p != NULL) {
        aiot_client_rx(&g_aiot, (const aiot_u8 *)p->payload, p->len);
        tcp_recved(pcb, p->tot_len);
        pbuf_free(p);
    }
    return ERR_OK;
}
```

注意 pbuf 可能链式；如果 `p->len != p->tot_len`，需要遍历 `p->next` 逐段喂给 SDK。

### 4.3 ESP8266 AT

同 Keil 文档：`AT+CIPSTART` → `aiot_client_connected()`；`+IPD,<len>:` → `aiot_client_rx()`；`CLOSED` → `aiot_client_disconnected()`。

---

## 5. 优化

| 目标 | 做法 |
|---|---|
| 减小栈 | 编译器宏 `AIOT_JSON_MAX_TOKENS=64` |
| 减小 Flash | 不编译 MQTT 客户端；只保留 `aiot.c` + `aiot_json.c` |
| 减小 RX | OTA 场景保留 4096；纯上报 1024–2048 |
| 降低功耗 | 拉长 `heartbeat_sec`，但必须小于平台型号 `keepalive_sec` |
| 避免阻塞 | `on_event` 中只做置标志/短操作，复杂业务交给主循环 |

---

## 6. 常见问题

| 现象 | 排查 |
|---|---|
| 编译报 `AIOT_JSON_MAX_TOKENS` 重定义 | 只在工程宏里定义一次，不要同时改头文件 |
| 卡在 `WAIT_LOGIN` | 检查 `bsp_tcp_send` 是否真的把 `\n` 也发了；检查密码/环境 |
| 收不到下行 | 确认平台下发的 `channel` 是 TCP；设备在线；TCP 连接未断 |
| 内存不足 | 减小 TX/RX；`AIOT_JSON_MAX_TOKENS=64`；不要用 MQTT 客户端 |
| HardFault | 栈不足（解析栈约 1 KB）；检查 `aiot_init` 的缓冲区是否是局部变量被释放 |

---

## 7. 参考

- 骨架：[`examples/iar/app_aiot.c`](../examples/iar/app_aiot.c)
- API：[`docs/06-API参考.md`](06-API参考.md)
- 移植：[`docs/05-移植指南.md`](05-移植指南.md)
