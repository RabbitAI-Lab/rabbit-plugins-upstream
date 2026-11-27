# AIoT C SDK（云智联南向设备接入）

面向 **云智联 AIoT 平台**（`aiot.yzlkj.com`）南向接口的 C89 设备端 SDK。目标是把“设备登录、数据上报、心跳、下行指令、历史补传、OTA 查询、UDP 低功耗、MQTT 接入”封装成一组可直接拖进 **Keil MDK / IAR EWARM / GCC** 工程的源文件，让 MCU 程序只关心业务，不重复实现协议。

> 本 SDK 不依赖 `malloc`、不依赖操作系统、不依赖 `printf`，核心只使用 `stddef.h` / `string.h`，类型定义在自带的 `aiot_types.h` 中，**不依赖 `<stdint.h>`**。网络层通过 `send` / `now_ms` 两个回调接入，适配 lwIP、W5500、ESP8266/4G AT 模组、Linux/Windows socket 都很简单。

---

## 1. 支持范围

| 接入方式 | 端口 | SDK 支持 | 说明 |
|---|---:|---|---|
| TCP 长连接 | 41032 | ✅ 完整 | JSON 一行一帧；连接后 `lgn`；支持下行 `order` |
| UDP 低功耗 | 40501 | ✅ 完整 | `lgn_facs` 免登录上报；`get_order` 拉取挂起指令；`ack` 回执 |
| MQTT | 1883 | ✅ 协议层 + 可选客户端 | clientId/username=设备ID，password=设备密码；发布/订阅 topic |
| 农污 DL/T645 | 40032 | ❌ 不包含 | 老协议，和本 SDK 的 JSON 南向接口不同 |

支持的上行功能：

- `lgn`：TCP 登录（SDK 自动完成）
- `facs`：实时数据
- `facs_his`：历史数据补传（一包多时间点，≤1000 点）
- `hear`：心跳保活（SDK 自动发送）
- `facs_reply`：指令执行结果
- `order_conf`：指令收到确认（默认自动发送）
- `get_time`：校时
- `get_order`：UDP 拉取挂起指令
- `gfinfo` / `gfcet`：OTA 固件信息 / 分片下载
- 自定义 `func`：`aiot_send_func()`

支持的下行指令：

- `set`：设置设施值
- `get`：查询设施值
- `upfs`：OTA 分片下发

---

## 2. 最快的验证方式（PC）

以下命令在 Linux / macOS / Windows（MinGW 或 WSL）均可运行。示例使用平台**测试环境**域名 `ciot.yzlkj.com`；生产环境是 `siot.yzlkj.com`。

```bash
# TCP
cc -std=c89 -Iinclude -Iport \
   examples/host_tcp_demo.c src/aiot.c src/aiot_json.c port/aiot_port_posix.c \
   -o host_tcp_demo
./host_tcp_demo ciot.yzlkj.com 41032 <设备ID> <设备密码> 30

# UDP
cc -std=c89 -Iinclude -Iport \
   examples/host_udp_demo.c src/aiot.c src/aiot_json.c port/aiot_port_posix.c \
   -o host_udp_demo
./host_udp_demo ciot.yzlkj.com 40501 <设备ID> <设备密码> 8

# MQTT（自带极简客户端，无 TLS）
cc -std=c89 -Iinclude -Iport \
   examples/host_mqtt_demo.c src/aiot.c src/aiot_json.c \
   port/aiot_port_posix.c port/aiot_mqtt_client.c \
   -o host_mqtt_demo
./host_mqtt_demo ciot.yzlkj.com 1883 <型号ID> <设备ID> <设备密码> 15
```

Windows 下链接 socket 需要加 `-lws2_32`。

运行后应看到：

```text
[demo] connected, waiting for login...
[demo] login func=lgn code=0 result=...
[demo] report -> sent
[demo] result func=facs code=0 fid=F1 result=(json)
[demo] result func=get_time code=0 fid=T1 result=2026-11-04 01:07:50
```

在平台页面给设备下发 `set` 指令，会看到：

```text
[demo] ORDER cmd=set tra=... args=["DEVICE-ID","sw","0"]
[demo] order_reply -> sent
```

---

## 3. 集成到 Keil / IAR（3 步）

### 第 1 步：添加文件

把下面三个文件加入工程即可（推荐使用 `dist/` 下的合并版）：

```text
dist/aiot_sdk.c     ← 核心 + JSON，单文件
dist/aiot.h         ← 公开 API
dist/aiot_types.h   ← C89 定宽类型
```

或者使用源码树：

```text
src/aiot.c
src/aiot_json.c
include/aiot.h
include/aiot_types.h
```

把 `include/` 加入头文件搜索路径。**不需要**添加 `port/aiot_port_posix.c`（那是 PC socket 适配层，MCU 用不到）。

### 第 2 步：提供两个回调

```c
#include "aiot.h"

static aiot_client_t g_aiot;
static aiot_u8 g_tx[2048];
static aiot_u8 g_rx[4096];

/* 把数据发到 TCP socket / WiFi 模组 / 4G 模组 */
static int my_send(void *user, const aiot_u8 *data, size_t len)
{
    (void)user;
    return bsp_tcp_send(data, len) == (int)len ? 0 : -1;
}

/* 单调毫秒时钟 */
static aiot_u32 my_now(void *user)
{
    (void)user;
    return HAL_GetTick();
}

static void my_event(void *user, const aiot_event_t *ev)
{
    (void)user;
    if (ev->type == AIOT_EV_LOGIN && ev->code == 0) {
        aiot_kv_t kv[] = {
            {"temp", "25.5"},
            {"hum",  "60"},
        };
        aiot_report(&g_aiot, kv, 2, NULL);
    }
    if (ev->type == AIOT_EV_ORDER) {
        /* 执行 ev->cmd，然后用实际值回执 */
        aiot_kv_t kv = {"sw", "1"};
        aiot_order_reply(&g_aiot, ev->tra, &kv, 1);
    }
}

void app_aiot_init(void)
{
    aiot_config_t cfg = {0};
    cfg.device_id = "WANCD2-0000001008";
    cfg.password  = "设备密码";
    cfg.mode      = AIOT_MODE_TCP;
    cfg.send      = my_send;
    cfg.now_ms    = my_now;
    cfg.on_event  = my_event;
    cfg.keepalive_sec = 300;
    cfg.heartbeat_sec = 60;

    aiot_init(&g_aiot, &cfg, g_tx, sizeof g_tx, g_rx, sizeof g_rx);
}
```

### 第 3 步：接入网络事件与主循环

```c
/* TCP 连接成功后 */
aiot_client_connected(&g_aiot);

/* socket / 模组收到数据后（可以是任意长度） */
aiot_client_rx(&g_aiot, data, len);

/* 主循环，建议 10~100 ms 调一次 */
aiot_client_poll(&g_aiot, HAL_GetTick());

/* 断线时 */
aiot_client_disconnected(&g_aiot);
```

完整骨架见 [examples/keil/app_aiot.c](examples/keil/app_aiot.c) 和 [docs/03-Keil集成.md](docs/03-Keil集成.md)。

---

## 4. 代码结构

```text
include/aiot.h                 公开 API（include 这个即可）
include/aiot_types.h           C89 定宽类型（aiot_u8/u16/u32/i32）
src/aiot.c                     协议状态机、帧构造、事件解析
src/aiot_json.c                有界字符串构造器 + 轻量 JSON 解析器
src/aiot_internal.h            内部接口
port/aiot_port.h               PC/RTOS socket 适配层声明
port/aiot_port_posix.c         POSIX / Windows socket 实现
port/aiot_mqtt.h               可选 MQTT 客户端声明
port/aiot_mqtt_client.c        可选 MQTT 3.1.1 客户端（QoS0/1）
examples/                      PC demo + Keil/IAR 骨架
tests/test_all.c               183 项主机单元测试
docs/                          协议、集成、API、移植、排障
dist/                          单文件合并版 + aiot.h + aiot_types.h
```

资源占用（ARM Cortex-M，`-Os`，粗略值，实际以工程 map 为准）：

| 模块 | Flash | RAM（不含用户 TX/RX） |
|---|---:|---:|
| 核心 + JSON | 约 12–18 KB | 约 300 B（client 对象） |
| 解析栈 | — | 约 1.0–1.4 KB（`handle_frame` 栈帧） |
| MQTT 可选客户端 | 约 4–6 KB | 约 4 KB（`aiot_mqtt_t` 内含 2×2 KB 缓冲） |

> 如果 RAM 紧张：把 `AIOT_JSON_MAX_TOKENS` 定义为 64，把 `g_rx` 设为 2048；OTA 的 `upfs` 大包需要更长 RX（建议 4096）。具体见 [docs/05-移植指南.md](docs/05-移植指南.md)。

---

## 5. 已实测

2026-11-04 在平台测试环境（`ciot.yzlkj.com`）用真实设备完成：

- TCP 登录、`facs` 上报、`get_time`、`hear`、`facs_his`
- TCP 下行 `set` 指令 → 自动 `order_conf` + `facs_reply` → 平台指令状态 `succeeded`
- UDP `lgn_facs`、`get_order`、`get_time`，`ack` 原样回传
- MQTT CONNECT（设备ID/密码）、SUBSCRIBE、QoS1 PUBLISH、下行 `set` → `succeeded`
- C89/C90 严格模式（`-std=c89 -pedantic -Werror`）编译通过
- 主机单元测试：**183 checks, 0 failures**

协议细节、实测中的坑和平台返回码见 [docs/01-协议说明.md](docs/01-协议说明.md)，真实抓包摘录见 [docs/08-实测报文.md](docs/08-实测报文.md)。

---

## 6. 安全提示

- 平台 41032/40501/1883 都是**明文**端口，没有 TLS。不要把设备密码和业务数据直接暴露在公网；建议使用 APN/VPN/内网专线，或在网关侧做 TLS 终结。
- `device password` 是设备身份凭证，不要写死在公开仓库；量产设备建议一机一密，并通过安全分区/加密存储保存。
- MQTT 1883 的认证方式是 **clientId=设备ID、username=设备ID、password=设备密码**；不要复用用户账号密码。
- 平台测试环境与生产环境是两套设备服务器：测试 `ciot.yzlkj.com`，生产 `siot.yzlkj.com`。设备在哪个环境由平台设备记录决定，连错环境会表现为“设备不存在/一直离线”。

---

## 7. License

MIT，见 [LICENSE](LICENSE)。协议字段和平台文档版权归平台方所有；本仓库只包含独立实现的客户端代码。



