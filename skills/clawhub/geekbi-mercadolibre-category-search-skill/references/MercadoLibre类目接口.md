# Mercado Libre 类目接口

类目接口从当前站点 ES 商品样本中的 `catItems` 构建，只覆盖已收录商品实际出现过的类目路径。

- 子类目：`python3 scripts/mercadolibre_category_list.py --parent-cat-id 0 --site-id 1`
- 类目父链：`python3 scripts/mercadolibre_category_info.py --cat-id <类目ID> --site-id 1`

响应中的 `coverage` 会标明样本口径，`sampleLimit` 是构建类目路径时最多读取的商品文档数。`parentCatId=0` 表示样本根类目。

类目字段：`catId`、`catName`、`catLevel`、`parentCatId`、`isLeaf`。此处 `isLeaf` 表示在已观察路径中没有更深层，不保证是平台官方叶子状态。
