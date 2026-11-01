# Open API · 行情（快照、分时、K 线）

> 根地址、`API_BASE`、统一响应与鉴权见 [api.md](./api.md)。

> ## ⚠️ 这几个接口**不是用来盯盘的**
>
> 它们给的是**当下这一次**的行情，用于分析、报价、算触发价。
> **禁止**为了等一个价格而循环 / 定时 / sleep 后重查——不管是「每 30 秒查一次快照」还是
> 「反复拉 K 线看有没有破位」，都不行。
>
> 用户要的「到价再买/再平」，正确做法是去 [api-cloud-orders.md](./api-cloud-orders.md)
> 建**条件单**或**持仓止盈止损**：条件由服务端 cloud-ctp 7×24 盯着，会话关掉也照样生效。

### 12. 单合约行情快照

```
GET /open/v1/market/snapshot?instrumentId=au2606
Headers: Authorization: Bearer ${API_KEY}
         X-Trading-Env: sim|live

Query（二选一，优先 instrumentId）：
  instrumentId   合约代码，如 au2606
  contractCode   合约代码别名（兼容旧调用）
```

**响应 `data`：**

```json
{
  "instrumentId": "au2606",
  "exchangeId": "SHFE",
  "instrumentName": "沪金2606",
  "volumeMultiple": 1000,
  "priceTick": "0.02",
  "lastPrice": "790.50",
  "openPrice": "789.80",
  "highestPrice": "792.00",
  "lowestPrice": "788.60",
  "bidPrice1": "790.48",
  "bidVolume1": "3",
  "askPrice1": "790.50",
  "askVolume1": "5",
  "preSettlementPrice": "788.00",
  "settlementPrice": "790.20",
  "tradingDay": "20260327",
  "updateTime": "2026-03-27 10:15:30"
}
```

> 该接口只读 Redis 缓存，不回源 DB/CTP；缓存缺失时字段为 `null`——**`null` 表示这一刻没缓存，不代表合约停牌或不存在**。
>
> ⚠️ **上面这些就是全部字段**：没有涨停价/跌停价，也没有成交量与持仓量。要涨跌停幅度请查
> `GET /open/v1/catalog/contract` 的 `priceLimit`。缺什么就说缺什么，**不要编一个数字出来**。
>
> ⚠️ **除 `volumeMultiple` 是整数外，价格与量都是字符串**（`"790.50"`），做算术前先转数字，
> 直接相加会变成字符串拼接。`priceTick` 可能为 `null`（取决于 Redis 里缓存的是哪种合约对象）。

---

### 13. 批量行情快照

```
GET /open/v1/market/snapshots?instrumentIds=au2606,ag2612,cu2506
Headers: Authorization: Bearer ${API_KEY}
         X-Trading-Env: sim|live
```

`instrumentIds`：逗号分隔，如 `au2606,ag2612,cu2506`，最多建议 20 个。

响应 `data` 为数组，每个元素结构与单合约快照完全相同（见第 12 节）。数组顺序与请求中 `instrumentIds` 顺序一致。

---

### 14. 分时图

```
GET /open/v1/market/tick?exchangeId=SHFE&instrumentId=au2606
Headers: Authorization: Bearer ${API_KEY}
         X-Trading-Env: sim|live
```

| Query 参数 | 必填 | 说明 |
|-----------|------|------|
| `exchangeId` | 否 | 交易所代码，如 `SHFE`、`DCE`、`CZCE`、`INE`、`CFFEX`、`GFEX`。**不确定就别传**——服务端会按合约代码自动解析；猜错交易所只会拿到空数据，而空数据很容易被误读成「这个合约没有行情」。要确认交易所用 `GET /open/v1/catalog/contract` |
| `instrumentId` | 否 | 合约代码，如 `au2606`。与 `contractCode` 二选一，优先 `instrumentId` |
| `contractCode` | 否 | `instrumentId` 的别名，两者等价 |

**响应 `data`：**

```json
{
  "startTime": "09:00:00",
  "endTime": "15:00:00",
  "closeTime": "15:00:00",
  "totalVolume": "58000",
  "reqTime": 1743040800,
  "ticks": [
    { "t": "1743040800000", "p": "790.50", "v": "120", "i": "121000", "a": "0" },
    { "t": "1743040860000", "p": "790.80", "v": "85",  "i": "121050", "a": "0" }
  ]
}
```

**`ticks` 数组每条字段（字段名均为单字母）：**

| 字段 | 类型 | 说明 |
|------|------|------|
| `t` | string | 时间戳，**毫秒、13 位字符串**（服务端把秒级时间直接拼了 `000`）。按秒解析会算出五万年后的日期——**要先除以 1000** |
| `p` | string | 价格 |
| `v` | string | 该分钟成交量 |
| `i` | string | 持仓量 |
| `a` | string | ⚠️ **本接口恒为 `"0"`**：服务端在分时路径上从未给它赋值。**不要当成交额用、也不要拿它算均价**，需要成交额只能自己用 `p × v` 估 |

> ⚠️ 外层 `reqTime` 是**秒**，数组里的 `t` 是**毫秒**——两者单位不同，不要混用。

| 外层字段 | 类型 | 说明 |
|---------|------|------|
| `startTime` | string | 交易开始时间，如 `09:00:00` |
| `endTime` | string | 交易结束时间，如 `15:00:00` |
| `closeTime` | string | 收盘时间 |
| `totalVolume` | string | 全日总成交量 |
| `reqTime` | number | 请求时间戳（秒） |

---

### 15. K 线图

```
GET /open/v1/market/kline?exchangeId=SHFE&instrumentId=au2606&type=6
Headers: Authorization: Bearer ${API_KEY}
         X-Trading-Env: sim|live
```

| Query 参数 | 必填 | 说明 |
|-----------|------|------|
| `exchangeId` | 否 | 交易所代码。**不确定就别传**，服务端按合约代码自动解析；猜错只会拿到空数据 |
| `instrumentId` | 否 | 合约代码。与 `contractCode` 二选一，优先 `instrumentId` |
| `contractCode` | 否 | `instrumentId` 的别名，两者等价 |
| `type` | 否 | K 线周期（见下表）。**不传默认 `10`（1 分钟）**；只接受下表这 8 个值，**没有月线、也没有 `1` 或 `8`**，传别的数字拿不到数据 |

**K 线周期 `type` 枚举：**

| type 值 | 说明 |
|---------|------|
| `10` | 1 分钟 |
| `2` | 5 分钟 |
| `3` | 15 分钟 |
| `4` | 30 分钟 |
| `9` | 4 小时 |
| `5` | 1 小时 |
| `6` | 日线 |
| `7` | 周线 |

**响应 `data`：**

```json
{
  "totalVolume": "320000",
  "reqTime": 1743040800,
  "chats": [
    {
      "t": "2026-03-20",
      "o": "788.00",
      "h": "795.00",
      "l": "786.50",
      "c": "792.00",
      "v": "45000",
      "a": "0",
      "u": 1742428800,
      "i": "118000",
      "s": "791.50"
    },
    {
      "t": "2026-03-21",
      "o": "792.00",
      "h": "798.00",
      "l": "790.00",
      "c": "796.00",
      "v": "52000",
      "a": "0",
      "u": 1742515200,
      "i": "120000",
      "s": "795.00"
    }
  ]
}
```

**`chats` 数组每条字段（字段名均为单字母）：**

| 字段 | 类型 | 说明 |
|------|------|------|
| `t` | string | 时间标签（分钟线格式 `MM-dd HH:mm`；日线格式 `yyyy-MM-dd`） |
| `o` | string | 开盘价 |
| `h` | string | 最高价 |
| `l` | string | 最低价 |
| `c` | string | 收盘价 |
| `v` | string | 成交量 |
| `a` | string | ⚠️ **恒为 `"0"`**：服务端在 K 线路径上从未给它赋值。**不要当成交额用**，需要成交额只能自己用价格 × 成交量估 |
| `u` | number | 时间戳，**秒**（与 `t` 表示同一时刻，`t` 是给人看的格式化字符串，排序/计算用 `u`） |
| `i` | string | 持仓量 |
| `s` | string | 结算价，**只有 `type=6`（日线）才赋值**；日线无结算价时为 `""`，其余周期（含周线 `type=7`）该字段**根本不存在 / 为 `null`**，不要当成 0 |

| 外层字段 | 类型 | 说明 |
|---------|------|------|
| `totalVolume` | string | 最新一根 K 线对应的全日总成交量 |
| `reqTime` | number | 请求时间戳（秒） |

---
