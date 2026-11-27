# 南向接口库（C / Python）

一个协议功能一个方法；加载技能后可直接调用，或按它改写别的语言。

## Python（`lib/south_client.py`，标准库）

```python
import sys; sys.path.insert(0, "lib")
from south_client import SouthDevice

d = SouthDevice(device_id="WANCD1-0000000007", password="123456").connect()
d.login()                       # lgn
d.report(wd="25.3")             # facs
d.heartbeat()                   # hear
d.order_conf(tra)               # order_conf
d.order_reply(tra, sw="1")      # facs_reply
d.backfill([{"ts": 1792714948, "values": {"kk1": "11"}}])
d.ota_info("fw_1"); d.ota_get("fw_1", 0)
d.close()
```

| 协议功能 | Python 方法 | C 头文件函数 |
|---|---|---|
| lgn | `login()` | `aiot_dev_connected()`（自动 lgn） |
| facs | `report(**kv)` / `report_pairs()` | `aiot_dev_report()` / `aiot_dev_report_begin/add/end()` |
| hear | `heartbeat()` | `aiot_dev_heartbeat()` |
| get_time | `get_time()` | `aiot_dev_request_time()` |
| order_conf | `order_conf(tra)` | `aiot_dev_order_confirm()` |
| facs_reply | `order_reply(tra, **kv)` | `aiot_dev_order_reply()` |
| facs_his | `backfill(points)` | `aiot_dev_backfill_begin/add/timestamp/end()` |
| gfinfo | `ota_info(id)` | `aiot_dev_ota_info()` |
| gfcet | `ota_get(id, index)` | `aiot_dev_ota_get()` |
| lgn_facs（UDP） | `wakeup(**kv)` | `aiot_dev_udp_wakeup()` |
| get_order（UDP） | `pull_order()` | —（SDK 内部） |
| MQTT 收包 | — | `aiot_dev_mqtt_feed()` + `aiot_mqtt_topic_*` |
| 连接/收包/轮询 | `connect()` / `recv()` / `serve_forever()` | `aiot_dev_connected/feed/poll` |

## C（`lib/aiot_device.h`，头文件内联）

```c
#include "aiot_device.h"

aiot_dev_init(&cli, &cfg, tx, sizeof tx, rx, sizeof rx);
aiot_dev_connected(&cli);
aiot_dev_feed(&cli, buf, n);
aiot_dev_poll(&cli, now_ms());
aiot_dev_report(&cli, kvs, count);
```

- 只是给 SDK 的接口起“设备语义”的名字，行为与 SDK 完全一致；
- 编译需带 `aiot.h` 与 `dist/aiot_sdk.c`。

## 帧与错误

- 帧格式来自 `docs/01-协议说明.md`（2026-11-04 实测）：`top/ter/data/func/args/fid`。
- 业务码：0 成功、1 参数、2 对象不存在、3 认证失败、4 未登录、9 未知函数。
- 南向不适用北向 REST 配额；上报按 `heartbeat_sec` / `keepalive_sec` 设计。

## 离线自测

```bash
python tests/test_south.py     # 起本地 mock TCP，跑 13 项
```
