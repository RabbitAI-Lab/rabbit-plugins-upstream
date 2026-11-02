# Open API · 商品期货持仓龙虎榜

> 根地址、`API_BASE`、统一响应与鉴权见 [api.md](./api.md)。

> ## ⚠️ 这是**交易所公布的会员持仓**，不是用户本人的持仓
>
> 本组数据来自交易所每日公布的期货公司会员持买/持卖仓量排名（俗称"龙虎榜"），反映的是**市场上各家期货公司客户的整体多空分布**。
> **用户自己的持仓请走 `GET /open/v1/positions`。** 把龙虎榜说成"你的持仓"是严重误导，务必分清。
>
> 与交易环境无关：`sim` / `live` 返回同一份市场数据。

## 0. 调用顺序（照做，能省掉大半无效请求）

1. `GET /open/v1/holding/meta/dates` 取**最新可用交易日** → 拿到 `tradeDate`；
2. 用该 `tradeDate` 调 `/holding/snapshot`。

> **不要直接拿"今天"的日期去查。** 龙虎榜由交易所**收盘后**公布，盘中当天没有数据；遇上非交易日、节假日更是空的。
> 直接用当天日期查到空结果，然后得出"这个品种没人持仓"的结论——这是最常见也最离谱的误读。
> 数据是否已更新到最近交易日，可另调 `/holding/meta/update-time` 确认。

## 1. 筛选项

### 1.1 可选交易日

```
GET /open/v1/holding/meta/dates?symbol=&exchange=&product=
```

传 `symbol`（合约代码，如 `rb2601`）**或** `exchange`+`product`（如 `SHFE` + `rb`）。返回倒序的交易日列表。

### 1.2 可选合约

```
GET /open/v1/holding/meta/contracts?exchange=SHFE&product=rb
```

`exchange`、`product` 均必填。

### 1.3 可选期货公司会员

```
GET /open/v1/holding/meta/brokers?symbol=&exchange=&product=&tradeDate=
```

### 1.4 数据最新交易日

```
GET /open/v1/holding/meta/update-time?symbol=&exchange=&product=
```

响应 `data.updateTime` 为该维度下的最大交易日。

**以上四个接口的筛选项元素结构：**

| 字段 | 说明 |
|------|------|
| `value` | 传给后续接口的值 |
| `name` / `displayName` | 展示名 |

## 2. 快照（头部指标 + 多空占比 + 会员排行）

```
GET /open/v1/holding/snapshot?tradeDate=2026-08-29&symbol=rb2601
GET /open/v1/holding/snapshot?tradeDate=2026-08-29&exchange=SHFE&product=rb&summary=true
```

| 参数 | 必填 | 说明 |
|------|------|------|
| `tradeDate` | **是** | 交易日 `yyyy-MM-dd`，必须是已公布的交易日（先用 1.1 取） |
| `symbol` | 视情况 | 单合约查询时传 |
| `exchange` / `product` | 视情况 | `summary=true` 时用它们定位品种 |
| `summary` | 否 | `false`（默认）= 单合约；`true` = 品种下全部合约汇总 |

**响应 `data`：**

| 字段 | 类型 | 说明 |
|------|------|------|
| `contractName` | string | 合约 / 品种展示名 |
| `dateLabel` | string | 数据日期标签 |
| `header.longCount` | number | 会员**持买**仓量合计 |
| `header.shortCount` | number | 会员**持卖**仓量合计 |
| `header.ratio` | string | 多空比展示值 |
| `pieData` | object | 分组饼图数据，值为 `{name, percent, color}` 数组 |
| `rankingList[]` | array | 会员排行，见下 |

**`rankingList[]` 每条：**

| 字段 | 类型 | 说明 |
|------|------|------|
| `rank` | int | 名次 |
| `company` | string | 期货公司会员简称 |
| `volume` | number | 持仓量 |
| `change` | number | 较上一交易日的增减（**可为负**） |
| `trend` | string | 增减方向标记 |

## 3. 多空持仓趋势（双折线）

```
GET /open/v1/holding/position-trend?endDate=2026-08-29&symbol=rb2601
```

| 参数 | 必填 | 说明 |
|------|------|------|
| `endDate` | **是** | 截止日 `yyyy-MM-dd` |
| `symbol` | 视情况 | 单合约 |
| `exchange` / `product` | 视情况 | `summary=true` 时必填 `product` |
| `summary` | 否 | 是否品种汇总 |

**响应 `data`：** `categories`（日期数组）、`longSeries`（持买）、`shortSeries`（持卖），三者等长、按位对应。

> ⚠️ **窗口是近 90 个自然日，按自然日补全。** 非交易日与无数据日的值是 **`null`，不是 0**。
> 算变化率、求和、作图时必须跳过 `null`；把 `null` 当 0 会凭空造出一个"持仓归零"的暴跌。

## 4. 单个会员的持仓结构

```
GET /open/v1/holding/broker-summary?exchange=SHFE&product=rb&brokerPrefix=XX&tradeDate=2026-08-29
```

四个参数**全部必填**。把该品种下全部合约按会员前缀聚合，用来看某家期货公司在这个品种上整体偏多还是偏空。

**响应 `data.rows[]`：** `typeLabel`（分类展示名）、`volume`（持仓量）、`change`（增减）、`typeKey` / `typeIcon` / `changeClass`（展示用）。

## 5. 单个会员的成交量趋势

```
GET /open/v1/holding/broker-volume-trend?exchange=SHFE&product=rb&brokerPrefix=XX&endDate=2026-08-29&range=1m
```

`range` 可选 `1m` / `3m` / `6m`，默认 `1m`。响应 `data`：`chartTitle`、`categories`、`seriesData`、`timeRangeOptions`。

## 6. 解读约束（重要）

- **龙虎榜是滞后的公开数据**，反映的是上一个交易日收盘后的会员持仓，**不能**当作实时行情或未来走势的预测。
- **不要**把"某家会员持买增加"解读成"该公司看多"或"跟着它买就能赚"——会员持仓包含其全部客户的净头寸与套保盘，方向与盈亏之间没有必然联系。
- 不要用它给出买卖建议。可以陈述数据、描述多空分布变化，判断和决策留给用户。
- 会员简称是交易所口径，与期货公司全称不一定一致；**不要**据此评价任何一家期货公司的优劣。
