# YZL-AIoT 南向（yzl-aiot-south）

> 云智联 AIoT 平台 `aiot.yzlkj.com` 的**南向设备端 C SDK**：让 MCU 用最少的代码连上平台。
> **只服务南向设备端**；应用侧接入用 `yzl-aiot-north`，开放平台 `open.yzlkj.com` 用 `yzl-open-api`。

**当前版本：v1.3.0**（自带接口库：C / Python）

## 平台边界

| 你的需求 | 用哪个技能 | 入口 / 协议 |
|---|---|---|
| MCU / 4G 模组固件接入 | **本技能 `yzl-aiot-south`** | TCP 41032 / UDP 40501 / MQTT 1883 |
| 后端 / 看板 / Webhook 读数据 | `yzl-aiot-north` | `aiot.yzlkj.com` REST / MQTT / Bridge |
| 开放平台 API Key 取数 / 开关水阀 | `yzl-open-api` | `open.yzlkj.com` Open API v2 |
| 不确定 | `yzl-aiot`（平台入口） | 负责分流 |

## 安装

```bash
clawhub install yzl-aiot-south
```

技能自带 `lib/`（`south_client.py`、`aiot_device.h`）与 `sdk/`（C SDK 源码、移植层、文档、示例、单测），不依赖外部工程。

## 快速使用

```bash
python tool.py frames              # 打印 lgn / facs / hear / order_conf / facs_reply 标准帧
python tool.py probe WANCD1-0000000007 123456            # 连接 ciot:41032 并登录
python tool.py probe WANCD1-0000000007 123456 --report wd=25.3
python tool.py report WANCD1-0000000007 123456 wd 25.3   # 登录后上报一个值
python tool.py check F:\proj\my_firmware                 # 检查固件工程是否接好 SDK
python tool.py check-update                              # 检查技能版本
```

## 接口库

```python
import sys; sys.path.insert(0, "lib")
from south_client import SouthDevice
d = SouthDevice("WANCD1-0000000007", "123456").connect()
d.login(); d.report(wd="25.3"); d.heartbeat(); d.close()
```

C 侧用 `lib/aiot_device.h`（每个协议功能一个 `aiot_dev_*` 函数）。完整对照见 `lib/README.md`。

## 示例

`examples/` 下有 C 与 Python 两套示例：

```bash
python examples/python/probe.py --report wd=25.3
python examples/python/simulate_device.py
# C 骨架：examples/c/minimal_device.c（配 dist/ 与 port/ 使用）
```

## 限频

南向设备链路（TCP 41032 / UDP 40501 / MQTT 1883）**不适用**北向 REST 的用户配额（基础 + 设备数 × 每台追加，按秒计；写接口 3 倍）。
上报节奏按 `heartbeat_sec` / `keepalive_sec` 设计，不要按秒级压。
开放平台 `open.yzlkj.com` 的按接口限速与「封 IP」与本平台无关。

## 文档

- 协议：`aiot-c-sdk\docs\01-协议说明.md`；实测报文：`08-实测报文.md`
- 集成：`03-Keil集成.md`、`04-IAR集成.md`、`05-移植指南.md`
- API：`06-API参考.md`；OTA 与排障：`07-OTA与故障排查.md`
- ML307C OpenCPU：`09-ML307C-OpenCPU工程.md`

## 联系

- 电话：089836692518/18689850608
- 邮箱：yzlkj@yzlkj.com
- 官网：www.yzlkj.com
