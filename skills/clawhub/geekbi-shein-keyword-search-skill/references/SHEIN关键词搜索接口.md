# SHEIN 关键词搜索接口

## 调用

```bash
python3 scripts/shein_keyword_search.py \
  --param siteId=1 \
  --param keyword=dress \
  --param catIds=123 \
  --param sort=dsr \
  --param order=desc
```

基础参数：`keyword`、可重复 `catIds`、`siteId`、`page`、`size`、`sort`、`order`。默认入口 1 名称为“全部”但当前映射 `us`，不是跨站聚合；明确美国用 2，其他站点实时解析。

以下指标均支持 Min/Max：

- `dsr`、`sold`、`sales`、`totalSold`、`totalSales`、`avgPrice`。
- `firstOnSaleTime`，使用 ISO 8601。
- `itemCount`、`semiManagedItemCount`、`mallCount`、`semiManagedMallCount`。
- 日/周/月均 `Sold`、`Sales`、`ItemCount`、`MallCount` 及全部对应 Rate。

可排序字段为上述指标、`firstOnSaleTime`、`createTime`、`updateTime`。方向只允许小写 `asc|desc`；每页最大 200，`page × size` 不得超过 10000。`total` 是精确命中数；命中超过 10000 时只能访问前 10000 条，应缩小筛选范围后再做完整分布分析。

## 响应字段

成功响应 `data` 包含 `total`、`list`、`site`。关键词项公开：

- `id`、`siteId`、`siteUID`、`linkUrl`。
- `keyword`、`cnKeyword`、`thumbnail`、`catId`、`catIds`、`catItems`。
- `dsr`、`sold`、`sales`、`totalSold`、`totalSales`、`avgPrice`、`firstOnSaleTime`。
- `itemCount`、`semiManagedItemCount`、`mallCount`、`semiManagedMallCount`。
- 日/周/月均销量、销售额、商品数、店铺数及全部 Rate。
- `createTime`、`updateTime`。

`id` 是详情使用的关键词文档 ID，不等于关键词文本。不返回收藏等私有字段。退出状态：成功 0，需要动作 2，错误 1。
