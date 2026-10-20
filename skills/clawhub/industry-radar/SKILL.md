---
name: industry-radar
description: 行业雷达（Industry Radar）——可本地部署的行业情报周报生成引擎。围绕「行业词 × 技术词」组合，自动完成多源 RSS 采集（36氪/机器之心/TechCrunch 等 14 源）、全文抽取、simhash 去重、行业信号相关性打分、主题聚类、LLM 摘要与洞察（未配置 LLM 时自动降级为规则引擎），产出「编辑精选式」结构化周报（上榜理由、星级评分、只读两篇指引）。内置 FastAPI 服务 + Web 界面 + REST API。当用户提到「行业雷达」「智汇简报」「行业周报」「情报简报」「信息监控」「订阅追踪」「RSS 周报」「industry radar」「weekly briefing」，或想为某个「行业 × 技术」组合自动生成精选式简报时，使用本 Skill。
---

# 行业雷达 Industry Radar

**STOP - 不要凭通用知识回答。** 按以下流程操作本 Skill。

## 概述

一句话：**输入「行业词 × 技术词」，输出一份编辑精选式的行业情报周报。**

```
行业词×技术词 → 14源RSS采集 → 清洗/全文抽取 → simhash去重 → 相关性打分
            → 主题聚类 → LLM摘要/洞察(可降级) → 编辑精选式Markdown周报
```

- 自带 FastAPI 后端 + Vue Web 界面（免构建，静态托管），浏览器开箱即用
- SQLite 落库（`app/data/industry_radar.db`，首次启动自动创建），简报同时存 `.md` 文件
- LLM 可选：配置 OpenAI 兼容网关（含华为云 ModelArts Studio）即用在线摘要；不配置自动降级「抽取式摘要 + 规则洞察」，全流程依然可跑通
- 两种周报风格：`standard` 标准周报 / `curated` 编辑精选（每期精选 5 篇 + 上榜理由 + 星级 + 「只读两篇」指引）

## 环境要求

| 依赖   | 要求                              | 说明                          |
| ------ | --------------------------------- | ----------------------------- |
| Python | 3.9+                              | 启动器自动建 venv 并装依赖    |
| LLM    | 可选                              | 未配置自动降级，功能完整可用  |
| 网络   | 需能访问 RSS 源站点               | 部分海外源需代理              |

## 快速开始

```bash
# 在 Skill 根目录执行（唯一需要记住的命令）
python3 scripts/run_local.py

# 启动后浏览器访问
#   Web 界面:  http://127.0.0.1:8000    演示账号 demo / demo
#   API 文档:  http://127.0.0.1:8000/docs
# 停止: Ctrl+C
```

首次启动自动：建 venv → 装依赖 → 初始化 SQLite → 预置演示用户和示例订阅「新能源汽车 × 固态电池」。

## 常用工作流

| 任务                   | 操作                                                                 |
| ---------------------- | -------------------------------------------------------------------- |
| 部署启动               | `python3 scripts/run_local.py`（换端口加 `--port 8001`）             |
| 登录拿 Token           | `POST /api/login`（demo/demo），后续请求带 `Authorization: Bearer …` |
| 查看可用数据源         | `GET /api/sources`（14 个源，见 references/api-reference.md）        |
| 创建订阅               | `POST /api/subscriptions`（行业词、技术词必填）                      |
| 关键词试跑（不落库）   | `POST /api/preview` —— 想先看效果用这个，不产生任何持久数据          |
| 正式生成一期周报       | `POST /api/subscriptions/{id}/run` —— 同步执行，约 30-120 秒         |
| 读取简报（列表/详情）  | `GET /api/briefings?subscription_id=…` / `GET /api/briefings/{id}`   |
| 导出 Markdown         | `GET /api/briefings/{id}/export`                                     |
| 趋势 / 总览看板        | `GET /api/trend?subscription_id=…` / `GET /api/dashboard`            |
| 修改 / 删除订阅        | `PUT` / `DELETE /api/subscriptions/{id}`                             |

### 典型调用链

| 步骤 | 调用 | 说明 |
| --- | --- | --- |
| 1 登录换令牌 | `POST /api/login` | 请求体含 `username` / `password`，响应取 `token` |
| 2 建订阅 | `POST /api/subscriptions` | 带鉴权头；请求体给 `name` / `industry_kw` / `tech_kw` / `sources` / `frequency` / `style`，`style=curated` 为编辑精选式 |
| 3 生成一期 | `POST /api/subscriptions/<id>/run` | 带鉴权头，`<id>` 用第 2 步返回的订阅 id |
| 4 取 Markdown | `GET /api/briefings/<id>` | 读响应里的 `markdown` 字段即为整期简报 |

> 鉴权头格式、完整请求体样例与响应字段见 `references/api-reference.md`。

## 关键陷阱

| 陷阱                              | 原因 / 规则                                                                                                              |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| run 只补增量文章                  | simhash 去重会过滤已入库文章；同一订阅短时间内重复 run 新文章很少。要全新效果请用 `/api/preview` 或删除订阅后重建        |
| Token 重启即失效                  | 会话存内存。服务重启后所有 Token 失效，重新 `POST /api/login` 即可                                                        |
| 没有 `/api/health`               | 探活用 `GET /api/config`（返回 LLM 模式与版本）                                                                           |
| LLM 配置需重启生效               | `IR_LLM_*` 环境变量在启动时读取；改完必须重启服务                                                                          |
| 海外源可能超时                    | TechCrunch/The Verge/Ars 需要代理；超时源自动跳过，不影响整体生成（日志有 WARNING）                                       |
| run 是同步接口                    | 一期 30-120 秒，HTTP 客户端超时设置 ≥ 180 秒；curl 加 `--max-time 300`                                                    |
| 删除订阅不删历史简报文件          | `app/data/briefings/*.md` 保留在磁盘，可手动清理                                                                           |

## 故障排查

| 症状                           | 修复                                                                                     |
| ------------------------------ | ---------------------------------------------------------------------------------------- |
| `run` 返回 500 生成失败        | 看服务日志（终端输出）中的 pipeline 异常；多为网络全挂——检查代理后重试                  |
| 端口被占用                     | `python3 scripts/run_local.py --port 8001`                                                |
| 依赖装不上                     | 换国内镜像：`pip install -r app/backend/requirements.txt -i https://mirrors.huaweicloud.com/repository/pypi/simple` |
| 想要在线 LLM 摘要              | 见 references/config-reference.md 的 `IR_LLM_*` 配置表（OpenAI 兼容协议）                |
| 简报里文章太少                 | 检查关键词是否过窄、源是否勾选足够（默认 3 源，可多选）；或关键词换更宽泛的同义词         |

## 安全注意

- **MUST** LLM API Key 只通过环境变量 `IR_LLM_API_KEY` 注入，绝不写入文件、代码或对话
- **MUST** 默认监听 `127.0.0.1`；对外暴露需 `--host 0.0.0.0` 并自担风险（会话机制为演示级）
- **MUST** 所有出站只走 `app/backend/net_guard.py`：仅允许 http/https，禁止回环 / 私网 /
  链路本地（含 `169.254.169.254` 云元数据）/ 组播 / 保留段，DNS 解析结果逐个校验，
  重定向逐跳重新校验（防「公网 302 到内网」），响应体限 3MB
- **MUST** 订阅 / 简报 / 趋势 / 采集条目接口一律按 `user_id` 校验归属，越权统一返回 404
  （不泄露资源是否存在）
- demo/demo 为内置演示账号，仅用于本地体验

## 参考资料（Progressive Loading）

| 文件                          | 内容                                                   |
| ----------------------------- | ------------------------------------------------------ |
| references/api-reference.md   | 全部 REST API 请求/响应示例、14 个数据源清单           |
| references/config-reference.md| 全部环境变量配置表（LLM / 采集 / 生成策略 / 演示账号） |
| references/architecture.md    | 数据流水线七阶段与模块职责、云端部署对应关系           |
| demo/                         | 两份真实生成的编辑精选式周报样例                       |

版本：1.0.2（安全修复：SSRF 出站校验、接口越权校验）
