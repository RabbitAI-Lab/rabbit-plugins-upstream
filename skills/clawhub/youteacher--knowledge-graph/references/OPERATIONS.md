# 操作、字段与结果

所有操作均为本地、同步、structured 结果；请求 JSON 总大小不超过 32 KiB。

## `entity.upsert`

字段：`type`、`external_key`、`name` 必填，`properties` 可选 JSON object。

- `type` 只能是 `company`、`person`、`product`、`project`、`component`、`concept`、`document`、`event`、`organization`、`location`、`technology`。
- `external_key` 最多 256 字节，`name` 最多 200 字节；二者不得含秘密。
- `properties` 最多 1 KiB、3 层、32 个键；键最多 64 字节，字符串值最多 256 字节，禁止敏感键和值。
- 当前用户最多 1000 个实体；同一用户、type 与 external_key 会 upsert 并返回 `deduplicated:true`。

结果为 `entity` 与 `deduplicated`。entity 含 `id`、`type`、`external_key`、`name`、`properties`、`verification`、`source_ids` 和时间字段。

## `relation.upsert`

```json
{"from_entity_id":101,"predicate":"depends_on","to_entity_id":102,"properties":{}}
```

两个端点必须是当前用户拥有的不同实体。`predicate` 只能是 `depends_on`、`parent_of`、`part_of`、`works_with`、`related_to`、`owns`、`uses`、`mentions`、`supports`、`located_in`。所有 predicate 禁止自环；`depends_on`、`parent_of`、`part_of` 分别按同一 predicate 检查并拒绝有向环，其他 predicate 可以形成非自环环路。不要用改名 predicate 绕过语义约束。

关系 properties 边界同实体。每用户最多 2000 条关系。结果为 `relation` 与 `deduplicated`；relation 含 `from_entity_id`、`predicate`、`to_entity_id`、`verification` 与 `source_ids`。

## `graph.query`

```json
{"seed_entity_id":101,"depth":2,"max_entities":20,"direction":"outgoing","predicates":["depends_on"]}
```

- `seed_entity_id` 是当前用户拥有的单个实体 ID（必填）。
- `depth` 为 0 至 4，默认 1；`max_entities` 为 1 至 500，默认 20。
- `direction` 为 `outgoing`、`incoming`、`both`，默认 both。
- `predicates` 可选，最多 10 个允许的 predicate；省略或空数组表示不筛选。

查询最多输出 20 条关系与 40 个来源；超过预算时整个请求失败并要求缩小范围，不截断。最终编码必须低于 60 KiB。结果为 `query`、`entities`、`relations`、`sources`，只含当前用户数据。

## `source.attach`

字段：`target_type` 为 `entity` 或 `relation`；`target_id` 必须属于当前用户；`source_url` 为无 userinfo 的 HTTPS URL（必填）。

- `source_url` 最多 512 字节，必须是无 userinfo 的 HTTPS URL。平台只保存它，不抓取、不解析、不验证可达性或内容真伪。
- 每用户最多 4000 个来源；重复 fingerprint 安全复用，不更新既有来源。

结果为 `source` 与 `deduplicated`。source 固定带 `source_kind:user_supplied`，并返回目标、URL 和 created_at。

## `graph.summarize`

请求字段与 `graph.query` 完全相同，不接受 snapshot ID、任意正文或自定义 prompt。平台从实时限定子图生成固定模板 `claims`，不调用 LLM。每条 claim 含 `verification`、`entity_ids`、`relation_ids`、`source_ids`；同时返回规范化 `query`。没有关系时才为实体生成 claim。
