# SHEIN 商品搜索接口

## 调用

```bash
python3 scripts/shein_goods_search.py \
  --param siteId=1 \
  --param keyword=dress \
  --param soldMin=100 \
  --param sort=daySold \
  --param order=desc \
  --param page=1 \
  --param size=20
```

每个查询条件单独使用一个 `--param 名称=值`。`catIds` 可重复传入；脚本保持多值。默认服务地址为 `https://openapi.geekbi.com`，仅开发测试时传 `--base-url`。

## 站点解析

- 未指定：传 `siteId=1`（名称“全部”，当前映射 `us`，不是跨站聚合）。
- 明确美国：传 `siteId=2`。
- 其他国家、地区、站点 UID 或域名：先运行：

```bash
python3 scripts/shein_site_list.py --country 德国
```

只在唯一命中后使用返回的 `siteId`；多义时请用户确认。

## 参数

基础条件：

| 参数 | 含义 |
| --- | --- |
| `keyword` | 商品名称、商品 ID、SPU、货号或店铺 ID 的混合查询，最长 300 字符 |
| `blockKeyword` | 排除商品名称中的词，最长 300 字符 |
| `matchMode` | `1` 严格 AND 匹配；`2` 75% 模糊匹配，默认 2 |
| `catIds` | 类目 ID，可重复；多个 ID 为 OR |
| `siteId` | 极鲸云 SHEIN 站点 ID |
| `hostingMode` | `1` 全托管；`2` 半托管；`0` 或不传为不限 |
| `page` / `size` | 页码默认 1；每页默认 20、最大 200；`page × size` 不得超过 10000 |
| `sort` / `order` | 排序字段；方向只允许 `asc` 或 `desc` |

数值范围均使用 `<指标>Min` / `<指标>Max`：

- 销量：`sold`、`totalSold`、`daySold`、`weekSold`、`monthSold`。
- 销量变化率：`daySoldRate`、`weekSoldRate`、`monthSoldRate`。
- 销售额：`sales`、`totalSales`、`daySales`、`weekSales`、`monthSales`。
- 销售额变化率：`daySalesRate`、`weekSalesRate`、`monthSalesRate`。
- 店铺与竞争：`mallSold`、`similarNum`。
- 价格与质量：`price`（过滤最低售价）、`supplyPrice`、`goodsScore`、`reviewNum`。

时间范围使用 ISO 8601：`onSaleTimeMin/Max`、`mallOpenTimeMin/Max`。最小值不得大于最大值。变化率传小数，如 `0.2` 表示 20%。

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

接口不接受 `siteUID`、商品状态、图片字段或精确同款数；同款数（跟卖数）仅用 Min/Max。

## 同款数（跟卖数）评估口径

- `similarNum` 对外统一称为“同款数（跟卖数）”，表示销售同一款商品的同行数量。
- 数值越大，同行越多、同质化竞争越强，通常核价通过概率也越低。
- 非工厂型卖家优先选择同款数不超过 10 的商品；超过 20 的候选默认降级或剔除，除非存在明确的价格、渠道、产品差异化或运营优势。
- 将同款数作为重要竞争指标，但同时结合销量及增长、供货价、商品价格、评价、上架时间和卖家自身能力综合判断。

## 响应

成功结构为 `code=0`，`data` 至少包含精确命中数 `total`、`list`、`site`。列表只允许分页访问前 10000 条；`total>10000` 时缩小筛选范围再做完整分布分析。每个商品公开：

- 标识：`id`、`goodsId`、`goodsSn`、`spuId`、`mallId`、`siteId`、`siteUID`、`linkUrl`。
- 基础：`hostingMode`、`thumbnail`、`goodsName`、`catId`、`catIds`、`catItems`。
- 竞争：`similarNum`、`similarNumUpdateTime`。
- 销量：`sold`、`daySold`、`weekSold`、`monthSold`、`totalSold` 及全部对应 Rate。
- 销售额：`sales`、`daySales`、`weekSales`、`monthSales`、`totalSales` 及全部对应 Rate。
- 价格：`minPrice`、`maxPrice`、`supplyPrice`、`minSupplyPrice`、`medianSupplyPrice`、`maxSupplyPrice`。
- 质量与店铺：`goodsScore`、`reviewNum`、`mallOpenTime`、`mallSold`。
- 时间：`onSaleTime`、`createTime`、`updateTime`。

`site` 包含站点名、域名、语言、货币符号、符号位置、汇率和千分位信息。接口不返回收藏等用户私有字段。

## 退出状态

- `0`：查询成功并输出 JSON。
- `2`：需要用户完成登录、额度或开通动作，按暂停流程处理。
- `1`：参数、网络或接口错误，错误 JSON 写入标准错误。
