# SHEIN 店铺搜索接口

## 调用

```bash
python3 scripts/shein_shop_search.py \
  --param siteId=1 \
  --param catIds=123 \
  --param hostingMode=2 \
  --param sort=mallSold \
  --param order=desc \
  --param page=1 \
  --param size=20
```

基础参数：`keyword`、可重复 `catIds`、`siteId`、`hostingMode`（1 全托管、2 半托管）、`page`、`size`、`sort`、`order`。未指定用入口 1（名称“全部”，当前映射 `us`，不是跨站聚合），明确美国用 2，其他站点先运行 `shein_site_list.py`。

以下指标均可使用 Min/Max：

- 近 3 个月与累计规模：`mallSold`、`mallSales`、`totalSold`、`totalSales`；另有 `mallStar`、`reviewNum`、`goodsNum`、`followerNum`、`avgPrice`。
- 周期经营：日/周/月均 `Sold`、`Sales` 及对应 Rate。
- 商品供给：日/周/月均 `ItemCount` 及对应 Rate。
- 粉丝规模：日/周/月均 `Follower` 及对应 Rate。
- 时间：`mallOpenTimeMin/Max`，使用 ISO 8601。

可排序字段为以上指标、`mallOpenTime`、`createTime`、`updateTime`。方向只允许小写 `asc|desc`，每页最大 200，`page × size` 不得超过 10000，所有范围必须有效。`total` 是精确命中数；命中超过 10000 时只能访问前 10000 条，应缩小筛选范围后再做完整分布分析。

## 响应字段

成功响应 `data` 包含 `total`、`list`、`site`。店铺项公开：

- `id`、`mallId`、`siteId`、`siteUID`、`linkUrl`、`hostingMode`。
- `mallLogo`、`mallName`、`descriptions`、`catIds`、`catItems`。
- `mallStar`、`reviewNum`、`goodsNum`、`followerNum`。
- `mallSold`、`mallSales`、`totalSold`、`totalSales`、`avgPrice`。
- 日/周/月均销量、销售额、商品数、粉丝数及全部对应 Rate。
- `mallOpenTime`、`createTime`、`updateTime`。

不返回收藏、备注等用户私有字段。退出状态：成功 0，需要动作 2，错误 1。
