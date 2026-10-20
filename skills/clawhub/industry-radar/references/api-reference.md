# API 参考 — 行业雷达 Industry Radar

服务基地址：`http://127.0.0.1:8000`（以启动器实际 `--host/--port` 为准）
认证方式：除 `/api/login`、`/api/sources`、`/api/config` 外，均需请求头 `Authorization: Bearer <token>`。
交互式文档：`http://127.0.0.1:8000/docs`（FastAPI 自动生成）。

## 认证与系统

### POST /api/login

```bash
curl -s -X POST http://127.0.0.1:8000/api/login \
  -H 'Content-Type: application/json' \
  -d '{"username":"demo","password":"demo"}'
```

响应：

```json
{"token": "a1b2c3...", "username": "demo", "user_id": 1}
```

> Token 存于内存，服务重启后失效，需重新登录。

### GET /api/config（无需认证，可当探活用）

```json
{"llm_enabled": false, "mode": "离线规则引擎（可配置 LLM）", "version": "1.0.0"}
```

### GET /api/sources（无需认证）

返回全部数据源元数据。当前 14 源：

| id            | 名称            | 语言 |
| ------------- | --------------- | ---- |
| 36kr          | 36氪            | zh   |
| ithome        | IT之家          | zh   |
| tmtpost       | 钛媒体          | zh   |
| leiphone      | 雷锋网          | zh   |
| infoq_cn      | InfoQ 中文      | zh   |
| sspai         | 少数派          | zh   |
| oschina       | 开源中国        | zh   |
| solidot       | Solidot 奇客    | zh   |
| zhihu_daily   | 知乎每日精选    | zh   |
| huxiu         | 虎嗅            | zh   |
| jiqizhixin    | 机器之心        | zh   |
| techcrunch    | TechCrunch      | en   |
| verge         | The Verge       | en   |
| ars           | Ars Technica    | en   |

## 订阅管理

### GET /api/subscriptions

响应（每项含 `briefing_count` 统计）：

```json
{"subscriptions": [
  {"id": 1, "user_id": 1, "name": "新能源汽车 × 固态电池",
   "industry_kw": "新能源汽车,汽车", "tech_kw": "固态电池,电池,续航",
   "extra_kw": "量产,车企", "sources_json": "[\"36kr\",\"zhihu_daily\",\"techcrunch\"]",
   "frequency": "weekly", "style": "curated", "enabled": 1,
   "last_run_at": "2026-10-20 16:19:26", "created_at": "...", "briefing_count": 4}
]}
```

### POST /api/subscriptions

```json
{
  "name": "智能眼镜 × 端侧AI",
  "industry_kw": "智能眼镜,AR眼镜",
  "tech_kw": "端侧AI,大模型",
  "extra_kw": "",
  "sources": ["36kr", "ithome", "jiqizhixin"],
  "frequency": "weekly",
  "style": "curated"
}
```

| 字段          | 必填 | 说明                                                        |
| ------------- | ---- | ----------------------------------------------------------- |
| name          | 是   | 订阅名称                                                    |
| industry_kw   | 是   | 行业词，逗号分隔                                            |
| tech_kw       | 是   | 技术词，逗号分隔                                            |
| extra_kw      | 否   | 附加过滤词                                                  |
| sources       | 否   | 数据源 id 数组，空则用默认启用源                            |
| frequency     | 否   | `weekly`（当前仅此值）                                      |
| style         | 否   | `standard` 标准周报 / `curated` 编辑精选（推荐）            |

响应：`{"id": 2, "message": "创建成功"}`

### PUT /api/subscriptions/{sub_id}

Body 传需要修改的字段（同上，均可选，另支持 `enabled` 0/1）。响应：`{"message": "更新成功"}`

### DELETE /api/subscriptions/{sub_id}

响应：`{"message": "已删除"}`。注意：历史简报 `.md` 文件保留在磁盘。

## 生成与预览

### POST /api/subscriptions/{sub_id}/run

同步执行整条流水线（采集→清洗→去重→打分→聚类→摘要→成稿），约 30–120 秒。
HTTP 客户端超时建议 ≥ 180 秒（curl 加 `--max-time 300`）。

```json
{"briefing_id": 5, "title": "智能眼镜 × 端侧AI 行业周报（第 1 期）",
 "stats": {"collected": 62, "deduped": 41, "kept": 12, "clusters": 4},
 "message": "简报生成完成"}
```

> 只补增量：simhash 去重会跳过已入库文章，短时间内重复 run 新文章很少。

### POST /api/preview

与 run 相同流水线但**不落库**，适合试关键词。Body：

```json
{"industry_kw": "人形机器人", "tech_kw": "具身智能", "extra_kw": "", "sources": ["36kr", "jiqizhixin"]}
```

响应：`{"markdown": "# ...", "stats": {...}}`

## 读取与导出

### GET /api/articles?subscription_id=1&limit=100

返回已入库文章（id/title/url/source_name/published_at/summary/score）。

### GET /api/briefings?subscription_id=1

简报列表（不含 md_path）。

### GET /api/briefings/{briefing_id}

单份简报详情，含完整 `markdown` 字段。

### GET /api/briefings/{briefing_id}/export

以 `text/markdown` 附件形式下载（Content-Disposition: briefing_<id>.md）。

### GET /api/trend?subscription_id=1

每期简报的 stats 时间序列 + 各源文章数分布。

### GET /api/dashboard

```json
{"subscription_count": 4, "briefing_count": 16, "article_count": 512, "llm_enabled": false}
```

## 数据落盘位置

| 数据     | 位置                                             |
| -------- | ------------------------------------------------ |
| SQLite   | `app/data/industry_radar.db`（可用 `IR_DB_PATH` 覆盖） |
| 简报 .md | `app/data/briefings/sub<N>_<日期>_<时间>.md`     |

> 数据库删除后下次启动自动重建；简报 .md 不受影响。
