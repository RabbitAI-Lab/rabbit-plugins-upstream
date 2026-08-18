# SHEIN 商品榜单查询预设

根据用户榜单或选品意图选择一个主预设，用户明确条件始终优先。预设依据 `geekbi-web-v2` 当前实际请求参数整理；文案与代码不一致时以代码为准。

## 使用规则

- 不叠加多个预设；从全新参数对象生成请求，避免网页或上一轮残留条件污染结果。
- 默认补 `siteId=1`（名称“全部”，当前映射 `us`，不是跨站聚合）；明确美国用 `2`，其他站点实时解析。再补页码和每页数量。
- 关键词与类目通常二选一；只有用户明确交叉限定时才组合。
- 排序方向只用 `asc|desc`。
- “近 3 个月”按执行时刻减 3 个自然月，转换成带时区 ISO 8601 绝对时间。
- 预设只定义筛选和排序，不代表命中结果必然是爆品或蓝海。

## 预设

### 热销商品

```text
sort=sold
order=desc
```

按最近销量排序，不把 `sold` 写成累计总销量。

### 日销排行

```text
soldMin=10000
sort=daySold
order=desc
```

这是网页当前真实条件；最低最近销量 10000 是榜单门槛，不是日销量门槛。

### 蓝海爆品

```text
soldMin=100
similarNumMin=1
similarNumMax=30
onSaleTimeMin=<执行时刻减3个自然月的ISO时间>
onSaleTimeMax=<执行时刻的ISO时间>
sort=daySold
order=desc
```

这是网页内置模板的实际宽口径。网页文案中的“销量不超过 1000”并非请求条件，不自动补 `soldMax`。命中后仍应优先保留同款数（跟卖数）不超过 10 的候选，并将超过 20 的候选标为竞争偏高。

### 严格低同款竞争（Skill 补充）

需要更严格的低竞争候选时，使用与蓝海爆品相同条件，但改为：

```text
similarNumMax=10
```

结果不足且用户接受放宽时可升至 20；这个补充预设不是网页内置模板。

### 热销新品

```text
onSaleTimeMin=<执行时刻减3个自然月的ISO时间>
onSaleTimeMax=<执行时刻的ISO时间>
sort=sold
order=desc
```

### 新店热销

```text
mallOpenTimeMin=<执行时刻减3个自然月的ISO时间>
mallOpenTimeMax=<执行时刻的ISO时间>
sort=sold
order=desc
```

### 大卖新品

```text
onSaleTimeMin=<执行时刻减3个自然月的ISO时间>
onSaleTimeMax=<执行时刻的ISO时间>
sort=mallSold
order=desc
```

网页文案曾写“近 1 个月”，实际请求是近 3 个月；本预设按实际请求。

## 请求前检查

1. 站点是否正确，是否误把名称“全部”的 `1` 写成跨站聚合。
2. 相对时间是否已变为绝对 ISO 8601。
3. 是否只使用有效接口参数与 `asc|desc`。
4. 是否区分网页蓝海宽口径 30 与 Skill 严格低竞争口径 10。
5. 是否在取得数据后结合销量、趋势、价格、评分和店铺结构验证标签。
