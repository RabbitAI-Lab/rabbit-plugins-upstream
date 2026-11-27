# 07 · OTA 与故障排查

---

## 1. OTA 两种模式

平台支持两种固件下发方式：

1. **设备主动拉取**：`gfinfo` 查元信息 → `gfcet` 逐包下载；
2. **平台主动推送**：下行 `upfs` 分片。

设备端至少要支持一种。建议：

- 网络稳定、可长连接：主动拉取，逻辑简单、可控；
- 低功耗/弱网：平台推送 + `order_conf`，设备按包写 flash。

---

## 2. 主动拉取流程

```text
设备                         平台
  │  gfinfo(fw_id)             │
  │───────────────────────────>│
  │<───────────────────────────│ {ver,size,total,bytes,tpro,...}
  │  gfcet(fw_id, 1)           │
  │───────────────────────────>│
  │<───────────────────────────│ {no:1,pro:"0144",data:"A8FF..."}
  │  ...                       │
  │  gfcet(fw_id, total)       │
  │<───────────────────────────│
  │  校验整包 CRC16-MODBUS     │
  │  写 flash / 切换分区       │
```

### 2.1 解析 `gfinfo`

`AIOT_EV_RESULT`：

```c
if (strcmp(ev->func, "gfinfo") == 0 && ev->code == 0) {
    /* ev->result_json 指向 {"fmid":...,"ver":...,"size":512,...} */
    /* 用你自己的 JSON 解析器/固定字段查找提取 */
}
```

SDK 不解析 OTA 元信息，因为不同项目用的 flash/分区/校验库不同；`result_json` 原样给出。

### 2.2 解析 `gfcet`

```json
{"fmid":"fw_1a2b3c","no":1,"pro":"0144","data":"A8FF3C..."}
```

- `data` 是**大写 hex 字符串**，长度 = `size × 2`
- `pro` 是本包 CRC16-MODBUS
- `no` 从 1 开始，最大 `total`

设备侧：

```c
/* 伪代码 */
int hex_to_bin(const char *hex, aiot_u8 *out, size_t out_cap);
aiot_u16 crc16_modbus(const aiot_u8 *data, size_t len);
```

### 2.3 CRC16-MODBUS

```c
aiot_u16 crc16_modbus(const aiot_u8 *data, size_t len)
{
    aiot_u16 crc = 0xFFFF;
    size_t i;
    int b;
    for (i = 0; i < len; i++) {
        crc ^= data[i];
        for (b = 0; b < 8; b++) {
            if (crc & 1) crc = (aiot_u16)((crc >> 1) ^ 0xA001);
            else         crc >>= 1;
        }
    }
    return crc;
}
```

整包校验用 `gfinfo.tpro`；单包用 `gfcet.pro`。

### 2.4 写入策略

- 先写备份区/下载区，整包校验通过后再切换启动分区；
- 每包写前擦除对应扇区，注意 flash 对齐；
- 记录 `next_block` 到备份寄存器/EEPROM，断电可续传；
- 下载完成后校验 `bytes`、`tpro`，再重启；
- 重启前回 `facs_reply` 报告新版本，例如 `{"ver","V12-261023"}`。

---

## 3. 平台推送 `upfs`

```json
{"top":"order","ter":"DEV","data":[
  {"cmd":"upfs","args":["0","4","512","A8FF3C..."],"tra":"fw000001"}
]}
```

- `args[0]` 包序号（从 0 开始，注意和 `gfcet` 的 1 起始不同）
- `args[1]` 总包数
- `args[2]` 单包字节数
- `args[3]` hex 数据

处理：

```c
if (strcmp(ev->cmd, "upfs") == 0) {
    /* 解析 args_json，写 flash */
    /* 默认 SDK 已 auto order_conf；写完可再 facs_reply */
}
```

`upfs` 的 `args_json` 可能 1–2 KB；确保 `g_rx` ≥ 4096，否则会 `AIOT_ERR_OVERFLOW`。

---

## 4. OTA 期间的连接

- OTA 下载可能持续几分钟；TCP 长连接要保持心跳（SDK 自动 `hear`）；
- 每包之间让出主循环，喂看门狗；
- 如果平台 30–60 秒收不到任何包，可能断开；建议每包后调用 `aiot_client_poll()`；
- 下载失败不要反复整包重来；记录 `next_block` 续传。

---

## 5. 故障排查

### 5.1 连接不上

| 检查 | 说明 |
|---|---|
| 域名/端口 | 测试 `ciot.yzlkj.com`，生产 `siot.yzlkj.com`；TCP 41032 |
| DNS | 模组是否支持 DNS；可先用 IP 测试 |
| 设备环境 | 平台设备记录是 `test` 还是 `prod` |
| 防火墙 | 41032/40501/1883 出站是否放行 |
| TCP 连接 | `AT+CIPSTART` 返回 `CONNECT`/`CONNECT OK` 才算成功 |

### 5.2 登录失败

| code | 处理 |
|---:|---|
| 3 | 密码错误；检查设备详情页“认证密钥”，不要用型号默认密码想当然 |
| 4 | 未登录就发业务；等 `AIOT_EV_LOGIN code=0` 再发 |
| 2 | 设备不存在；检查设备 ID、环境 |
| 9 | 未知函数；检查 `func` 拼写 |

### 5.3 一直离线

- 只建立 TCP 连接、不发 `lgn`：平台不会认为在线；
- 登录后不发数据/心跳：超过 `keepalive_sec` 会离线；
- 心跳周期 >= `keepalive_sec`：把 `heartbeat_sec` 设为 60；
- 设备在测试环境，页面看的是生产环境：确认顶部环境切换。

### 5.4 收不到下行

- 设备必须在线（TCP 已 lgn / MQTT 已订阅）；
- 平台指令 `channel` 必须是 TCP/MQTT/UDP，和设备协议一致；
- TCP 下行是 `{"top":"order"...}`，不是 `result`；
- MQTT 必须订阅 `down/order`，QoS1；
- UDP 设备要主动 `get_order`，平台不会主动推。

### 5.5 数据不显示/值不对

- 测点键必须在型号设施定义内；`autoAddMetrics=0` 时未定义键被丢弃；
- `dataType` 不匹配：decimal 传 `"abc"` 可能被平台存成文本/异常；
- `facs_his` 时间戳不是数字 → `code=1`；
- 平台按收到时间入库；设备本地时间不准时先 `get_time` 校时。

### 5.6 缓冲区溢出

- `AIOT_ERR_OVERFLOW`：TX 太小或单帧太大；
- RX 溢出：单行超过 `rx_cap`，常见于 `upfs`/`gfcet` 大分片；
- 处理：增大 `g_tx`/`g_rx`，或分批上报；OTA 场景 RX 至少 4096。

### 5.7 MQTT 连不上

- 匿名必失败；
- clientId/username 都必须是设备 ID；
- password 必须是设备密码，不是用户账号密码；
- 1883 明文；平台没有 8883 TLS；
- 订阅 topic 的 `{product}` 必须是型号 ID，不是设备名。

### 5.8 解析错误

- TCP 数据必须带 `\n` 才能触发拆帧；
- 如果模组把一帧拆成多段，直接多次 `aiot_client_rx()`，不要自己拼接后再加 `\n`；
- 如果平台返回 `"result":"..."` 字符串，`ev->result_text` 是解码后的文本；对象结果看 `result_json`；
- `AIOT_JSON_MAX_TOKENS=64` 时，超大 `order` 可能解析失败；OTA 用 128。

---

## 6. 日志建议

在 `send` 和 `rx` 处加**可控**日志：

```c
#define AIOT_DEBUG 1
#if AIOT_DEBUG
#define LOGF(...) printf(__VA_ARGS__)
#else
#define LOGF(...) do {} while (0)
#endif
```

不要在生产固件里永久打开完整 JSON 打印：串口阻塞会拖慢 TCP，且可能泄露设备密码（`lgn` 帧包含密码）。

建议日志字段：

```text
[aiot] tx len=... func=lgn fid=L1
[aiot] rx len=... top=result func=lgn code=0
[aiot] order cmd=set tra=... 
[aiot] state=online
```

如果需要打印帧，过滤掉 `lgn` 的 `args`。

---

## 7. 单元测试与回归

```bash
cc -std=c89 -Iinclude -Isrc tests/test_all.c src/aiot.c src/aiot_json.c -o test_all
./test_all
```

输出：

```text
183 checks, 0 failures
```

新增功能时建议在 `tests/test_all.c` 增加：

- 新帧的构造断言（字段、转义、换行）；
- 新回执的解析断言；
- 边界：空值、超长、非法 JSON、缓冲区溢出。

---

## 8. 版本升级注意

- 平台字段可能变化；升级前先用测试设备跑 `host_tcp_demo`；
- 不要改 `AIOT_EV_*` 枚举值（会影响已有业务）；
- `aiot_event_t` 新增字段时放在末尾，保持 ABI 兼容；
- 修改 `aiot_client_t` 布局需要重新编译所有使用方。



