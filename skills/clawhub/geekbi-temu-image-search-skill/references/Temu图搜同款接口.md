# Temu 图搜同款接口

## 目录

- [调用脚本](#调用脚本)
- [图片输入](#图片输入)
- [基础参数](#基础参数)
- [筛选与排序参数](#筛选参数)
- [商品数据口径](#金额与币种口径)
- [响应与失败处理](#成功响应)

## 调用脚本

```bash
python3 scripts/temu_image_search.py \
  --image "/path/to/product.jpg" \
  --param "siteId=48" \
  --param "page=1" \
  --param "size=20"
```

脚本上传图片、在视觉候选池中应用商品条件并输出 JSON。查询需要登录；认证模块会自动复用极鲸云 Temu Skills 的统一登录态，不要在每次查询前重复登录。服务端要求暂停时遵循 [查询暂停与恢复流程](查询暂停与恢复流程.md)。

## 图片输入

`--image` 支持以下输入：

| 输入形式 | 示例或规则 |
| --- | --- |
| 本地文件或会话附件 | 使用图片在当前运行环境中的真实文件路径 |
| 文件地址 | `file:///path/to/product.jpg` |
| 图片网址 | `http://` 或 `https://` 开头的可直接下载地址 |
| Data URI | `data:image/png;base64,...` |
| Base64 | 使用 `base64:...` 前缀 |
| 标准输入 | 使用 `--image -`，从标准输入读取原始图片字节 |

- 图片最大为 10M。
- 脚本根据图片内容识别 JPEG、PNG、GIF、WebP、BMP、TIFF、AVIF 和 HEIC/HEIF 等常见格式，不只依赖文件扩展名。
- 对聊天中上传的图片，优先使用平台提供的本地附件路径；不要把图片内容打印到对话、日志或思考过程。
- 图片网址无法直接下载、需要网页 Cookie 或存在防盗链时，先保存为本地临时文件再传入。

## 基础参数

所有查询参数都使用可重复的 `--param "key=value"` 传入。单页 `size` 最大为 200。

| 参数 | 类型 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `keyword` | string | 无 | 在视觉候选中继续匹配商品名称或品牌关键词，最长 300 个字符 |
| `catIds` | integer，可重复 | 无 | 可信 Temu 类目 ID；多个 ID 匹配其中任一类目 |
| `siteId` | integer | `48` | 极鲸云站点 ID；美国站直接使用默认值，其他站点先用 `scripts/temu_site_list.py` 实时解析 |
| `page` | integer | `1` | 页码 |
| `size` | integer | `20` | 每页数量，最大 200 |
| `sort` | string | 无 | 业务排序字段；省略时保留图片相似度顺序 |
| `order` | string | `desc` | `asc` 或 `desc` |
| `hostingMode` | integer | 无 | 托管模式；`1` 全托管、`2` 半托管 |

- 图片候选与所有商品条件是交集关系。只添加回答当前问题必需的条件，避免过度筛选。
- 仅在用户提供或当前上下文已有可信类目 ID 时使用 `catIds`，不得根据类目名称猜测 ID，也不得依赖其他 Skill 获取类目 ID。
- 用户明确给出商品词时可以使用 `keyword`；不要将对图片的主观描述转换成关键词来替代图片检索。
- 多个 `catIds` 使用多个同名参数，例如 `--param "catIds=123" --param "catIds=456"`。
- 用户指定其他国家或地区时，运行 `python3 scripts/temu_site_list.py --country "国家或地区名"`；无唯一精确匹配时请用户确认，不自行选择。
- 分页查询时始终使用同一张图片和同一组条件，只改变页码。请求全部结果时依据 `data.total` 继续分页。

## 筛选参数

所有区间都可只传最小值或最大值。

| 维度 | 最小值参数 | 最大值参数 |
| --- | --- | --- |
| 总销量 | `soldMin` | `soldMax` |
| 日销量 | `daySoldMin` | `daySoldMax` |
| 周销量 | `weekSoldMin` | `weekSoldMax` |
| 月销量 | `monthSoldMin` | `monthSoldMax` |
| 日销量增长率 | `daySoldRateMin` | `daySoldRateMax` |
| 周销量增长率 | `weekSoldRateMin` | `weekSoldRateMax` |
| 月销量增长率 | `monthSoldRateMin` | `monthSoldRateMax` |
| 总销售额 | `salesMin` | `salesMax` |
| 日销售额 | `daySalesMin` | `daySalesMax` |
| 周销售额 | `weekSalesMin` | `weekSalesMax` |
| 月销售额 | `monthSalesMin` | `monthSalesMax` |
| 日销售额增长率 | `daySalesRateMin` | `daySalesRateMax` |
| 周销售额增长率 | `weekSalesRateMin` | `weekSalesRateMax` |
| 月销售额增长率 | `monthSalesRateMin` | `monthSalesRateMax` |
| 库存 | `quantityMin` | `quantityMax` |
| 店铺销量 | `mallSoldMin` | `mallSoldMax` |
| 同款数 | `similarNumMin` | `similarNumMax` |
| 商品价格 | `priceMin` | `priceMax` |
| 供货价 | `supplyPriceMin` | `supplyPriceMax` |
| 商品评分 | `goodsScoreMin` | `goodsScoreMax` |
| 评论数 | `reviewNumMin` | `reviewNumMax` |
| 上架时间 | `onSaleTimeMin` | `onSaleTimeMax` |
| 开店时间 | `mallOpenTimeMin` | `mallOpenTimeMax` |

时间参数使用 ISO 8601 日期时间。

## 排序字段

| 维度 | `sort` 可选值 |
| --- | --- |
| 销量 | `sold`、`daySold`、`weekSold`、`monthSold`、`mallSold` |
| 销量增长率 | `daySoldRate`、`weekSoldRate`、`monthSoldRate` |
| 销售额 | `sales`、`daySales`、`weekSales`、`monthSales` |
| 销售额增长率 | `daySalesRate`、`weekSalesRate`、`monthSalesRate` |
| 价格 | `minPrice`、`maxPrice`、`supplyPrice`、`minSupplyPrice`、`medianSupplyPrice`、`maxSupplyPrice` |
| 商品指标 | `quantity`、`goodsScore`、`reviewNum`、`similarNum` |
| 时间 | `onSaleTime`、`mallOpenTime` |

未指定 `sort` 时保留图片相似度顺序；指定后只在视觉候选池中按业务字段排序。

## 金额与币种口径

- `supplyPrice`、`minSupplyPrice`、`medianSupplyPrice`、`maxSupplyPrice` 及供货价筛选区间的单位固定为人民币（CNY）。
- `minPrice`、`maxPrice` 及商品价格筛选区间使用当前站点币种；美国站使用美元。
- 展示金额时明确标注币种。计算价差、毛利或利润前先换算为同一币种，并说明汇率及日期；没有可靠汇率时不得直接相减。

## 同款数口径

- `similarNum` 表示销售同一款商品的同行数量，不等于当前图片查询的命中商品数。
- 默认将不超过 10 视为优选区间，11 至 20 视为中等竞争，超过 20 视为高竞争。
- 将同款数与销量、增长、价格、供货价、评分和上架时间结合判断，不单独据此下结论。

## 库存口径

- `quantity` 大于 `0` 时仅表示当前采集到的库存快照，不等于长期可售库存。
- `quantity` 为 `0` 时按“暂未统计到，需进一步核实”处理，不直接认定为缺货或售罄。
- 计算库存指标时将值为 `0` 的商品作为缺失样本并披露排除数量。

## 成功响应

```json
{
  "code": 0,
  "data": {
    "total": 460,
    "list": []
  }
}
```

- `data.total` 是视觉候选与全部商品条件交集后的命中数。
- `data.list` 是当前页完整 Temu 商品记录，包含商品 ID、店铺 ID、标题、图片、类目、价格、供货价、销量、销售额、增长率、评分、评论数、库存、状态、托管模式和时间字段。
- 服务端为每个商品返回 `linkUrl`。每次向用户展示商品时都必须将标题写成 `[商品标题](<linkUrl>)`，不得自行拼接、猜测或补全链接。
- `reviewNum` 只表示评论规模，不包含评论文本，不能据此推断具体好评或差评原因。

## 失败处理

- 将 `code != 0`、HTTP 非 2xx、响应不是 JSON 或缺少 `data` 视为查询失败。
- 服务端提供一级 `msg` 时只向用户展示该中文文案，不打印错误 JSON、请求参数、英文响应字段或内部状态。
- 服务端要求暂停并返回跳转地址时，按 [查询暂停与恢复流程](查询暂停与恢复流程.md) 暂停；恢复后使用原图片和原查询条件重新调用。
