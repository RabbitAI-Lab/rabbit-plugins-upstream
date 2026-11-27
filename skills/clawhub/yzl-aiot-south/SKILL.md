---
name: yzl-aiot-south
description: YZL-AIoT 南向设备端 C SDK（yzl-aiot-south；C89，无 malloc / 无 OS 依赖、不依赖 stdint.h）。用于给 STM32/GD32 等 MCU 固件（Keil MDK、IAR EWARM、GCC）接入 aiot.yzlkj.com 南向接口：TCP 41032 登录与上报、UDP 40501 低功耗、MQTT 1883、下行 set/get 指令与回执、facs_his 历史补传、OTA（gfinfo/gfcet/upfs）。Use when writing, porting, or debugging device-side firmware that connects a device to the 云智联 AIoT platform, or when the user mentions 南向、设备端、MCU、4G 模组、lwIP、W5500、Keil、IAR。
---

> 🧭 **平台边界**：本技能只服务 `aiot.yzlkj.com` 南向（设备端固件）。
> 应用侧接入 → `yzl-aiot-north`；平台总入口 → `yzl-aiot`；开放平台 `open.yzlkj.com` → `yzl-open-api`（不是同一套系统）。
> 南向走 TCP 41032 / UDP 40501 / MQTT 1883，和北向 REST 是两条链路。

## ⚙️ 运行时要求

- **C89**：无 `malloc`、无 OS 依赖、不依赖 `stdint.h`；裸机或 FreeRTOS 均可
- **工具链**：Keil MDK、IAR EWARM、GCC（STM32 / GD32 / …）
- **移植面**：只要求 `send(buf, len)` 与 `now_ms()` 两个回调；网络层可用 4G/WiFi AT 模组、lwIP、W5500 或裸 socket
- **MQTT 模式**：额外需要 `product_id`
- **接口库**：`lib/south_client.py`（Python，标准库）与 `lib/aiot_device.h`（C，头文件内联），一个协议功能一个方法/函数

## 🚦 限频说明

- 南向设备链路（TCP 41032 / UDP 40501 / MQTT 1883）**不适用**北向 REST 的用户配额（基础配额 + 设备数 × 每台追加，按秒计；写接口 3 倍）
- 上报节奏按 `heartbeat_sec` / `keepalive_sec` 设计，**不要按秒级压**
- 开放平台 `open.yzlkj.com` 的按接口限速与「非 0 返回封 IP」与本平台无关

## 🌱 YZL-AIoT 南向（aiot.yzlkj.com 设备端）

**一句话：让一块 MCU 用最少的代码连上平台。**

设备侧要做的四件事：登录（`lgn`）、上报（`facs`）、心跳（`hear`）、响应下行指令（`set` / `get` / `upfs`）；历史补传与 OTA 由 SDK 封装。

## ⚡ 快速集成（4 步）

1. **加文件**：`dist/aiot_sdk.c`、`dist/aiot.h`、`dist/aiot_types.h`；头文件搜索路径加 `include/`（或 dist 目录）。
   MCU 工程**不要**加 `port/aiot_port_posix.c`（那是 PC socket 适配层）。
2. **填配置**：`device_id`、`password`、`mode`、`send`、`now_ms`、`on_event`、`keepalive_sec`(300)、`heartbeat_sec`(60，必须 < keepalive)。MQTT 还要 `product_id`。
3. **分配缓冲**：`tx/rx` 各 ≥256，常用 `tx 2048 / rx 4096`（OTA 大包需 4096），然后 `aiot_init()`。
4. **接网络事件与主循环**（10–100 ms 调一次）：

```c
aiot_client_connected(&c);            /* TCP 连接成功 → 自动发 lgn；UDP/MQTT 直接 ONLINE */
aiot_client_rx(&c, data, len);        /* TCP 收到任意长度字节，SDK 按 \n 拆帧 */
aiot_client_poll(&c, HAL_GetTick());  /* 主循环：心跳、登录超时、链路超时 */
aiot_client_disconnected(&c);         /* 断线 */
```

UDP / MQTT 收包改用 `aiot_client_rx_datagram()` / `aiot_mqtt_rx()`：每次一个完整 JSON，不带 `\n`。

## 🧩 事件与指令

```c
static void on_event(void *u, const aiot_event_t *ev) {
    (void)u;
    if (ev->type == AIOT_EV_LOGIN && ev->code == 0) {
        /* ONLINE，可以开始上报 */
    }
    if (ev->type == AIOT_EV_ORDER) {          /* set / get / upfs；order_conf 默认已自动发 */
        aiot_kv_t kv = {"sw", "1"};
        aiot_order_reply(&c, ev->tra, &kv, 1); /* tra 必须原样回传 */
    }
}
```

## 📡 协议与端口

| 链路 | 端口 | 特点 |
|---|---|---|
| TCP | 41032 | 一行一帧 JSON（`\n` 分隔）；登录 + 实时 + 历史补传 |
| UDP | 40501 | 低功耗：`lgn_facs`、`get_order`，单包 < 1200 字节 |
| MQTT | 1883 | `clientId` = `username` = 设备 ID，`password` = 设备密码 |

- 域名分环境：测试 `ciot.yzlkj.com`、生产 `siot.yzlkj.com`；连错表现为「设备不存在 / 一直离线」
- 未登录发业务返回 `code=4`；SDK 在 `WAIT_LOGIN` 状态会直接拒发

## 🔧 API 速查

| 用途 | API |
|---|---|
| 初始化 / 连接 / 断开 | `aiot_init` `aiot_client_connected` `aiot_client_disconnected` |
| 收包 | `aiot_client_rx`（TCP 流）`aiot_client_rx_datagram`（UDP/MQTT）`aiot_mqtt_rx` |
| 主循环 | `aiot_client_poll`、`aiot_client_state`、`aiot_client_last_rx_ms` |
| 实时上报 | `aiot_report`，或 `aiot_report_begin/add/end`（大包分段） |
| 历史补传 | `aiot_backfill_begin/add/timestamp/end`（仅 TCP/MQTT，≤1000 点/帧） |
| 心跳 / 校时 | `aiot_heartbeat` `aiot_request_time` |
| 指令回执 | `aiot_order_confirm` `aiot_order_reply` |
| UDP 拉指令 / 唤醒 | `aiot_request_order` `aiot_udp_wakeup` |
| OTA | `aiot_ota_info` `aiot_ota_get`（结果在 `AIOT_EV_RESULT.result_json`） |
| MQTT topic | `aiot_mqtt_topic_up` `aiot_mqtt_topic_down_order` `aiot_mqtt_topic_down_result` |
| 扩展 | `aiot_send_func`（任意 `func`，args 形如 `["x",1]`） |
| 解析下行 args | `aiot_args_count` `aiot_args_get_str` `aiot_args_get_u32` |
| 工具 | `aiot_version` `aiot_strerror` `aiot_state_name` |

返回值 `0` / `AIOT_OK` 为成功，负值为错误；只有 `AIOT_STATE_ONLINE` 才能发业务。

## ⚠️ 常见坑（实测）

1. TCP 41032 一次 `recv` 可能读到**多行**，必须按 `\n` 拆（SDK 已处理，自己写收包时注意）。
2. 域名分环境：测试 `ciot.yzlkj.com`、生产 `siot.yzlkj.com`。
3. 未登录发业务返回 `code=4`。
4. UDP 的 `lgn_facs` 与 `get_order` **不要连发**（会先到 `get_order`、回 `code=4`），等回执再拉；单包 < 1200 字节。
5. MQTT 匿名必失败；普通上报没有回执。
6. 下行 `tra` 必须原样回传，否则平台指令不会变 `succeeded`。
7. `facs_his` 的 timestamp 必须是 Unix 秒**数字**，字符串会整包参数错误。
8. `get_time` 平台实测返回 `"2026-11-04 01:05:14"` 这类字符串（文档写数字），两种都兼容。
9. **非线程安全**：多任务共享 client 要自己加锁；`on_event` 里不要阻塞、不要递归调 `aiot_client_rx`。
10. `args_json` / `result_json` 只在回调期间有效，需要留存就自己拷贝。

## ✅ 验证流程

1. 先在 PC 跑对应 demo（编译命令见 SDK `README.md` 第 2 节；Windows 链接加 `-lws2_32`），确认 `lgn` → `facs` → `get_time` 正常；
2. 平台下发 `set`：设备应打出 `[demo] ORDER cmd=set ...`，随后自动 `order_conf` + `facs_reply`，平台指令状态变 `succeeded`；
3. 主机单元测试：`tests/test_all.c`（183 checks, 0 failures）；
4. 资源预算（Cortex-M，`-Os`）：核心 + JSON 约 12–18 KB Flash、约 300 B RAM、解析栈约 1.0–1.4 KB；RAM 紧张时 `AIOT_JSON_MAX_TOKENS=64`、`g_rx` 2048（OTA 仍需 4096）。

## 📦 移植与模组

- **ML307C / 中移 OpenCPU**（代码跑在模组里、无外挂 MCU）：走 `docs\09-ML307C-OpenCPU工程.md`，用 lwIP socket + CMSIS-RTOS2 落地，含建工程步骤、`send`/`now_ms` 参考移植层与踩坑清单。
- 其他网络层：实现 `send` 与 `now_ms` 即可；AT 模组模式注意 `send` 的阻塞时间，别在回调里等待。

## 🔐 安全

- 41032 / 40501 / 1883 全部**明文无 TLS**；公网必须走 APN / VPN / 内网专线，或在网关侧做 TLS 终结。
- 设备密码是长期凭证：一机一密、不要提交到公开仓库、放安全存储区。
- 平台账号 / API Key 不要下发到设备，设备只用设备密码。

## 🧰 接口库（C / Python）

| 文件 | 语言 | 说明 |
|---|---|---|
| `lib/south_client.py` | Python（标准库） | `SouthDevice`：lgn / facs / hear / get_time / order_conf / order_reply / backfill / OTA |
| `lib/aiot_device.h` | C（头文件内联） | 每个协议功能一个 `aiot_dev_*` 函数，转发 SDK |
| `lib/README.md` | — | 功能 ↔ 方法 ↔ 函数对照表 |

`tests/` 内有本地 mock 与自测：`python tests/test_south.py`。

## 📁 示例（C / Python）

| 文件 | 用途 |
|---|---|
| `examples/c/minimal_device.c` | 最小设备骨架：`aiot_init` → `lgn` → 上报 → 下行回执 |
| `examples/python/probe.py` | 登录探测（TCP 41032），可选上报一次 |
| `examples/python/simulate_device.py` | 假设备模拟器：周期上报 + 自动回 `order_conf` / `facs_reply` |

运行方式与依赖见 `examples/README.md`。

## 📁 本地资源

SDK 已随技能打包在 `sdk/`：

- 单文件合并版：`sdk/dist/aiot_sdk.c` + `sdk/dist/aiot.h` + `sdk/dist/aiot_types.h`
- 头文件 / 移植层：`sdk/include/`、`sdk/port/`
- 文档：`sdk/docs/01-协议说明.md`、`03-Keil集成.md`、`04-IAR集成.md`、`05-移植指南.md`、`06-API参考.md`、`07-OTA与故障排查.md`、`09-ML307C-OpenCPU工程.md`
- 主机示例与单测：`sdk/examples/`、`sdk/tests/`

## 📞 联系与官网

- 电话：089836692518/18689850608
- 邮箱：yzlkj@yzlkj.com
- 官网：www.yzlkj.com

## 版本历史

### v1.3.0 (2026-11-27) — 自带接口库（C / Python）
- 🧰 新增 `lib/south_client.py`（TCP/UDP 全功能）与 `lib/aiot_device.h`（C 内联封装）
- 🖥️ `tool.py` 改为调用自带库
- 🧪 新增 `tests/`：本地 mock TCP + 13 项自测

### v1.2.0 (2026-11-27) — 增加 C / Python 示例
- 📁 新增 `examples/`：`minimal_device.c`、`probe.py`、`simulate_device.py`
- 📝 SKILL / README 增加示例入口

### v1.1.0 (2026-11-27) — 文档重写 + 联调工具
- 📝 SKILL.md 按 `yzl-open-api` 结构重写
- 🧰 新增 `tool.py`：`frames` / `probe` / `report` / `check` / `check-update`
- 📄 补齐 README / CHANGELOG / skill-card / _meta / sync.sh

### v1.0.0 — 南向首版
- 🧩 C89 SDK：TCP 41032 / UDP 40501 / MQTT 1883、`lgn` / `facs` / `hear` / `set` / `get` / `facs_his` / OTA
- 🧪 183 项主机单测；Keil / IAR / GCC 示例；ML307C OpenCPU 移植指南
- 📏 资源预算：约 12–18 KB Flash、约 300 B RAM

> 2026-11-27：技能更名 `aiot-c-sdk` → `yzl-aiot-south`（内容不变）。
