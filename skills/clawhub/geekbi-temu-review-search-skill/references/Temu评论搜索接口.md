# Temu 评论搜索接口

## 目录

- [脚本调用](#脚本调用)
- [查询参数](#查询参数)
- [推荐查询](#推荐查询)
- [排序字段](#排序字段)
- [成功响应](#成功响应)
- [评论字段](#评论字段)
- [无数据与失败处理](#无数据与失败处理)

## 脚本调用

- 单页数量：最大 200
- 去重口径：相同评论 ID 只保留一条

基础调用：

```bash
python3 scripts/temu_review_search.py \
  --param "goodsId=601099512345678" \
  --param "size=20"
```

服务端要求暂停查询时，按 [查询暂停与恢复流程](查询暂停与恢复流程.md) 提示用户；恢复条件满足后再次运行同一命令。

## 查询参数

| 参数 | 类型 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `goodsId` | string | 必填 | Temu 商品 ID，最长 100 个字符 |
| `siteId` | integer | `48` | 极鲸云站点 ID；默认美国站，其他国家或地区先实时解析站点 |
| `skuId` | string | 无 | 可选 SKU ID，用于限定商品规格，最长 100 个字符 |
| `scoreMin` | integer | 无 | 最低评分，1 至 5 |
| `scoreMax` | integer | 无 | 最高评分，1 至 5 |
| `helpfulMin` | integer | 无 | 最小有用数，不小于 0 |
| `helpfulMax` | integer | 无 | 最大有用数，不小于 0 |
| `commentTimeMin` | datetime | 无 | 最早评论时间，ISO 8601 格式 |
| `commentTimeMax` | datetime | 无 | 最晚评论时间，ISO 8601 格式 |
| `sort` | string | `commentTime` | 排序字段，取值见下方 |
| `order` | string | `desc` | `asc` 或 `desc` |
| `page` | integer | `1` | 页码，从 1 开始 |
| `size` | integer | `20` | 每页数量，最大 200 |

最低值不能大于对应最高值。分页最多读取排序后的前 10000 条；需要研究大量评论时应缩小评分、规格或时间范围后分批读取。

## 推荐查询

最有用的差评：

```bash
python3 scripts/temu_review_search.py \
  --param "goodsId=601099512345678" \
  --param "scoreMax=3" \
  --param "sort=helpful" \
  --param "order=desc" \
  --param "size=100"
```

指定时间范围内的最新评论：

```bash
python3 scripts/temu_review_search.py \
  --param "goodsId=601099512345678" \
  --param "commentTimeMin=2026-01-01T00:00:00+08:00" \
  --param "commentTimeMax=2026-07-31T23:59:59+08:00" \
  --param "sort=commentTime" \
  --param "order=desc"
```

## 排序字段

| 维度 | `sort` 值 | 常用方向 |
| --- | --- | --- |
| 评论时间 | `commentTime` | `desc`，最新评论优先 |
| 有用数 | `helpful` | `desc`，更多用户认为有参考价值的评论优先 |
| 评分 | `score` | `asc` 看低分，`desc` 看高分 |
| 采集时间 | `createTime` | `desc`，最近进入极鲸云的数据优先 |

## 成功响应

```json
{
  "code": 0,
  "data": {
    "total": 37,
    "list": [
      {
        "id": "document-id",
        "siteId": 48,
        "reviewId": "review-id",
        "comment": "The material is better than expected.",
        "score": 5,
        "goodsId": "601099512345678",
        "skuId": "sku-id",
        "specs": "{\"Color\":\"Blue\",\"Size\":\"M\"}",
        "pictures": ["https://example.com/review.jpg"],
        "video": "https://example.com/review.mp4",
        "helpful": 18,
        "commentTime": "2026-07-01T12:00:00.000+00:00",
        "createTime": "2026-07-02T12:00:00.000+00:00"
      }
    ]
  }
}
```

- `data.total` 是当前条件下按评论 ID 去重后的评论总数。
- `data.list` 是当前页评论，返回下表中的全部已存储字段；字段没有数据时可能为 `null` 或空数组。

## 评论字段

| 字段 | 中文含义 | 分析用途 |
| --- | --- | --- |
| `id` | 记录 ID | 区分极鲸云中的数据记录 |
| `siteId` | 站点 ID | 区分评论所属 Temu 站点，并与商品详情链接保持一致 |
| `reviewId` | 评论 ID | 评论去重与明细追踪 |
| `comment` | 评论内容 | 痛点、卖点、场景和情绪分析 |
| `score` | 评分 | 1 至 5 星评价结构 |
| `goodsId` | 商品 ID | 确认评论归属商品 |
| `skuId` | SKU ID | 比较不同商品规格 |
| `specs` | 规格信息 | 可能是结构化文本，保留原值并解析颜色、尺寸、型号等 |
| `pictures` | 评论图片 | 评论附带的图片地址数组 |
| `video` | 评论视频 | 评论附带的视频地址 |
| `helpful` | 有用数 | 认为该评论有参考价值的用户数，不代表主题出现次数 |
| `commentTime` | 评论时间 | 用户发表时间，用于新旧反馈和趋势分析 |
| `createTime` | 采集时间 | 数据进入极鲸云的时间，不等于用户发表时间 |

## 无数据与失败处理

- 成功响应中 `data.total = 0` 且 `data.list = []` 表示当前条件没有已收录评论。先核对商品 ID、站点、SKU、评分和时间范围；仍为空时明确说明暂未收录，不继续生成评论结论。
- 服务端要求暂停查询时，按 [查询暂停与恢复流程](查询暂停与恢复流程.md) 展示提示，有跳转地址时再展示可点击链接，不把它解释为无评论。
- 退出码 `1` 时读取 stderr 一级 `msg`，面向用户只提示该中文文案。
- 请求多页时逐页累计并记录实际读取页数；未完成全部分页时不得声称结果为全量。
