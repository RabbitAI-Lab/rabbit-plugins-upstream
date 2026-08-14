# SHEIN 店铺榜单查询预设

每次选择一个最贴近用户意图的主预设。补充站点、分页以及用户明确的关键词、类目或托管模式；不继承其他查询状态。

## 预设

### 热销店铺

```text
sort=mallSold
order=desc
```

按店铺近 3 个月销量排序。这是 SHEIN 网页当前实际口径，不按评论量代替热销。

### 高评论店铺（Skill 补充）

```text
sort=reviewNum
order=desc
```

评论数反映反馈规模，不等于高评分或好口碑。

### 热销新店

```text
mallOpenTimeMin=<执行时刻减3个自然月的ISO时间>
mallOpenTimeMax=<执行时刻的ISO时间>
sort=mallSold
order=desc
```

对“潜力新店”结论还需检查月销量、增长、商品数和口碑，避免被单一历史爆款误导。

### 最近开店

```text
sort=mallOpenTime
order=desc
```

不自动增加时间范围；用户明确范围时再补充。

## 请求前检查

- 默认入口 `1` 名称为“全部”但当前映射 `us`，不是跨站聚合；明确美国用 `2`，其他站实时解析。
- 近 3 个月已换算成绝对 ISO 8601。
- 排序只用 `asc|desc`，并区分近 3 个月销量、累计销量、评论规模和评分。
