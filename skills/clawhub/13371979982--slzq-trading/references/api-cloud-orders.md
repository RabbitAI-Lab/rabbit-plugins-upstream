# Open API · 云条件单 / 止盈止损

> 根地址、`API_BASE`、统一响应与鉴权见 [api.md](./api.md)。

> ## ⚠️ 这组接口就是用来**代替智能体自己盯盘**的
>
> 只要用户的需求带**触发条件**——「跌到 X 就买」「涨到 Y 帮我平」「帮我盯着」「设个止损」——
> 就在这里建一张单，然后**这一轮结束**。条件由服务端 **cloud-ctp** 盯：它持有实盘 CTP 凭据，7×24 跑在服务器上，
> 满足条件自动报单。
>
> **禁止**用 `/market/snapshot`、`/market/kline`、`/positions` 循环轮询去等一个价格，禁止 sleep 后重查，
> 禁止写「每 N 秒查一次」的脚本或后台任务，禁止跟用户说「别关窗口我帮你盯着」。
> 会话一关、客户端一退、夜盘一开，你的循环就没了；期货逐笔跳动，秒级轮询本来也接不住——**漏掉的是用户的真钱**。

> ## ⚠️ 本组接口**仅在 `X-Trading-Env: live` 下可用**
>
> 这套托管机制**只对真实 CTP 账号存在**，模拟盘没有对应实现。
>
> `sim` 环境调用会明确报错并指回 **`POST /open/v1/orders`**（模拟盘直接下单）。**不要重试、不要换参数再试**，
> 那是环境能力差异，不是参数错了。也**不要**因为云单用不了就退回去轮询行情——如实告诉用户
> 「到价触发需要实盘（`X-Trading-Env: live`，密钥档位 `SIM_LIVE`），模拟盘只能立即下单」。

## 用户想干什么 → 用哪个接口

| 用户的话 | 用什么 | 关键参数 |
|---|---|---|
| 「现在买 2 手 rb2601」 | `POST /open/v1/orders` 直接报单 | — |
| 「跌到 3000 再买 2 手」（还没仓位，到价开仓） | **条件单** | `offsetFlag=0`、`triggerMode=le`、`triggerPrice=3000` |
| 「突破 3200 就追多」 | **条件单** | `offsetFlag=0`、`triggerMode=ge`、`triggerPrice=3200` |
| 「在 2980～3020 之间帮我建仓」 | **条件单** | `triggerMode=range`、`triggerPriceMin=2980`、`triggerPriceMax=3020` |
| 「这个多单跌破 2950 帮我砍了」 | **止盈止损** | `positionDirection=0`、`conditionType=2`、`triggerPrice=2950` |
| 「赚到 3300 就跑」 | **止盈止损** | `conditionType=3`、`triggerPrice=3300` |
| 「帮我盯着这个仓，回撤 2% 止损」 | 按开仓均价**算出触发价**再建**止盈止损** | 触发价算好一次性传进去 |
| 「明天开盘到价再说」「收盘了先挂上」 | **条件单**（任何时间可建） | `timeCondition=GTC` |

## 两者的区别（先分清再选接口）

| | **条件单** | **止盈止损** |
|---|---|---|
| 是什么 | 盯某个价格条件，满足即报单（可开仓也可平仓） | 对**已有持仓**设触发平仓条件 |
| 何时可创建 | 任何时间 | 任何时间 |
| 前置条件 | 无 | 必须已有对应持仓 |
| 接口 | `POST /open/v1/cloud/orders/condition` | `POST /open/v1/cloud/orders/stop-profit-loss` |
| 用户在 App 里看得见吗 | **看得见**（交易 → 条件单，可自己改自己撤） | 看得见（挂单 → 止损/止盈） |

**平仓类怎么选**（先看持仓：实盘 `todayPosition`/`ydPosition`，模拟盘上期所/能源看 `positionDateType`）：

- 大商所、郑商所、广期所不区分今昨，到价平仓用**止盈止损**即可。
- **整仓**到价平掉：用**止盈止损**。上期所、能源、中金所服务端拆成两张，平昨用普通平仓 `offsetFlag=1`，平今用 `offsetFlag=3`，和 App 一样。**不要传 `positionDateType`**（那是立即下单字段，止盈止损没有，传了会被忽略）。
- 用户**只要平今**：止盈止损可传 `offsetFlag=3`，或改用**条件单** `offsetFlag=3`。**只要平昨**：传 `1`，不必传 `4`。两边都有而用户没说清时先问。
- **平今只能当日有效**：`offsetFlag=3` 或上期所/能源/中金所只有今仓时，到期就是当天 15:00。用户要长期有效时先说明、等确认，再用 `GFD` 建单，不要传 `GTC`。

> **交易时间内要立刻成交，用 `POST /open/v1/orders`。** 云单是给「还没到条件」的需求用的，
> 当下就能报的单没必要绕服务端托管。

> ### 挂单（`orderCategory=1`）：**服务端当前未开放创建/修改**
>
> `POST /open/v1/cloud/orders/pending` 与 `/pending/modify` 在当前服务端**没有开放**，调用会失败——
> **不要重试、不要换域名**。收盘后想先把单子挂上，用**条件单**（`timeCondition=GTC`）达到同样效果。
>
> 查询与撤销仍然覆盖挂单：历史上建过的挂单可以用 `GET /open/v1/cloud/orders?orderCategory=1` 查、
> 用 `POST /open/v1/cloud/orders/cancel` 撤。

## 枚举速查

### 条件单专用（`/cloud/orders/condition*`）

| 字段 | 取值 |
|------|------|
| `direction` | `0`=买入，`1`=卖出。指这笔委托本身买还是卖，不是持仓方向 |
| `offsetFlag` | `0`=开仓，`1`=平仓（平昨传 `1`），`3`=平今，`4`=平昨（不必传）。上期所/能源/中金所平今必须 `3`，传 `1` 只平昨 |
| `triggerMode` | `ge`=涨到触发价才动手，`le`=跌到触发价才动手，`range`=落进 `[min,max]` 才动手 |
| `orderPriceType` | `MARKET` 市价 / `LIMIT` 限价（须给 `limitPrice`）/ `LAST` 最新价 / `OPPONENT` 对手价 / `QUEUE` 排队价。**仅条件单**；立即下单 `POST /open/v1/orders` 的市价是 `priceType=ANY`，不要把 `MARKET` 写过去 |
| `timeCondition` | `GFD`=当日有效（默认），`GTC`=撤销前长期有效。**平今（offsetFlag=3）不能传 GTC** |
| `status`（条件单列表/详情） | `0` 盯盘中 `1` 已触发 `2` 已暂停 `3` 已撤销 `4` 已失效 `5` 失败 |
| `tabType`（条件单列表筛选） | `OPEN`=开仓条件单，`CLOSE`=平仓条件单 |

> **触发价只看最新价**，没有买一价 / 卖一价可选。旧字段 `conditionType`、`triggerPriceType`
> 已经不用传了——`triggerPriceType=2/3` 会被明确拒绝，**不要改成别的值重试**。
>
> **两套 `status` 不要混**：上表是条件单的；下表 `GET /open/v1/cloud/orders` 用的是另一套。
> 念给用户时直接用返回里的 `statusLabel`，别按数字自己编文案。

### 挂单 / 止盈止损（`/cloud/orders`、`/cloud/orders/stop-profit-loss*`）

| 字段 | 取值 |
|------|------|
| `direction` | `0`=买入，`1`=卖出 |
| `positionDirection`（止盈止损） | `0`=买入持仓，`1`=卖出持仓 |
| `offsetFlag` | `0`=开仓，`1`=平仓（平昨传 `1`），`3`=平今，`4`=平昨（不必传）。止盈止损可选；整仓不传。**不要传 `positionDateType`** |
| `conditionType` | `1`=价格条件，`2`=止损，`3`=止盈 |
| `triggerPriceType` | `1`=最新价，`2`=买一价，`3`=卖一价 |
| `triggerOperator` | `1`=`≥`，`2`=`≤` |
| `orderPriceType` | `1`=市价，`2`=限价（限价必须给 `limitPrice`） |
| `stopPriceType` | `1`=对手价，`2`=最新价，`3`=超价，`4`=排队价，`5`=涨跌停价（默认） |
| `timeCondition` | `GFD`=当日有效，`GTC`=撤销前长期有效。**平今不能传 GTC** |
| `status` | `0`待触发 `1`已触发 `2`委托中 `3`已成交 `4`已撤销 `5`失败 `6`部分成交 |
| `orderCategory` | `0`=条件单，`1`=挂单，`2`=止盈止损 |

## 1. 查询

### 1.1 条件单：`GET /open/v1/cloud/orders/condition`

```
GET /open/v1/cloud/orders/condition?tabType=OPEN&startTime=&endTime=
```

返回**全部盯盘中的条件单**（不限创建日） ∪ 时间窗内创建的任意状态；不传时间窗时窗口就是当前交易日
（上一交易日 15:00 ～ 当前交易日 15:00）。**这份数据和用户在 App「交易 → 条件单」里看到的是同一份**，
所以可以直接跟用户对上号。响应 `data` 是数组，不是分页壳。

| 字段 | 说明 |
|------|------|
| `type` | `single`=一张单；`group`=同合约分组，**真正的单在 `orders[]` 里**，别把分组行当成一张单 |
| `id` | 条件单 id，修改 / 撤销 / 查详情都用它 |
| `instrumentName` / `productName` | 合约与品种中文名，直接念给用户 |
| `direction` / `offsetFlag` / `volume` | 方向 / 开平 / 手数 |
| `triggerPriceText` | 触发条件的中文描述，可直接念 |
| `status` / `statusLabel` | 状态码见上方条件单枚举表；**念用户听的一律用 `statusLabel`** |
| `orderPriceTypeDesc` / `limitPrice` | 触发后报单价格类型 / 限价 |
| `estimatedMargin` / `estimatedCommission` | 预估保证金 / 手续费 |
| `stopLossText` / `takeProfitText` | 附带的止损 / 止盈描述，没设就是 `null` |
| `expireTime` / `createTime` / `updateTime` | 有效期与时间 |

### 1.2 条件单详情：`GET /open/v1/cloud/orders/condition/detail`

```
GET /open/v1/cloud/orders/condition/detail?orderId=123
```

在列表字段之外还给 `conditions`（触发条件明细）与 `actions`（动作与状态变更历史）。
**排查「为什么没触发 / 为什么失败」先看 `actions`**，比反复查列表有效。

### 1.3 挂单 / 止盈止损：`GET /open/v1/cloud/orders`（分页）

```
GET /open/v1/cloud/orders?orderCategory=1&status=0&instrumentId=&pageNum=1&pageSize=20
```

四个筛选项都可省略。响应 `data` 为统一分页形状（`list` / `currentPage` / `pageSize` / `totalCount` / `totalPage`）。

> **条件单不要用这个接口查**：它是旧口径，`status` 是另一套码，字段也和用户在 App 里看到的对不上。
> 查条件单用 1.1。

`list[]` 每条关键字段：

| 字段 | 说明 |
|------|------|
| `id` | **orderId**，修改与撤销都用它 |
| `instrumentId` / `instrumentName` / `productName` / `exchangeId` | 合约与品种 |
| `direction` / `offsetFlag` / `volume` | 方向 / 开平 / 手数 |
| `orderCategory` / `status` | 类别 / 状态（见上表） |
| `conditionType` / `triggerPriceType` / `triggerOperator` / `triggerPrice` | 触发条件 |
| `orderPriceType` / `limitPrice` / `stopPriceType` / `orderPrice` | 报单价格设置 |
| `timeCondition` / `expireTime` | 有效期 |
| `triggerTime` / `orderRef` / `orderSysId` | 触发时间与报单引用（已触发时有值） |
| `errorMsg` | 失败原因（`status=5` 时看这里） |
| `estimatedMargin` / `estimatedCommission` | 预估保证金 / 手续费 |
| `openAvgPrice` / `estimatedProfitLoss` | 开仓均价 / 预估盈亏（止盈止损、平仓类才有） |
| `retryCount` / `maxRetry` | 重试次数 |
| `createTime` / `updateTime` / `remark` | 时间与备注 |

## 2. 动作历史

```
GET /open/v1/cloud/orders/actions?orderId=123
```

返回该单的操作日志与状态变更：`action`、`statusBefore` → `statusAfter`、`triggerPrice`、`errorMsg`、`source`、`operator`、`createTime`。
**排查"为什么没触发/为什么失败"先看这里**，比反复查列表有效。

## 3. 创建挂单 —— **服务端当前未开放，别调**

`POST /open/v1/cloud/orders/pending` 当前没有开放，调用必失败。收盘后想先把单子挂上，
改用**条件单**（第 5 节，`timeCondition=GTC`），效果等价。

## 4. 创建止盈止损

```
POST /open/v1/cloud/orders/stop-profit-loss

{
  "instrumentId": "rb2601",
  "exchangeId": "SHFE",
  "positionDirection": 0,
  "volume": 3,
  "conditionType": 2,
  "triggerPrice": 3020,
  "stopPriceType": 5,
  "timeCondition": "GFD"
}
```

服务端会**查 CTP 实际持仓**校验合约、持仓方向与数量——报"持仓不足"就是真的不足，不要改大数量重试。

**不要传 `positionDateType`。** 那是 `POST /open/v1/orders` 立即下单的字段，本接口没有，传 `"今"` / `"昨"` 会被丢掉。要指定今/昨，传可选 `offsetFlag`：今=`3`，昨=`1`（不必传 `4`）。整仓止盈止损不要传 `offsetFlag`，由服务端按持仓拆。

`exchangeId` **可不传**，服务端按合约代码补齐。上期所 / 能源 / 中金所拆今昨仓依赖这个值。**补不上会拒绝下单**，向用户确认合约代码，不要猜交易所。

## 5. 创建条件单

**这条链路和用户在 App 里自己下单是同一条**——建出来的单他能在 App「交易 → 条件单」里看到、
自己改自己撤。（历史上这个接口走的是另一条旧链路：单子照样盯盘触发成交，但 App 列表里根本不显示，
用户只能干等它触发。已经换掉了。）

```
POST /open/v1/cloud/orders/condition

{
  "instrumentId": "rb2601",
  "direction": 0,
  "offsetFlag": 0,
  "volume": 1,
  "triggerMode": "le",
  "triggerPrice": 3000,
  "orderPriceType": "MARKET",
  "timeCondition": "GTC"
}
```

- `exchangeId` **不用传**，服务端按合约代码解析；**补不上会拒绝**，向用户确认合约代码，不要猜交易所。
- `triggerMode=range` 时改传 `triggerPriceMin` / `triggerPriceMax`，不要传 `triggerPrice`。
- `orderPriceType=LIMIT` 时必须同时给 `limitPrice`，其余类型不要传 `limitPrice`。
- 可选 `stopLossConfig` / `takeProfitConfig`：这张单**触发成交之后**自动再挂的止损 / 止盈，
  形如 `{"spread": 50, "orderPriceType": "市价"}`（`spread` 是相对成交价的价差）。用户没主动提就不要传。

**旧字段没了**：`conditionType`、`triggerPriceType` 不用再传。触发价只看最新价，
传 `triggerPriceType=2`（买一价）或 `3`（卖一价）会被明确拒绝——那是 V2 给不了的条件，
**不要换个值重试**，如实告诉用户只能按最新价触发。

## 6. 修改

```
POST /open/v1/cloud/orders/stop-profit-loss/modify    { "orderId": 1, "triggerPrice": 3030, "volume": 2, ... }
POST /open/v1/cloud/orders/condition/modify           { "id": 1, "triggerMode": "le", "triggerPrice": 3005 }
```

止盈止损用 `orderId`，条件单用 `id`（老字段名 `orderId` 也收，但别两个都传）。只传要改的字段，
没传的保持不变。

**条件单的触发条件是整体重建的**：要改触发价，就把 `triggerMode` 和触发价一起传，只传价格不带模式会被拒。
**只有盯盘中 / 已暂停的条件单能改**——报「状态不允许」就是已经触发 / 撤销 / 失效了，
**不要换参数重试**，要换条件就撤了重建。

**类别不能改**——条件单不能改成止盈止损，要换类别就撤了重建。
（`/pending/modify` 与创建挂单一样，服务端当前未开放。）

## 7. 撤销（通用）

```
POST /open/v1/cloud/orders/cancel?orderId=123
```

条件单、挂单、止盈止损都用这一个接口，服务端按单子自己的类型走对应的撤销链路，**不用先判断是哪一类**。

## 8. 建完之后就收手

1. 把返回的 `id`（= `orderId`）告诉用户，并说明**条件由服务端盯着**，关掉会话、退出客户端都照样生效；
2. 用户问进展时**才**查 `GET /open/v1/cloud/orders/condition`（条件单）
   或 `GET /open/v1/cloud/orders/condition/detail?orderId=` 看动作历史；
3. **不要**建完单还定时回来查有没有触发——那等于换个接口继续盯盘，同样禁止。

## 9. 硬性约束

- **不许自己盯盘。** 不得用行情 / 持仓接口循环、定时、sleep 后重查来等一个触发价，不得写「每 N 秒查一次」的
  脚本或后台任务，不得跟用户说「别关窗口我帮你盯着」。到价才交易的需求一律建云单。
- **请求体里的 `account` / `company` / `sessionId` 会被服务端按 Api-Key 覆盖**，传了不作数，也不要试图用它们操作别的账号。
- **创建、修改、撤销都要有用户的明确指令。** 这些接口动的是实盘真钱，不允许 Agent 自行推断"应该止损了"就下手。
  下单前把合约、方向、手数、触发价、有效期复述给用户确认。
- 报错先读 `errorInfo`，条件单再看 `/cloud/orders/condition/detail` 的 `actions`、
  挂单/止盈止损看 `/cloud/orders/actions`，**不要**换参数盲试——涨跌停校验、
  持仓校验都是硬规则，重试不会变。
- `GTC`（长期有效）的单子会一直挂着直到触发或撤销。替用户创建 `GTC` 单时要说明这一点。**平今仓不能设 GTC**：先说明只能当日有效，等用户确认后再用 `GFD` 建。
