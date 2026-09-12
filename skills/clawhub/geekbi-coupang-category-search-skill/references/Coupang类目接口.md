# Coupang 类目接口

## 子类目列表

运行：

```bash
python3 scripts/coupang_category_list.py --parent-id 0
```

- `parent-id` 使用 `displayItemCategoryId`，根节点固定为 `0`。
- 返回 `displayItemCategoryId`、`displayItemCategoryCode`、名称和 `isLeaf`。
- `displayItemCategoryId` 用于继续下钻或查询父链；`displayItemCategoryCode` 是展示类目编码，两者不可互换。

## 类目父链

运行：

```bash
python3 scripts/coupang_category_info.py --category-id <displayItemCategoryId>
```

返回从根到目标类目的 `path`。空路径只说明该 ID 未在当前类目服务中找到。

## 用类目筛选商品

类目接口与商品 ES 的字段分工不同：

- 顶级类目：将已确认的 `displayItemCategoryCode` 作为 `rootCategoryCode`。
- 叶子类目：将已确认的 `displayItemCategoryCode` 作为 `leafCategoryCode`。
- 中间类目：先查询父链，将名称以 `>` 连接后作为 `categoryPathPrefix`；路径文字以接口返回为准。
- 已从商品记录取得完整路径时，可用 `categoryPath` 精确匹配。

然后按 [商品接口](Coupang商品接口.md) 运行 `coupang_goods_search.py`。不要把 `displayItemCategoryId` 直接当作商品筛选编码。
