# 指数 V2 接口字段权威参考

本文中的路径均为 JSON 路径，`$` 表示响应根节点。字段缺失、空值或结构异常时先检查真实响应，不把 ETF 或场外基金字段套到指数对象。

## 公共约定

- 认证和来源请求头由 `scripts/api_client.py` 与 `config.py` 处理。
- 指数代码通常使用6位交易代码；带后缀代码读取 `sinfoWindcode` / `sInfoWindcode`。
- 批量结果逐项检查 `availabilityStatus`。
- 指数点位不是基金净值，指数成分股不是某只基金的实际持仓，指数收益也不是跟踪基金的实际收益。

## 能力与数据路径速查

| 接口 | 结果路径 | 主要用途 |
|---|---|---|
| `POST /skill/v2/search/chinaIndex` | `$.data.data[]` | 中国指数关键词与复杂条件筛选 |
| `POST /skill/v2/search/index-by-stock` | `$.data.list[]` | 按成分股反查指数 |
| `POST /skill/v2/index/detail` | `$.data[] → detail` | 指数完整画像 |
| `POST /skill/v2/index/holdings` | `$.data[] → holdingItems[]` | 前十大成分股 |
| `POST /skill/v2/index/return` | `$.data[]` | 历史区间收益 |
| `POST /skill/v2/index/valuation` | `$.data[]` | 当前估值与历史分位 |
| `POST /skill/v2/index/financial-indicators` | `$.data[]` | 基本面汇总指标 |
| `GET /skill/v2/quote/index` | `$.data.list[]` | 最新指数行情 |
| `POST /skill/v2/quote/minite` | `$.data.dataList[]` | 分钟走势与增量行情 |

## 指数搜索与高级筛选

### `POST /skill/v2/search/chinaIndex`

指数高级检索直接使用 `/search/chinaIndex`，不调用 `/search/index`，也不执行兼容回退。该接口只保证中国指数能力，不应据此声称境外指数搜索完整可用。

请求体：

| 参数 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `keyword` | string | 否 | 指数代码、名称或简称 |
| `pageNum` | integer | 否 | 默认1 |
| `pageSize` | integer | 否 | 默认10 |
| `filters` | object | 否 | 复杂筛选条件 |

`filters` 支持：

- `productType[]`：一级-二级-三级分类字符串；
- 表现区间：`pctChg1D/1W/1M/3M/6M/TY/1Y/3Y/5Y`；
- 估值：`PETtm/PETtm5Y`、`PBLf/PBLf5Y`、`PSTtm/PSTtm5Y`；
- 基本面：`dividendYield`、`ROE`、`operatingRevenueYoy`、`parentComOwnerYoy`；
- 跟踪产品：`trackETFNetInFlow`、`trackETFAmount`、`trackETFCount`、`trackETFScale`、`trackETFLinkedCount`、`trackETFLinkedScale`；
- 年度表现：`lastYearYield`、`prevYearYield`。

数值筛选均为 `{ "min": number, "max": number }`，边界包含在内。注意 `trackETFScale` 和 `trackETFLinkedScale` 在搜索接口文档中为万元；资金流和成交额为元。

分页字段：`$.data.pageNum`、`pageSize`、`totalNum`、`serverTime`。

> **筛选与分页规则**：筛选类条件（表现、估值、基本面、跟踪产品区间）必须优先用 `filters` 参数在服务端完成，禁止靠翻页逐条人工过滤。搜索响应已随附行情（`lastPrice`、`changeRate`）、表现（`pctChg*`）、估值基本面和跟踪产品等字段；筛选、排序和比较必须基于搜索结果在本地完成，不为每只候选重复请求 `index/detail`。`pageSize` 建议直接取大值一次取回候选；翻页仅为浏览候选，根据 `totalNum` 判断是否还有未覆盖结果，仅当已取页面确实无匹配候选时才翻页，最多翻页 5 页，仍覆盖不全时在回答中说明筛选条件、覆盖范围与排序口径，不得继续扫库。确需详情时，多指数必须用批量接口一次传入全部代码，禁止逐个单查。

`$.data.data[]` 关键字段：

- 标识分类：`trdCode`、`sinfoWindcode`、`indexName`、`indexSht`、`firstClass`、`indexType`、上下级分类。
- 随附行情：`lastPrice`（点）、`changeRate`（%）。
- 表现：`pctChg*`、`lastYearYield`、`prevYearYield`。
- 估值基本面：`PETtm/PBLf/PSTtm`及分位、`ROE`、`dividendYield`、营收与利润增速。
- 跟踪产品：ETF/场外基金数量与规模、`trackETFAmount`、`trackETFNetInFlow`。
- 代表产品：`maxScaleFund`、`maxExcessReturnFund`、`minTrackErrorFund`。
- 产品列表：`relatedETF[]`、`relatedOutIndex[]`。
- 行情属性：`regionType`、`quoteRegionType`、`realtimeQuoteType`、`authorizedIndex`。

## 按成分股反查指数

### `POST /skill/v2/search/index-by-stock`

请求体：

- `stockCodes` 必填；
- `onlyIncludeFullMatch=Y` 同时包含全部输入股票，`N` 包含任意一只；
- `pageNum/pageSize`、`sortField/sortOrder` 可选；
- `showOnlyMaxIndexScaleMatch` 当前为预留参数，不依赖其过滤效果。

`$.data.list[]`：`sInfoWindcode`、`trdCode`、`indexName`、`indexSht`、`indexType`、`totalRatio`、`holdingsDetail[]`。

`holdingsDetail[]`：`stockCode`、`secuSht`、`holdNavRat`。分页信息位于 `currentPage`、`pageSize`、`totalPage`、`totalCount`；`requestList[]` 用于回显输入股票。

## 指数详情

### `POST /skill/v2/index/detail`

请求体：`fundCodes` 必填，最多20个指数代码。

结果：`$.data[]`，外层为 `indexCode`、`availabilityStatus`、`detail`。

`detail` 按问题选择字段：

| 类别 | 关键字段 |
|---|---|
| 标识分类 | `trdCode`、`sinfoWindcode`、`indexName`、`indexSht`、`indexType`、各级分类 |
| 编制属性 | `pubDt`、`baseDt`、`creatIndexOrg`、`regionType`、`quoteRegionType`、`realtimeQuoteType` |
| 随附行情 | `lastPrice`（点）、`changeRate`（%） |
| 跟踪产品 | `relatedETF[]`、`relatedOutIndex[]`、ETF/场外数量与规模 |
| 代表产品 | `maxScaleFund`、`maxExcessReturnFund`、`minTrackErrorFund` |
| 收益 | `annualizedReturn*`、`pctChg*` |
| 风险 | `annualizedVol*`、`volatility*`、`maxDown*`、`sharpRatio*` |
| 市值风格 | `marketCapDistTrdDt`、大中小盘数量与占比 |
| 行业分布 | `industryDistribution[]` 中的日期、行业名、权重与排序 |

相关基金规模存在单位差异：文档中 `relatedETF[].fundScale`、`trackETFScale` 和部分代表ETF规模为万元；`relatedOutIndex[].fundScale`、`trackETFLinkedScale` 为元。展示前按具体字段换算。

以下字段虽然以 `Json` 结尾，当前真实响应是资源链接字符串，不是内嵌 JSON：

- `eodPriceJson`
- `financialIndicatorJson`
- `valuationPercentileJson`
- `dividendRatioJson`

除非用户明确要求访问链接内容，否则不要继续抓取，也不要直接 `json.loads`。

## 指数前十大成分股

### `POST /skill/v2/index/holdings`

请求体：`fundCodes` 必填，最多10个；`date` 可选，格式 `yyyy-MM-dd`。

`$.data[].holdingItems[]`：`stockCode`、`secuSht`、`holdNavRat`（%）。部分辅助日期或Wind字段可能为空，不自行补造报告期。

## 指数区间收益

### `POST /skill/v2/index/return`

| 参数 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `codes` | array | 是 | 最多10个 |
| `timeMode` | string | 是 | `PERIOD` 或 `RANGE` |
| `period` | string | PERIOD时 | `1D/1W/1M/3M/6M/1Y/3Y/5Y/10Y/TY/INCE` |
| `startDate/endDate` | string | RANGE时 | `yyyy-MM-dd` |
| `boundaryMatchMode` | string | 否 | `FLEXIBLE` 默认，或 `STRICT` |

`$.data[]`：`trdCode`、`code`、`startDate`、`endDate`、`returnRate`（%）、`availabilityStatus`、`serverTime`。

展示实际起止日期；状态异常时不补造收益率。

## 指数估值

### `POST /skill/v2/index/valuation`

请求体：`indexCodes` 必填，最多10个。

`$.data[]`：

- `trdCode`、`trdDt`；
- 当前倍数：`pETtm`、`pBLf`、`pSTtm`；
- 历史分位：对应字段后缀 `3M/6M/TY/1Y/2Y/3Y/5Y/10Y/Bgn`，单位%。

API 响应使用小写前缀 `pETtm/pBLf/pSTtm`，与搜索接口 `PETtm/PBLf/PSTtm` 大小写不同。当前倍数与百分位不可混淆。

## 指数基本面指标

### `POST /skill/v2/index/financial-indicators`

请求体：`indexCodes` 必填，最多10个。

`$.data[]`：

| 字段 | 单位/含义 |
|---|---|
| `trdCode`、`trdDt` | 指数代码、更新日期 |
| `rOE` | 净资产收益率（%） |
| `dividendYield` | 股息率（%） |
| `operatingRevenueYoy` | 营收同比增速（%） |
| `parentComOwnerYoy` | 归母净利润同比增速（%） |
| `operatingIncome` | 营业收入（元） |
| `parentComOwners` | 归母净利润（元） |

这些是指数成分股汇总口径，不是单家公司的财务数据。

## 指数盘口行情

### `GET /skill/v2/quote/index?symbols=...`

> **调用前检查**：`search/chinaIndex` 和 `index/detail` 的响应已随附 `lastPrice`（点）和 `changeRate`（%）。已通过它们获得问题所需的最新点位或涨跌幅时，**禁止**再调本接口获取相同信息。只有需要以下本接口独有字段时才调用：`changeValue`（涨跌额）、`yesterdayClosePrice`（昨收）、`dealVolume`/`dealBalance`（成交量/额）、精确行情时间（`date + timeStamp`）。
>
> **应当使用本接口的情形**：用户以"现在/实时/盘中"口径询问点位、要求精确到秒的行情时间，或明确提出批量刷新行情（多只指数一次查最新点位）时，直接使用本接口——随附行情字段不含 `date + timeStamp`，用随附字段回答实时口径问题属于口径不达标。

`symbols` 必填，英文逗号分隔，最多50个。

`$.data.list[]`：`symbol`、`lastPrice`（点）、`changeValue`（点）、`changeRate`（%）、`yesterdayClosePrice`（点）、`dealVolume`、`dealBalance`（元）、`turnoverRatio`、`date`、`timeStamp`。

响应模型可能还出现 `iopv`，该字段对指数无实际意义，不要展示为有效指数指标。指数通常没有 `deviationRate`，不得补造溢折率。

## 指数分钟行情

### `POST /skill/v2/quote/minite`

请求体：`fundCodeList` 必填，最多50个；`date` 可选；`lastTimestamp=0` 全量，`>0` 增量。

`$.data.dataList[]` 包含 `symbol`、`quoteList[]`、`latestQuote`。分钟记录读取 `minute`、`lastPrice`、`changeRate`；指数的 `iopv` 不作为有效指标展示。

## 时间、单位与解释

- 行情数据时间：每条行情的 `date + timeStamp`；`serverTime` 只是服务器时间。
- 非交易时段表述为“接口返回的最新一笔行情”。
- 点位、涨跌额使用“点”；收益率、涨跌幅、权重、估值分位和基本面比例使用“%”。
- 估值倍数使用“倍”；金额按接口字段的元或万元换算。
- 低历史分位只说明当前指标在自身历史中的位置，不等价于投资建议或未来回报判断。
