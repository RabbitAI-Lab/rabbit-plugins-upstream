# SHEIN 图搜同款接口

## 调用

```bash
python3 scripts/shein_image_search.py \
  --image /absolute/path/product.jpg \
  --param siteId=1 \
  --param sort=daySold \
  --param order=desc \
  --param page=1 \
  --param size=20
```

`--image` 支持本地路径、`file:`、`http:`、`https:`、图片 Data URI、`base64:` 内容，或 `-` 从标准输入读取。脚本在本地读取远程图片后上传；单图最大 10 MiB，支持 JPEG、PNG、GIF、WebP、BMP、TIFF、AVIF、HEIC/HEIF，不支持 SVG。

所有 `--param`、排序、分页与响应字段完全复用 [商品搜索接口](SHEIN商品搜索接口.md)。图片是必填输入，不能用关键词代替。

## 分页与排序

- 要完整结果时，以 `size=200` 重复上传同一张图片，保持全部筛选不变并依次请求后续页，直至累计条数覆盖 `total`。这里的完整仅指服务端本次视觉候选池与筛选条件的交集；候选池最多 1000 个，`total=1000` 时不得称 SHEIN 全平台全部同款。
- 未指定业务排序时只称“视觉相似候选”，除非响应明确返回相似度及顺序，否则不宣称按最相似排列。
- 指定 `sort` 后，结果是在视觉候选池中按商品业务指标重排。
- `similarNum` 对外统一称为“同款数（跟卖数）”，并按商品搜索接口的同款竞争口径解释。

成功、暂停与错误退出状态和商品搜索一致。
