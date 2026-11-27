# 06 · API 参考

头文件：`#include "aiot.h"`（它会自动包含 `aiot_types.h`）

语言标准：**C89/C90**。所有整数类型使用 `aiot_u8` / `aiot_u16` / `aiot_u32` / `aiot_i32`，不使用 `<stdint.h>` 的 `uintN_t`。

所有函数返回 `0` / `AIOT_OK` 表示成功，负值表示错误（见 `aiot_strerror()`）。除非特别说明，`client` 不能为 `NULL`。

---

## 1. 枚举

### `aiot_mode_t`

| 值 | 说明 |
|---|---|
| `AIOT_MODE_TCP` | TCP 长连接 |
| `AIOT_MODE_UDP` | UDP 低功耗 |
| `AIOT_MODE_MQTT` | MQTT |

### `aiot_state_t`

| 值 | 说明 |
|---|---|
| `AIOT_STATE_IDLE` | 未连接 |
| `AIOT_STATE_WAIT_LOGIN` | TCP 已连接，等待 lgn 回执 |
| `AIOT_STATE_ONLINE` | 可发送业务 |
| `AIOT_STATE_ERROR` | 登录失败/链路超时，需重连 |

### `aiot_event_type_t`

见 `aiot_event_t` 一节。

### 返回码

| 值 | 含义 |
|---|---|
| `AIOT_OK` | 成功 |
| `AIOT_ERR_ARG` | 参数非法 |
| `AIOT_ERR_NOMEM` | 缓冲区不足 |
| `AIOT_ERR_STATE` | 当前状态不允许 |
| `AIOT_ERR_IO` | `send` 回调失败 |
| `AIOT_ERR_PARSE` | JSON 解析失败 |
| `AIOT_ERR_OVERFLOW` | 帧超出缓冲区 |
| `AIOT_ERR_TIMEOUT` | 登录/链路超时 |
| `AIOT_ERR_AUTH` | 认证失败（保留） |
| `AIOT_ERR_UNSUPPORTED` | 当前模式不支持 |

---

## 2. 结构体

### `aiot_kv_t`

```c
typedef struct {
    const char *key;
    const char *value;
} aiot_kv_t;
```

- `value` 是字符串；数值也以字符串传入（`"25.5"`、`"60"`），平台按测点 `dataType` 转换。
- `key`/`value` 只在调用期间被读取，SDK 不保存指针。

### `aiot_config_t`

| 字段 | 必填 | 说明 |
|---|---|---|
| `device_id` | 是 | 平台设备 ID，≤31 字符 |
| `product_id` | MQTT 必填 | 型号 ID，≤31 字符；TCP/UDP 可为 NULL |
| `password` | 是 | 设备认证密钥，≤63 字符 |
| `mode` | 是 | `AIOT_MODE_*` |
| `send` | 是 | 发送回调 |
| `now_ms` | 是 | 1 ms 单调时钟 |
| `on_event` | 建议 | 事件回调 |
| `user` | 否 | 原样传给三个回调 |
| `keepalive_sec` | 否 | 平台保活秒数，默认 300 |
| `heartbeat_sec` | 否 | 心跳周期，默认 60；必须 < keepalive |
| `no_auto_order_conf` | 否 | 置 1 关闭收到 order 时自动 `order_conf` |
| `no_auto_heartbeat` | 否 | 置 1 关闭自动 `hear` |

### `aiot_event_t`

| 字段 | 说明 |
|---|---|
| `type` | 事件类型 |
| `code` | 平台 `result.code`（order 事件为 0） |
| `error` | 本地错误码（仅 `AIOT_EV_ERROR`） |
| `func` | 回执的功能名，如 `facs`/`lgn` |
| `fid` | 帧序号 |
| `cmd` | 下行指令 `set`/`get`/`upfs` |
| `tra` | 下行事务 ID |
| `ack` | 平台回传的 ack |
| `result_text` | `result` 为字符串时解码后的文本；否则为空 |
| `args_json` / `args_len` | 下行 `args` 原始 JSON 数组 |
| `result_json` / `result_len` | 平台 `result` 原始 JSON（对象/数组/字符串/数字/null） |

`args_json` / `result_json` 指向内部 RX 缓冲，**只在回调期间有效**。

事件类型：

| 类型 | 触发 |
|---|---|
| `AIOT_EV_CONNECTED` | `aiot_client_connected()` 成功进入连接流程 |
| `AIOT_EV_LOGIN` | 收到 `lgn` 回执（`code=0` 成功） |
| `AIOT_EV_RESULT` | 收到非 lgn 的 `result` |
| `AIOT_EV_ORDER` | 收到下行 `order` |
| `AIOT_EV_DISCONNECTED` | `aiot_client_disconnected()` |
| `AIOT_EV_ERROR` | 本地发送/解析/溢出错误 |
| `AIOT_EV_TIMEOUT` | 登录超时或 TCP 链路超时 |

---

## 3. 生命周期

### `int aiot_init(...)`

```c
int aiot_init(aiot_client_t *client, const aiot_config_t *cfg,
              aiot_u8 *tx_buf, size_t tx_cap,
              aiot_u8 *rx_buf, size_t rx_cap);
```

- 复制 `device_id`/`password`/`product_id` 到 client 内部；
- `send` / `now_ms` / `on_event` / `user` 只保存指针/值，不复制指向的数据；
- `tx_cap >= 256`、`rx_cap >= 256`；推荐值见快速开始；
- 成功后 `state=IDLE`，不会自动连接。

### `int aiot_client_connected(aiot_client_t *client)`

- TCP：置 `WAIT_LOGIN`，立即发送 `lgn`；
- UDP：置 `ONLINE`；
- MQTT：置 `ONLINE`，并发布一次 `hear`（除非 `no_auto_heartbeat=1`）；
- 触发 `AIOT_EV_CONNECTED`。

### `int aiot_client_disconnected(aiot_client_t *client)`

- 置 `IDLE`，清空 RX 行缓存和构造状态；
- 触发 `AIOT_EV_DISCONNECTED`。

### `int aiot_client_rx(...)`

```c
int aiot_client_rx(aiot_client_t *client, const aiot_u8 *data, size_t len);
```

TCP 流入口。可一次喂任意长度；SDK 按 `\n` 拆帧，自动处理半包/粘包。返回解析/溢出错误；单个 JSON 解析失败不会断开连接。

### `int aiot_client_rx_datagram(...)`

UDP/MQTT 数据报入口。每次一个完整 JSON，不需要 `\n`。

### `int aiot_client_poll(...)`

```c
int aiot_client_poll(aiot_client_t *client, aiot_u32 now_ms);
```

主循环周期调用：

- WAIT_LOGIN：10 秒未收到 lgn → `AIOT_EV_TIMEOUT`，返回 `AIOT_ERR_TIMEOUT`；
- ONLINE：按 `heartbeat_ms` 发 `hear`；
- TCP：`keepalive_sec × 2` 无 RX → 超时；
- MQTT：不做 SDK 层链路超时（由 MQTT 客户端负责）。

### 查询

```c
aiot_state_t aiot_client_state(const aiot_client_t *client);
aiot_u32 aiot_client_last_rx_ms(const aiot_client_t *client);
```

---

## 4. 上行

### `aiot_report`

```c
int aiot_report(aiot_client_t *client, const aiot_kv_t *kvs, size_t count,
                const char *fid);
```

- `count` > 0；`fid` 可为 NULL（自动 `F1/F2/...`）；
- TCP/MQTT 生成 `facs`；UDP 生成 `lgn_facs`（自动带密码+设备 ID）；
- 要求 `state=ONLINE`。

### `aiot_report_begin/add/end`

```c
int aiot_report_begin(aiot_client_t *client, const char *fid);
int aiot_report_add(aiot_client_t *client, const char *key, const char *value);
int aiot_report_end(aiot_client_t *client);
```

- 构造期间 `client->builder=1`，不能调用其它发送 API；
- 出错或放弃时调用 `aiot_build_abort()`；
- `begin` 的 `fid` 会被保存到 `pending_fid`，`end` 使用它。

### `aiot_backfill_*`

```c
int aiot_backfill_begin(aiot_client_t *client, aiot_u32 timestamp, const char *fid);
int aiot_backfill_add(aiot_client_t *client, const char *key, const char *value);
int aiot_backfill_timestamp(aiot_client_t *client, aiot_u32 timestamp);
int aiot_backfill_end(aiot_client_t *client);
```

- 仅 TCP/MQTT；UDP 返回 `AIOT_ERR_UNSUPPORTED`；
- `timestamp` 是 Unix 秒；
- 单帧 ≤ 1000 个点；
- `timestamp()` 开始下一组；调用前当前组至少要有 1 个点；
- 超出缓冲返回 `AIOT_ERR_OVERFLOW` 并复位构造。

### `aiot_heartbeat`

```c
int aiot_heartbeat(aiot_client_t *client);
```

发送 `hear`。`poll` 已自动发送；手动调用用于特殊节奏。

### `aiot_request_time`

```c
int aiot_request_time(aiot_client_t *client, const char *fid);
```

发送 `get_time ["1"]`；结果在 `AIOT_EV_RESULT`（`func="get_time"`）中。`result_text` 可能是格式化时间字符串（实测）或数字（文档）。

### `aiot_request_order`

```c
int aiot_request_order(aiot_client_t *client, const char *ack);
```

UDP 拉取一条挂起指令；`ack` 可为 NULL。结果 `result_json` 为 `{"cmd":...,"args":...,"tra":...}` 或 `null`。

### `aiot_ota_info` / `aiot_ota_get`

```c
int aiot_ota_info(aiot_client_t *client, const char *firmware_id, const char *fid);
int aiot_ota_get(aiot_client_t *client, const char *firmware_id,
                 aiot_u32 block_no, const char *fid);
```

- `gfinfo` 结果：`{"fmid","name","ver","size","total","bytes","fill","encry","check","tpro","time"}`
- `gfcet` 结果：`{"fmid","no","pro","data"}`，`data` 为 hex 字符串
- 结果通过 `AIOT_EV_RESULT` 的 `result_json` 给出。

### `aiot_udp_wakeup`

```c
int aiot_udp_wakeup(aiot_client_t *client, const aiot_kv_t *kvs, size_t count,
                    const char *ack);
```

仅 UDP；生成 `lgn_facs`，带 `ack`。`count` 可以为 0（纯唤醒）。

### `aiot_send_func`

```c
int aiot_send_func(aiot_client_t *client, const char *func,
                   const char *args_json, const char *fid);
```

发送任意 `func`。`args_json` 必须形如 `["x",1]`（SDK 只检查首尾括号，不校验内部）。用于平台新增功能。

### `aiot_build_abort`

```c
int aiot_build_abort(aiot_client_t *client);
```

放弃 `report_begin`/`backfill_begin` 构造，清空 TX 状态。

---

## 5. 下行回执

### `aiot_order_confirm`

```c
int aiot_order_confirm(aiot_client_t *client, const char *tra);
```

发送 `order_conf`。默认 `no_auto_order_conf=0` 时 SDK 已自动调用；只有关闭自动确认后才需要手动调用。

### `aiot_order_reply`

```c
int aiot_order_reply(aiot_client_t *client, const char *tra,
                     const aiot_kv_t *kvs, size_t count);
```

发送 `facs_reply`，参数为 `[tra, device_id, k0,v0, ...]`。`count` 可以为 0（仅回执）。

---

## 6. MQTT 辅助

### `aiot_mqtt_topic_up` / `down_order` / `down_result`

```c
int aiot_mqtt_topic_up(const aiot_client_t *client, char *buf, size_t cap);
int aiot_mqtt_topic_down_order(const aiot_client_t *client, char *buf, size_t cap);
int aiot_mqtt_topic_down_result(const aiot_client_t *client, char *buf, size_t cap);
```

生成：

```text
south/{product}/{device}/up
south/{product}/{device}/down/order
south/{product}/{device}/down/result
```

缓冲区不足返回 `AIOT_ERR_NOMEM`。

### `aiot_mqtt_rx`

```c
int aiot_mqtt_rx(aiot_client_t *client, const aiot_u8 *payload, size_t len);
```

收到 `down/order` 或 `down/result` 的 payload 后调用。不需要 `\n`；内部复用 UDP 数据报解析路径。

---

## 7. 工具

```c
const char *aiot_version(void);
const char *aiot_strerror(int err);
const char *aiot_state_name(aiot_state_t state);
```

### 下行参数解析

```c
int aiot_args_count(const char *args_json, size_t len);
int aiot_args_get_str(const char *args_json, size_t len, int index,
                      char *out, size_t cap);
int aiot_args_get_u32(const char *args_json, size_t len, int index,
                      aiot_u32 *out);
```

用于解析 `AIOT_EV_ORDER` 的 `args_json`，例如：

```c
/* 下行 set: args = ["DEV","sw","1"] */
char key[32], value[32];
if (aiot_args_get_str(ev->args_json, ev->args_len, 1, key, sizeof key) >= 0 &&
    aiot_args_get_str(ev->args_json, ev->args_len, 2, value, sizeof value) >= 0) {
    /* key="sw", value="1" */
}
```

`args_get_str` 对字符串返回解码后的文本，对数字/布尔/null 返回原始 JSON 文本；失败返回负值。

---

## 8. 线程安全与重入

- SDK **不是线程安全的**；
- `send` 回调可能在 `report`/`poll`/`rx` 内部被调用；
- 不要在 `on_event` 里递归调用 `aiot_client_rx`；
- 如果多任务共享 client，用自己的互斥锁包住所有 `aiot_*` 调用；
- `on_event` 中的 `args_json`/`result_json` 只在回调期间有效。

---

## 9. 内存所有权

| 对象 | 所有权 |
|---|---|
| `tx_buf` / `rx_buf` | 调用方；生命周期必须覆盖 client |
| `cfg.device_id/password/product_id` | SDK 复制到 client 内部 |
| `cfg.user` | 调用方；SDK 只透传 |
| `aiot_kv_t` 的 key/value | 调用方；调用期间有效即可 |
| 事件中的字符串 | SDK 内部；仅回调期间有效 |
| `aiot_mqtt_t` 的 tx/rx | 结构体内嵌，调用方分配结构体 |

