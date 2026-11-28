# 南向示例（C / Python）

| 文件 | 用途 |
|---|---|
| `c/minimal_device.c` | 最小设备骨架：`aiot_init` → `lgn` → 上报 → 下行 `order` 回执 |
| `python/probe.py` | 登录探测：连 TCP 41032，发 `lgn`，可选上报一个值 |
| `python/simulate_device.py` | 假设备模拟器：周期上报 + 自动回 `order_conf` / `facs_reply` |

## C 示例

- SDK 在技能自带 `../../sdk/`：`sdk/dist/aiot_sdk.c` + `sdk/dist/aiot.h` + `sdk/dist/aiot_types.h`；
- `my_send` / `my_now_ms` 需要按网络层补全；
- PC 联调可用 `sdk/port/aiot_port_posix.c`（见 `sdk/README.md`）；
- 编译进 MCU 工程时**不要**带 `port/aiot_port_posix.c`。

## Python 示例

```bash
set AIOT_DEVICE=WANCD1-0000000007
set AIOT_DEVICE_PASSWORD=123456

python probe.py                      # 只登录
python probe.py --report wd=25.3     # 登录后上报一次
python simulate_device.py            # 模拟设备：30s 上报一次，自动回指令
python simulate_device.py --host siot.yzlkj.com --interval 60
```

## 注意

- 41032 / 40501 / 1883 均为**明文无 TLS**，只在 APN / VPN / 内网使用。
- 设备密码是长期凭证，不要写进示例或提交仓库。
- 上报节奏按 `heartbeat_sec` / `keepalive_sec` 设计，不要按秒级压；南向不走北向 REST 配额。
- 遇到 `code=4` 表示未登录：先 `lgn` 再发业务；`code=3` 是密码错误，别高频重试。
