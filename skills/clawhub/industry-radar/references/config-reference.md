# 配置参考 — 行业雷达 Industry Radar

全部配置走环境变量，启动时读取（改配置需重启服务）。导出示例：

```bash
export IR_LLM_BASE_URL="https://api.example.com/v1"
export IR_LLM_API_KEY="sk-xxxx"
python3 scripts/run_local.py
```

## LLM（可选 — 不配置自动降级为规则引擎）

| 变量             | 默认          | 说明                                                        |
| ---------------- | ------------- | ----------------------------------------------------------- |
| IR_LLM_BASE_URL  | `""`          | OpenAI 兼容网关地址，如华为云 ModelArts Studio 推理服务端点 |
| IR_LLM_API_KEY   | `""`          | API Key。**只通过环境变量注入，绝不写入文件或代码**         |
| IR_LLM_MODEL     | `deepseek-chat` | 模型名，按网关实际支持填写                                |
| IR_LLM_TIMEOUT   | `60`          | 单次 LLM 请求超时（秒）                                     |

两者（BASE_URL + API_KEY）同时非空才启用在线 LLM；`GET /api/config` 可查看当前模式。

## 采集

| 变量                    | 默认值 | 说明                             |
| ----------------------- | ------ | -------------------------------- |
| IR_HTTP_TIMEOUT         | `15`   | 单源 HTTP 超时（秒）             |
| IR_USER_AGENT           | Mozilla/5.0 (compatible; IndustryRadar/1.0; +weekly-briefing) | 抓取 UA |
| IR_MAX_PER_SOURCE       | `15`   | 每源单次最多采集条数             |
| IR_FETCH_FULLTEXT       | `1`    | `1`=抓取全文（摘要质量更高但更慢），`0`=仅用 RSS 摘要 |

## 生成策略

| 变量                  | 默认值 | 说明                                         |
| --------------------- | ------ | -------------------------------------------- |
| IR_TOP_K              | `12`   | 每份简报纳入的文章上限                       |
| IR_CLUSTER_THRESHOLD  | `0.18` | token Jaccard 聚类兜底阈值                   |
| IR_MAX_SECTIONS       | `5`    | 简报板块数上限（超出合并进「其他动态」）     |
| IR_DEDUP_HAMMING      | `3`    | simhash 汉明距离去重阈值                     |
| IR_CURATED_PICKS      | `5`    | 编辑精选模式下每期精选的文章条数             |

## 路径与演示账号

| 变量        | 默认值                        | 说明                 |
| ----------- | ----------------------------- | -------------------- |
| IR_DATA_DIR | `app/data`                    | 数据目录             |
| IR_DB_PATH  | `app/data/industry_radar.db`  | SQLite 文件路径      |
| IR_DEMO_USER | `demo`                       | 演示账号用户名       |
| IR_DEMO_PASS | `demo`                       | 演示账号密码         |

> 演示会话机制为演示级（内存 Token），生产使用请自行替换为 JWT + 存储。
