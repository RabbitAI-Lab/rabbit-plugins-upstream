# SHEIN 类目搜索接口

## 调用

```bash
python3 scripts/shein_category_search.py \
  --param siteId=1 \
  --param keyword=女装 \
  --param catLevel=2 \
  --param sort=totalSold \
  --param order=desc
```

基础参数：`keyword`、`siteId`、`catLevel`、精确 `parentCatId`、`page`、`size`、`sort`、`order`。默认入口 1 名称为“全部”但当前映射 `us`，不是跨站聚合；明确美国用 2，其他站点实时解析。

以下指标均支持 Min/Max：

- `dsr`、`sold`、`sales`、`totalSold`、`totalSales`、`avgPrice`。
- `itemCount`、`semiManagedItemCount`、`mallCount`、`semiManagedMallCount`。
- 日/周/月均 `Sold`、`Sales`、`ItemCount`、`MallCount` 及全部对应 Rate。

可排序字段为 `catLevel`、上述数值指标、`createTime`、`updateTime`。方向只允许小写 `asc|desc`；页码从 1 开始，每页最大 200，`page × size` 不得超过 10000。`total` 是精确命中数；命中超过 10000 时只能访问前 10000 条，应缩小筛选范围后再做完整分布分析。

## 响应字段

成功响应 `data` 包含 `total`、`list`、`site`。类目项公开：

- `id`、`catId`、`siteId`、`siteUID`、`linkUrl`。
- `thumbnail`、`catName`、`catNameCn`、`catLevel`、`parentCatId`、`isLeaf`、`parentCatItems`。
- `dsr`、`sold`、`sales`、`totalSold`、`totalSales`、`avgPrice`。
- `itemCount`、`semiManagedItemCount`、`mallCount`、`semiManagedMallCount`。
- 日/周/月均销量、销售额、商品数、店铺数及全部 Rate。
- `createTime`、`updateTime`。

不返回收藏等用户私有字段。退出状态：成功 0，需要动作 2，错误 1。
