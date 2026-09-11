# AliExpress 类目接口

## 子类目列表

运行 `scripts/aliexpress_category_list.py --parent-cat-id <父类目ID> --site-id <站点ID>`。

- 根类目使用 `parentCatId=0`。
- 成功响应包含站点、父类目 ID 和直接子类目数组。
- 类目字段包括 `catId`、`catName`、`catLevel`、`parentCatId` 和 `isLeaf`。

## 类目父链

运行 `scripts/aliexpress_category_info.py --cat-id <类目ID> --site-id <站点ID>`。

成功响应的 `path` 从根类目排列到当前类目。空路径表示该 ID 未在当前类目表中找到，不能自行补齐。

## 类目商品

确认 `catId` 后，用 `scripts/aliexpress_goods_search.py --param siteId=<站点ID> --param catId=<类目ID>` 查询商品样本。

当前类目表本身不带站点字段；请求仍需通过 `siteId` 确认数据站点。跨站点使用前必须重新查询站点并核验类目适用性。
