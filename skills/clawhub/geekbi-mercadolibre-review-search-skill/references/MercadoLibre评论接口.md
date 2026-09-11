# Mercado Libre 评论接口

运行 `scripts/mercadolibre_review_search.py`，必须传 `--param goodsId=<商品ID或产品ID>`。

可选条件：

- `siteId`，默认 `1`（墨西哥）；
- `keyword`，匹配评论正文；
- `scoreMin/Max`，1 到 5；
- `helpfulMin/Max`；
- `sort=commentTime|helpful|score`、`order=asc|desc`；
- `page`、`size`，最多访问前 200 条。

接口同时在评论的 `goodsId` 和 `productId` 字段中匹配输入 ID。响应可包含评论 ID、商品/产品 ID、评分、正文、图片链接、有用数、评论时间和采集时间。
