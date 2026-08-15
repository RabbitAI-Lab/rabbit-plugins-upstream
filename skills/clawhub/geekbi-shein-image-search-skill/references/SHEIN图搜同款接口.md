# SHEIN 图搜同款接口

## 目录

- [脚本调用](#脚本调用)
- [图片输入](#图片输入)
- [站点解析](#站点解析)
- [查询参数](#查询参数)
- [筛选与排序](#筛选参数)
- [视觉候选与同款数](#视觉候选与同款数)
- [响应与失败处理](#成功响应)

## 脚本调用

```bash
python3 scripts/shein_image_search.py \
  --image /absolute/path/product.jpg \
  --param siteId=1 \
  --param sort=daySold \
  --param order=desc \
  --param page=1 \
  --param size=20
```

脚本在本地读取图片、上传图片、在视觉候选池中应用商品条件并输出 JSON。每个查询条件单独使用一个 `--param 名称=值`；`catIds` 可重复传入。默认服务地址为 `https://openapi.geekbi.com`，仅开发测试时传 `--base-url`。服务端要求暂停时遵循 [查询暂停与恢复流程](查询暂停与恢复流程.md)。

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

- 单图最大 10 MiB。
- 支持 JPEG、PNG、GIF、WebP、BMP、TIFF、AVIF 和 HEIC/HEIF，不支持 SVG。
- 对聊天中上传的图片，优先使用平台提供的本地附件路径；不要把图片内容打印到对话或日志。
- 图片网址无法直接下载、需要网页 Cookie 或存在防盗链时，先保存为本地临时文件再传入。

## 站点解析

- 未指定站点时传 `siteId=1`（名称“全部”，当前映射 `us`，不是跨站聚合）。
- 明确美国站时传 `siteId=2`。
- 其他国家、地区、站点 UID 或域名先运行：

```bash
python3 scripts/shein_site_list.py --country 德国
```

只在唯一命中后使用返回的 `siteId`；多义时请用户确认，不自行选择。

## 查询参数

所有查询参数都使用可重复的 `--param 名称=值` 传入。

| 参数 | 含义 |
| --- | --- |
| `keyword` | 在视觉候选中继续匹配商品名称、商品 ID、SPU、货号或店铺 ID，最长 300 字符 |
| `blockKeyword` | 排除商品名称中的词，最长 300 字符 |
| `matchMode` | `1` 严格 AND 匹配；`2` 75% 模糊匹配，默认 2 |
| `catIds` | 可信类目 ID，可重复；多个 ID 为 OR |
| `siteId` | 极鲸云 SHEIN 站点 ID |
| `hostingMode` | `1` 全托管；`2` 半托管；`0` 或不传为不限 |
| `page` / `size` | 页码默认 1；每页默认 20、最大 200；`page × size` 不得超过 10000 |
| `sort` / `order` | 排序字段；方向只允许 `asc` 或 `desc` |

- 图片候选与全部商品条件是交集关系，只添加回答当前问题必需的条件。
- 仅在用户提供或当前上下文已有可信类目 ID 时使用 `catIds`，不得根据类目名称猜测 ID，也不得依赖其他 Skill 获取类目 ID。
- 用户明确给出商品词时可以使用 `keyword`；不要将对图片的主观描述转换成关键词来替代图片检索。
- 分页查询时始终使用同一张图片和同一组条件，只改变页码。

## 筛选参数

数值范围均使用 `<指标>Min` / `<指标>Max`，所有区间可只传一端：

- 销量：`sold`、`totalSold`、`daySold`、`weekSold`、`monthSold`。
- 销量变化率：`daySoldRate`、`weekSoldRate`、`monthSoldRate`。
- 销售额：`sales`、`totalSales`、`daySales`、`weekSales`、`monthSales`。
- 销售额变化率：`daySalesRate`、`weekSalesRate`、`monthSalesRate`。
- 店铺与竞争：`mallSold`、`similarNum`。
- 价格与质量：`price`（过滤最低售价）、`supplyPrice`、`goodsScore`、`reviewNum`。

时间范围使用 ISO 8601：`onSaleTimeMin/Max`、`mallOpenTimeMin/Max`。最小值不得大于最大值。变化率传小数，例如 `0.2` 表示 20%。

可排序字段：

```text
sold,totalSold,daySold,weekSold,monthSold,
daySoldRate,weekSoldRate,monthSoldRate,totalSoldRate,
sales,totalSales,daySales,weekSales,monthSales,
daySalesRate,weekSalesRate,monthSalesRate,totalSalesRate,
minPrice,maxPrice,supplyPrice,minSupplyPrice,medianSupplyPrice,maxSupplyPrice,
goodsScore,reviewNum,similarNum,similarNumUpdateTime,onSaleTime,
mallSold,mallOpenTime,createTime,updateTime
```

未指定 `sort` 时只称结果为视觉相似候选；指定后只在视觉候选池中按业务字段排序。接口不接受 `siteUID`、商品状态、图片字段或精确同款数；同款数（跟卖数）仅用 Min/Max 筛选。

## 视觉候选与同款数

- `data.total` 是服务端本次视觉候选池与全部商品条件交集后的精确命中数。单次视觉候选池最多 1000 个，`total=1000` 时可能触及上限，不得称为 SHEIN 全平台全部同款。
- 每个商品的 `similarNum` 对外统一称为“同款数（跟卖数）”，表示销售同一款商品的同行数量，不等于 `data.total`。
- 默认将同款数不超过 10 视为优选区间，11 至 20 视为中等竞争，超过 20 视为高竞争。
- 将同款数与销量、增长、价格、供货价、评分和上架时间结合判断，不单独据此下结论。

## 商品数据口径

- `sold/sales` 表示最近销量/销售额，`totalSold/totalSales` 表示累计总量；未确认固定窗口时不将最近口径写成 90 天。
- 日、周、月变化率是小数比例，`0.25` 表示增长 25%。
- `minPrice`、`maxPrice` 和销售额使用当前站点币种；供货价字段使用人民币。计算利润前先统一币种并说明汇率及日期。
- `hostingMode` 只按 `1=全托管`、`2=半托管` 解释。
- `reviewNum` 只表示评论规模，不包含评论文本，不能据此推断具体好评或差评原因。

## 成功响应

```json
{
  "code": 0,
  "data": {
    "total": 100,
    "list": [],
    "site": {}
  }
}
```

- `data.list` 是当前页完整 SHEIN 商品记录。
- 标识字段包括 `id`、`goodsId`、`goodsSn`、`spuId`、`mallId`、`siteId`、`siteUID`、`linkUrl`。
- 基础字段包括 `hostingMode`、`thumbnail`、`goodsName`、`catId`、`catIds`、`catItems`。
- 竞争字段包括 `similarNum`、`similarNumUpdateTime`。
- 销量字段包括 `sold`、`daySold`、`weekSold`、`monthSold`、`totalSold` 及对应变化率。
- 销售额字段包括 `sales`、`daySales`、`weekSales`、`monthSales`、`totalSales` 及对应变化率。
- 价格字段包括 `minPrice`、`maxPrice`、`supplyPrice`、`minSupplyPrice`、`medianSupplyPrice`、`maxSupplyPrice`。
- 质量、店铺与时间字段包括 `goodsScore`、`reviewNum`、`mallOpenTime`、`mallSold`、`onSaleTime`、`createTime`、`updateTime`。
- `site` 包含站点名、域名、语言、货币符号、符号位置、汇率和千分位信息。
- 每次展示商品时，必须将标题写成 `[商品标题](<linkUrl>)`；不得根据商品 ID 或站点自行拼接、猜测或补全链接。

## 失败处理

- 退出状态 `0` 表示查询成功并输出 JSON。
- 退出状态 `2` 表示需要用户完成登录、额度或开通动作，按暂停流程处理。
- 退出状态 `1` 表示参数、网络或接口错误，错误 JSON 写入标准错误。
- 服务端提供一级 `msg` 时只向用户展示该中文文案，不打印错误 JSON、图片内容、英文响应字段或内部状态。
