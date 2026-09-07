# ZY Action Platform API 速查（供脚本 / 通用透传参考）

> 本文件是 `scripts/zy_platform.py` 内置命令与 `request` 通用透传的接口依据。路径默认相对产品 API 根（直连 `http://127.0.0.1:<端口>/api/v1`）。版本会演进，发布包内 `API 接入及测试方法参考.txt` 与 `docs/**` 为更新权威源；两者冲突时以平台实际响应与随包文档为准。

## 0. 通用约定

- **基址**：本机直连 `http://127.0.0.1:18080`~`:18084`（AIP/Foundry/Apollo/Gotham/Swift）；经网关 `http://<host>/<产品前缀>/v1`，前缀 `api`(Foundry)/`aip-api`/`apollo-api`/`gotham-api`/`swift-api`。
- **鉴权**：除 `health` 与登录接口外，均需请求头 `Authorization: Bearer <JWT>`。登录接口：
  - `POST /api/v1/auth/login`，body `{"username":"...","password":"..."}`。
  - 各产品默认播种管理员 `admin/admin1`（可被环境变量覆盖），也支持 `POST /api/v1/auth/register` 自助注册。
  - **响应格式不一致（脚本已自动兼容）**：AIP/Apollo/Gotham/Swift 平铺返回 `{"token": ...}`（Gotham/Swift 另含 `refresh_token`）；Foundry 套信封 `{"code":0,"data":{"token":...}}`。
  - token 缓存于 `~/.workbuddy/zy_action_session.json`，按产品隔离。
- **响应信封**：Foundry/Gotham/Apollo 成功多为 `{"code":0,"message":"ok","data":{...}}`（Apollo 另含 `request_id`）；AIP 的 login/chat/health 多为裸 JSON。`code` 非 0 视为业务失败。
- **HTTP 状态**：401=token 失效/缺失（重新 login）；404=该版本无此路由（先 `request`/读 docs 确认真实路径）；400=参数错；5xx=服务端异常。
- **脚本退出码**：0 成功 / 1 参数或本地错误 / 2 网络不可达或超时 / 3 HTTP 错误(4xx/5xx 且非 401) / 4 鉴权失败(401) / 5 业务信封 code≠0。

## 1. LightAIP（aip，18080）—— 查数与自动化

| 脚本命令 | 方法+路径 | 说明 |
| --- | --- | --- |
| `chat --query "…"` | POST `/chat` | NLQ 自然语言查数。body `{"query":"…"}`。响应含 `intent/confidence/data_source_name/sql_query/query_result{columns,rows}/visualization/fix_attempts/rejected`；`rejected=true` 说明没查成，转述 `message`。 |
| `workflow-list` | GET `/workflows` | 列出自动化/工作流（`?page=&page_size=`）。取 `data` 里各项的 `id`、`name`、`description`。 |
| `workflow-run --workflow-id <id>` | POST `/workflows/{id}/run` | 手动执行一次，同步返回 `data.execution_id`、`status`、`nodes[]`、`outputs`（节点 id → 结果）。可带 `--params '{"区域":"华东"}'`。 |
| `workflow-status --execution-id <eid>` | GET `/workflows/executions/{eid}` | 执行详情：`execution`（status 等）+ `nodes[]`（node_type/status/output/error）。status 常见取值：`pending/running/completed/failed/cancelled`。 |
| `workflow-cancel --execution-id <eid>` | POST `/workflows/executions/{eid}/cancel` | 取消执行。 |
| `datasource-list` | GET `/datasources` | 数据源列表（含演示库）。 |
| `audit-list` | GET `/audit/logs` | 审计日志（管理员）。 |
| `health` | GET `/health` | 公开。`{status,checks:{database,vector,llm_gateway,disk_space}}`。 |

## 2. LightFoundry（foundry，18081）—— 数据/本体/指标

| 脚本命令 | 方法+路径 | 说明 |
| --- | --- | --- |
| `datasource-list` | GET `/datasources` | 数据源列表。 |
| `dataset-list` | GET `/datasets` | 数据集列表（`?status=&limit=`）。 |
| `dataset-preview --dataset-id <id>` | GET `/datasets/{id}/preview?limit=` | 数据集行预览（默认 50，上限 500）。 |
| `ontology-objects` | GET `/ontology/objects` | 本体对象类型列表（order/customer/product…）。 |
| `ontology-search --query "…"` | POST `/ontology/semantic-search` | **推荐**：按业务语义检索本体/指标/对象。body `{"query":"…","limit":10}`。 |
| `metric-list` | GET `/metrics` | 指标列表（另有 `/metrics/catalog`）。 |
| `dashboard-list` | GET `/dashboards` | 看板列表。 |
| `report-list` | GET `/reports` | 报表列表。 |
| （透传可试） | GET `/charts`、`/sync/targets`、`/audit/events`、`/nexus/search?q=` | 视版本存在。 |
| `health` | GET `/health` | 公开 `{status:"ok",service:"zy-action-foundry"}`。 |

## 3. LightGotham（gotham，18083）—— 情报分析

| 脚本命令 | 方法+路径 | 说明 |
| --- | --- | --- |
| `search --query "…" --limit 5` | GET `/search?q=&limit=` | 跨四个数据域（融合实体/图节点/时间轴/地理要素）统一搜索，`data.categories[]`。 |
| `graph-nodes` | GET `/graph/nodes` | 知识图谱节点（ABAC 过滤）。 |
| `graph-stats` | GET `/graph/stats` | 图统计（nodes/edges）。 |
| `entity-list` | GET `/ingestion/entities` | 多源融合实体列表。 |
| `timeline-events` | GET `/timeline/events` | 时间轴事件（可 `?range=`）。 |
| `map-features` | GET `/map/features` | 地图要素（点/面）。 |
| `report-list` | GET `/reports` | 情报报告列表。 |
| `health` | GET `/health` | 公开 `{status:"ok",service:"zy-action-gotham"}`。 |

## 4. LightApollo（apollo，18082）—— 部署平台

| 脚本命令 | 方法+路径 | 说明 |
| --- | --- | --- |
| `apollo-docs` | GET `/docs` | **公开**：返回受保护路由全集（method/path/perm）与公开路由、错误码映射。优先用它对实际版本做自省。 |
| `desired-state-list` | GET `/desired-states` | 期望状态列表。 |
| `deployment-list` | GET `/deployments` | 部署列表。 |
| `deployment-status --deployment-id <id>` | GET `/deployments/{id}` | 部署详情。 |
| `drift-list` | GET `/drift/events` | 漂移事件。 |
| `bundle-list` | GET `/bundles` | bundle 制品列表。 |
| `agent-list` | GET `/agents` | Spoke Agent 节点列表。 |
| `health` | GET `/health` | 公开 `{status:"ok",service:"zy-action-apollo"}`。 |

## 5. LightSwift（swift，18084）

仅健康检查：`GET /health`、`GET /api/health`（公开）。如需验登录态可 `login --product swift`。

## 6. 未内置接口：curl / 透传示例

```
# curl 直连示例（先登录拿 token）：
curl -s -X POST http://127.0.0.1:18080/api/v1/auth/login -H 'Content-Type: application/json' \
  -d '{"username":"admin","password":"admin1"}'

# 通用透传：调 Foundry 指标目录
python3 scripts/zy_platform.py request --product foundry --method GET --path=metrics/catalog
# 透传带 query
python3 scripts/zy_platform.py request --product gotham --method GET --path=search --query-str 'q=%E8%AE%A2%E5%8D%95&limit=3'
# 透传带 body（POST）
python3 scripts/zy_platform.py request --product aip --method POST --path=chat --data '{"query":"各区域销售额Top5"}'
```

> 注意：Windows 的 Git Bash 可能把以 `/` 开头的参数转成路径，故 `--path` 一律**不带前导 `/`**（脚本会自动从 API 根拼接）。
