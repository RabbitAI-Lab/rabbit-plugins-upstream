# SHEIN 评论搜索接口

## 调用

```bash
python3 scripts/shein_review_search.py \
  --param goodsId=123456789 \
  --param siteId=1 \
  --param scoreMin=1 \
  --param scoreMax=2 \
  --param sort=commentTime \
  --param order=desc \
  --param page=1 \
  --param size=100
```

## 参数

| 参数 | 规则 |
| --- | --- |
| `goodsId` | 必填，明确 SHEIN 商品 ID，最长 100 字符 |
| `siteId` | 默认入口 1 名称“全部”但当前映射 `us`，不是跨站聚合；明确美国 2；其他站实时解析 |
| `specs` | 规格 JSON 字符串的精确条件，最长 300 字符 |
| `scoreMin/Max` | 1–5 分 |
| `helpfulMin/Max` | 有用数，非负整数 |
| `commentTimeMin/Max` | ISO 8601 评论时间 |
| `sort` | `commentTime`、`helpful`、`score`、`createTime` |
| `order` | 只允许小写 `asc|desc`，默认 `desc` |
| `page` / `size` | 默认 1/20，每页最大 200，结果窗口最多前 10000 条 |

最小值不得大于最大值。不要传 Temu 的 `regionId` 或 `skuId`；SHEIN 使用站点和 `specs`。

## 响应

成功响应 `data` 包含去重后的 `total`、`list`、`site`。评论项公开：`id`、`siteId`、`siteUID`、`commentId`、`comment`、`score`、`specs`、`pictures`、`goodsId`、`helpful`、`commentTime`、`createTime`。服务端按 `commentId` 去重，并使用稳定次排序。`total` 使用 Elasticsearch 基数统计，超大评论集可能有近似误差；完整分页以不足一页、空页或 10000 条结果窗口上限为停止条件，不只依赖 `total`。

`specs` 保留数据源 JSON 字符串契约，调用方需要解析时必须容忍无效或空值。退出状态：成功 0，需要动作 2，错误 1。
