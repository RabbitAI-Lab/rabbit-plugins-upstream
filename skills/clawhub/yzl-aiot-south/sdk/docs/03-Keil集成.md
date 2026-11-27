# 03 · Keil MDK 集成

以 Keil MDK 5 + ARM Compiler 5/6 + STM32（或任何 Cortex-M）为例。SDK 本身不依赖 STM32 HAL，只依赖你提供的 `send` / `now_ms`。

---

## 1. 添加文件

推荐直接把合并版加入工程：

```text
aiot-c-sdk/dist/aiot_sdk.c
aiot-c-sdk/dist/aiot.h
aiot-c-sdk/dist/aiot_types.h
```

操作：

1. Keil 工程窗口 → `Project` → `Manage` → `Project Items`；
2. 新建组 `AIoT`；
3. 把 `aiot_sdk.c` 加到 `AIoT` 组；
4. `Options for Target` → `C/C++` → `Include Paths` 加入 `dist` 目录（或 `include` 目录）；
5. `C/C++` → 选择 C90/C89 模式（ARMCC 5 勾选 `C90`；ARMCC 6 用 `--c90`）。

不需要添加：

- `port/aiot_port_posix.c`（PC socket 适配层）
- `port/aiot_mqtt_client.c`（除非你用 PC/RTOS 且没有 MQTT 栈）

---

## 2. 实现 BSP 回调

假设你的 WiFi/4G 模组已经提供：

```c
int  bsp_tcp_connect(const char *host, aiot_u16 port);
int  bsp_tcp_send(const aiot_u8 *data, aiot_u32 len);
void bsp_tcp_close(void);
```

则：

```c
#include "aiot.h"
#include <string.h>

static aiot_client_t g_aiot;
static aiot_u8 g_tx[2048];
static aiot_u8 g_rx[4096];

static int aiot_send(void *user, const aiot_u8 *data, size_t len)
{
    (void)user;
    if (bsp_tcp_send(data, (aiot_u32)len) != (int)len) {
        return -1;
    }
    return 0;
}

static aiot_u32 aiot_now(void *user)
{
    (void)user;
    return HAL_GetTick();   /* 1 ms 单调递增即可 */
}
```

> `HAL_GetTick()` 默认 1 ms 递增。如果你的 SysTick 是 10 ms，请自行换算成 ms。

---

## 3. 事件回调

```c
static void aiot_event(void *user, const aiot_event_t *ev)
{
    (void)user;
    switch (ev->type) {
    case AIOT_EV_LOGIN:
        if (ev->code == 0) {
            aiot_kv_t kv[] = {
                {"temp", "25.5"},
                {"hum",  "60"},
                {"ver",  "fw-1.0.0"},
            };
            aiot_report(&g_aiot, kv, 3, NULL);
        } else {
            /* code=3 密码错误；不要无限重试 */
        }
        break;

    case AIOT_EV_ORDER:
        if (strcmp(ev->cmd, "set") == 0) {
            /*
             * ev->args_json 形如 ["DEVICE","sw","1"]
             * 真实项目应解析出 key/value，执行 GPIO/PWM，再回实际值。
             */
            aiot_kv_t kv = {"sw", "1"};
            aiot_order_reply(&g_aiot, ev->tra, &kv, 1);
        } else if (strcmp(ev->cmd, "get") == 0) {
            aiot_kv_t kv = {"sw", "1"};
            aiot_order_reply(&g_aiot, ev->tra, &kv, 1);
        }
        break;

    case AIOT_EV_RESULT:
        /* 按 ev->func / ev->fid 处理平台回执 */
        break;

    case AIOT_EV_TIMEOUT:
    case AIOT_EV_ERROR:
        /* 置重连标志，由主循环关闭 socket 并重连 */
        break;

    default:
        break;
    }
}
```

---

## 4. 初始化和主循环

```c
void app_aiot_init(void)
{
    aiot_config_t cfg;
    memset(&cfg, 0, sizeof cfg);

    cfg.device_id     = "WANCD2-0000001008";
    cfg.password      = "设备密码";
    cfg.mode          = AIOT_MODE_TCP;
    cfg.send          = aiot_send;
    cfg.now_ms        = aiot_now;
    cfg.on_event      = aiot_event;
    cfg.keepalive_sec = 300;
    cfg.heartbeat_sec = 60;

    aiot_init(&g_aiot, &cfg, g_tx, sizeof g_tx, g_rx, sizeof g_rx);
}

/* 在 WiFi/4G 连接建立后调用 */
void app_aiot_on_connected(void)
{
    aiot_client_connected(&g_aiot);
}

/* 在串口/模组收到 TCP 数据后调用；可多次、任意长度 */
void app_aiot_on_data(const aiot_u8 *data, aiot_u32 len)
{
    aiot_client_rx(&g_aiot, data, (size_t)len);
}

/* main while(1) 里调用 */
void app_aiot_loop(void)
{
    aiot_client_poll(&g_aiot, HAL_GetTick());
}
```

---

## 5. ESP8266 AT 模组接入示例

SDK 不直接发 AT 命令；你只需要把“连接、发送、接收”三件事做好。

### 5.1 连接

```text
AT+CIPMUX=0
AT+CIPSTART="TCP","ciot.yzlkj.com",41032
```

收到 `CONNECT` 后调用 `aiot_client_connected()`。SDK 会自动发 `lgn`，你看到的发送内容类似：

```json
{"top":"func","ter":"WANCD2-0000001008","data":[{"func":"lgn","args":["密码"],"fid":"L1"}]}
```

### 5.2 发送

```text
AT+CIPSEND=<len>
<等待 '>'
<写入 len 字节 JSON>
```

`aiot_send()` 里把 `data/len` 交给 `AT+CIPSEND`。注意：AT 模组通常要求一次发送不超过 2048 字节；SDK 的 TX 默认 2048，够用。

### 5.3 接收

模组上报格式：

```text
+IPD,<len>:<len 字节数据>
```

解析出 `<len>` 字节后，原样交给：

```c
aiot_client_rx(&g_aiot, payload, len);
```

**不要**在 `+IPD` 回调里做耗时业务；把数据拷到环形缓冲，主循环再处理，避免阻塞模组。

### 5.4 断线

模组上报 `CLOSED` 或 `ERROR` 时：

```c
aiot_client_disconnected(&g_aiot);
/* 关闭 socket，按退避重连 */
```

---

## 6. 资源与优化

### 6.1 减小 RAM

在 `Options for Target` → `C/C++` → `Define` 加：

```text
AIOT_JSON_MAX_TOKENS=64
```

可把 `handle_frame()` 的 token 栈从约 1 KB 降到约 0.5 KB。代价：单帧能解析的字段变少；常规 `order`/`result` 足够，OTA 大包建议保留 128。

### 6.2 减小 RX

- 不做 OTA：`g_rx[2048]`
- 做 OTA/大分片：`g_rx[4096]`

### 6.3 关闭不用的功能

- 只上报，不处理下行：可以不订阅 / 不实现 `AIOT_EV_ORDER`，但 TCP 仍可能收到 order，SDK 会回调；忽略即可。
- 不需要自动心跳：`cfg.no_auto_heartbeat = 1`，自己发 `aiot_heartbeat()`。
- 不需要自动确认：`cfg.no_auto_order_conf = 1`。

### 6.4 看门狗

`aiot_client_poll()` 不做阻塞等待；可以放在主循环。不要在 `on_event` 里调用 `aiot_client_rx()` 递归处理。

---

## 7. 常见编译问题

| 现象 | 处理 |
|---|---|
| `unknown type name 'aiot_u8'` | 确认 `aiot.h` / `aiot_types.h` 已加入 include 路径；ARMCC 5 选 C90/C89 模式 |
| `undefined symbol aiot_...` | `aiot_sdk.c` 没加入工程，或只加了头文件 |
| `L6218E: Undefined symbol memmove` | C 库已包含；检查是否用了 `--no_stdlib` |
| 栈溢出/HardFault | 增大启动文件 Stack_Size；`handle_frame` 需要约 1 KB 栈 |
| 收到数据但无事件 | 检查是否带 `\n`；TCP 流必须按行拆，SDK 需要换行 |
| 一直 `AIOT_STATE_WAIT_LOGIN` | 没收到 lgn 回执；检查发送是否真的发出、密码、环境域名 |

---

## 8. 最简验证顺序

1. 串口打印 `aiot_client_connected()` 的返回值；
2. 打印 `aiot_send()` 收到的每一帧（确认 lgn 已发出）；
3. 打印 `aiot_client_rx()` 收到的原始字节（确认有 `\n`）；
4. 看到 `AIOT_EV_LOGIN code=0` 后再发 `facs`；
5. 平台设备详情页应变为在线，最新数据出现。

---

## 9. 参考工程

- 骨架：[`examples/keil/app_aiot.c`](../examples/keil/app_aiot.c)
- 主机可运行版本：[`examples/host_tcp_demo.c`](../examples/host_tcp_demo.c)
- 合并版源文件：[`dist/aiot_sdk.c`](../dist/aiot_sdk.c)
