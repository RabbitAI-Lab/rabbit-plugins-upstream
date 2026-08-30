# 操作与字段

所有操作均为平台本地、同步、structured 结果，不需要外部连接或上游调用。平台仍可能因统一任务调度返回 `202`。

## `memory.write`

写入当前用户的一条记忆。

| 字段 | 约束 |
|---|---|
| `type` | 必填：`error`、`correction`、`preference`、`lesson` |
| `scope` | 必填：`global`、`domain:<域名>` 或 `project:<标识>`，最多 80 字节；会转小写 |
| `content` | 必填，最多 1000 字节；不得含秘密或控制字符 |
| `confidence` | 可选，0 至 1，最多四位小数；默认 `0.5000` |
| `metadata` | 可选 JSON object；最多 8 KiB、4 层、64 个键，字符串值最多 1000 字节；不得含秘密 |

同一用户、scope 与规范化内容会安全去重。每个用户最多 1000 条记忆；已达上限时，新内容失败，但重复内容仍可复用。结果关键字段：`memory.id`、`scope`、`type`、`confidence`、`source_memory_ids`、时间字段及 `deduplicated`。审计结果不回显 `content`；搜索结果才包含内容。

## `memory.search`

请求示例：

```json
{"scope":"project:alpha","query":"包管理器","limit":10,"include_archived":false}
```

`query` 必填且最多 1000 字节；`limit` 为 1 至 20，默认 10；`include_archived` 默认 false。请求非 global scope 时，只搜索当前用户的精确 scope 与 `global`，精确 scope 优先；请求 `global` 时只搜索 global。不会搜索其他项目、domain 或用户。结果为 `memories` 与 `candidate_count`。

## `memory.consolidate`

```json
{"scope":"project:alpha","source_memory_ids":[101,102]}
```

`source_memory_ids` 必须含 1 至 10 个正整数 ID。所有来源及其 lineage 必须属于当前用户、同一精确 scope 且未归档；lineage 最多 20 条。跨用户、跨范围、缺失或已归档来源必须停止，不得自动移动或复制。

整理是 `deterministic-local-v1`：不调用 LLM、不执行用户内容；合并唯一内容，生成 `lesson`，取置信度平均值并保留来源 lineage。合并内容仍受 1000 字节和秘密检测限制。结果同写入：`memory` 与 `deduplicated`。

## `memory.archive`

```json
{"memory_ids":[101,102]}
```

每批 1 至 50 个正整数 ID。只归档当前用户拥有的记录；请求中的外部 ID不会泄露其存在性。归档来源会级联归档引用它的派生记忆。归档后默认搜索不可见，但可通过 `include_archived:true` 搜索；平台没有取消归档操作，不声称可恢复。

API 没有预览操作，执行前无法预览完整级联集合。调用前必须让用户确认准确 ID，并明确说明其所有派生记忆可能一并归档；不要声称已列出全部受影响 ID。结果字段为 `archived_count`；新的重复归档逻辑可能为 0，同一幂等键重放则返回原响应。

## `memory.delete`

```json
{"memory_ids":[101,102]}
```

每批 1 至 50 个正整数 ID。调用前必须明确说明记忆主记录的物理删除不可逆，并让用户确认准确 ID。删除只作用于当前用户；另一用户的 ID 不会被删除或暴露。若目标仍被批次外派生记忆引用，操作失败；应让用户决定是否把派生记忆加入同一批次或先删除它，不能擅自扩大删除范围。

`memory.delete` 不清理既有加密任务历史：先前 `memory.write`/`memory.consolidate` 的 request payload，以及先前 `memory.search` 的 result payload，可能按平台保留策略继续存在并可由原任务 GET 返回。不要把删除说成彻底擦除所有副本；用户要求彻底清除历史时，停止并转交平台数据删除流程。

结果字段为 `deleted_count`；使用同一幂等键重放会返回原响应，以新键重新删除已不存在记录才可能返回 0。归档与删除都是免费操作，但仍记录真实计费头。
