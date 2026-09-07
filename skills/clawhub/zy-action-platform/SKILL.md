---
name: zy-action-platform
display_name: ZY AI商业行动平台助手
display_name_en: ZY Action Platform Assistant
description: "Connect and operate ZY Action Platform (AI Business Action System): guide local install & DeepSeek key config, then health-check/login and, across the five products AIP/Foundry/Gotham/Apollo/Swift, run natural-language data queries, list/run automation workflows, query datasets/ontology, search intel, inspect deployments and more."
description_zh: "连接并操作 ZY Action Platform（AI 商业行动系统）：引导本机下载安装与 DeepSeek Key 配置；支持账号登录，并跨 LightAIP/Foundry/Gotham/Apollo/Swift 五个产品完成健康检查、自然语言查数、查看与运行自动化工作流、数据集与本体查询、情报搜索、部署与漂移查看等常用操作。也可按用户给出的安装目录自读官方文档辅助。"
description_en: "Connect ZY Action Platform. Guide install & API key setup, then log in and operate all five products: NLQ data query and workflow automation on AIP, datasets/ontology on Foundry, intel search/graph on Gotham, deployments on Apollo, health on Swift."
category: analytics
version: 1.0.1
author: 展映科技（zyinfo.pro）
allowed-tools: Bash, Read, Grep, Glob
---

# ZY Action Platform 数据与自动化助手

## 一、技能概览与触发词

本技能帮助你使用自研企业数据智能平台 **ZY Action Platform（AI 商业行动系统）**：从"下载安装、填 Key 配置"到"连接登录、查数、跑自动化、查部署/情报"。当用户提到「ZY Action」「AI 商业行动系统」「行动平台」、或表达**查数据/分析、跑自动化/工作流、列数据集/本体/指标、搜情报/实体、看部署状态**等意图，并且语境指向本地已装/要装该平台时，激活本技能。与本平台无关的请求直接说明并终止。

平台包含五个可独立运行的后端产品（本机一键启动后同时运行，默认端口如下）：

| 产品 | 代号 | 端口 | 一句话能力 |
| --- | --- | --- | --- |
| LightAIP | aip | 18080 | NLQ 智能查数、自动化工作流、数据源 |
| LightFoundry | foundry | 18081 | 数据集成、数据集、本体/指标、语义检索 |
| LightApollo | apollo | 18082 | 部署平台：期望状态/部署/漂移/bundle/Spoke |
| LightGotham | gotham | 18083 | 情报分析：搜索/知识图谱/融合实体/时空/报告 |
| LightSwift | swift | 18084 | 星上结算（本技能仅健康检查） |

## 二、运行环境与总则

- 所有平台调用统一通过脚本 `scripts/zy_platform.py` 执行（仅 Python 标准库）。调用格式：`python3 scripts/zy_platform.py <命令> --product <产品> [参数]`；Windows 无 python3 时用 `python`。若脚本不可执行，提示用户环境缺少 Python 3 或路径不对。
- 先执行脚本并读取其 JSON 输出，再向用户做中文摘要；不要凭空编造接口结果。
- `--product` 缺省为 `aip`；产品端口即默认 `--base-url`（`http://127.0.0.1:<端口>`），通常无需传。跨机/经网关访问时再传 `--base-url`（详见第六节）。
- 脚本 stdout 仅输出 JSON；出错信息在 stderr，以 `[zy_platform]` 开头。退出码：0 成功 / 1 参数错 / 2 网络不通或超时 / 3 HTTP 错误 / 4 鉴权失败（401）/ 5 业务失败（信封 code≠0）。先看退出码与提示再决定动作。

## 三、安装与配置引导（用户未装/未启动平台时）

1. **下载**：打开官网下载页 `https://zyinfo.pro/action/`，下载安装包 `https://zyinfo.pro/files/ZY-Action-Platform.rar`（约几百 MB，含全部五个后端 + 前端 + 一键启动器）。
2. **解压**：将 rar 解压到任意目录（Windows，免安装、免 Python/Node/数据库）。解压后根目录含 `运行AI商业行动系统-ZY Action.exe`、`关闭全部服务.bat`、`config.yaml.example`、`.env.example`、`bin/`、`docs/` 等。
3. **填写 API Key（关键，否则查数/检索不可用）**：把根目录的 `config.yaml.example` 复制一份并重命名为 `config.yaml`，用文本编辑器打开，找到 `llm:` 下的 `api_keys:`，把 DeepSeek 的 Key 填到 `deepseek: "sk-..."` 一项；如做 RAG/向量检索再填 `dashscope`。若用户是演示体验且本机未安装 PostgreSQL，请把 `database.type` 从 `"PostgreSQL"` 改为 `"SQLite"`（无 config.yaml 时平台默认就是 SQLite、免数据库）。等效替代：复制 `.env.example` 为 `.env`，填 `DEEPSEEK_API_KEY=sk-...`。
4. **启动**：双击 `运行AI商业行动系统-ZY Action.exe`（或根目录同名 `.bat`）。脚本自动拉起 aip/foundry/apollo/gotham/swift 五个后端与网关并打开浏览器 `http://127.0.0.1/`。等待约 2~5 秒后，用 `health` 子命令验证各产品就绪。
5. **登录账号**：新安装默认内置管理员 `admin / admin1`（建议登录后改密），也可在平台页面自助注册新账号。后续 WorkBuddy 对话中由用户提供其平台账号口令执行登录。
6. **停止**：双击根目录 `关闭全部服务.bat`。

## 四、连接与登录

1. 先运行健康检查确认平台在跑：
   `python3 scripts/zy_platform.py health --product aip`（可对 aip/foundry/apollo/gotham/swift 各跑一次）。
2. 登录并缓存 token（每产品独立缓存；请先征询用户账号，不要假设固定口令）：
   `python3 scripts/zy_platform.py login --product aip --username <用户名> --password <口令>`
   登录成功会把 token 缓存到本机 `~/.workbuddy/zy_action_session.json`（仅用户本机，不随技能上传），之后其余命令自动带 token。
3. 若收到退出码 4 / "鉴权失败(401)"，说明 token 过期，先重新 login 再继续。

## 五、常用操作速查（先对用户确认要做哪类，再选用命令）

- **查数/对话（AIP）**：`chat --product aip --query "<用户原话>"`。NLQ 自然语言→SQL；结果含 `sql_query/query_result/confidence`。用户只要结论时做中文摘要；用户想看明细再展示表格。若报 LLM 相关业务错，提示检查 config.yaml 的 `deepseek` Key 是否填写、平台是否授权。
- **自动化/工作流（AIP）**：先 `workflow-list --product aip` 拿工作流 id 并向用户确认要跑哪个；`workflow-run --product aip --workflow-id <id>`（可选 `--params '{"区域":"华东"}'`）；拿到 `execution_id` 后 `workflow-status --product aip --execution-id <eid>` 轮询汇报（间隔随 status，最长约 60 秒），结束给用户结论与 outputs 摘要；需取消时 `workflow-cancel`。
- **数据源与审计**：`datasource-list --product aip|foundry`；`audit-list --product aip`。
- **Foundry 数据/本体**：`dataset-list`、`dataset-preview --dataset-id <id>`、`ontology-objects`、`ontology-search --query "<业务语义>"`（本体/指标/对象语义检索，最推荐）、`metric-list`、`dashboard-list`、`report-list`。
- **Gotham 情报**：`search --query "<关键词>" --limit 5`（跨图/实体/时间轴/地图统一搜索）、`graph-nodes`、`graph-stats`、`entity-list`、`timeline-events`、`map-features`、`report-list`。
- **Apollo 部署**：`apollo-docs`（可自省全部接口与权限点）、`desired-state-list`、`deployment-list`、`deployment-status --deployment-id <id>`、`drift-list`、`bundle-list`、`agent-list`。
- **Swift**：仅 `health --product swift`。

以上命令均可用 `--pretty` 美化输出；列表类可用 `--page/--page-size/--limit` 控制。

## 六、接口未内置时：通用透传 + 自读官方文档

平台接口随版本演进。两种扩展方式：

1. **通用请求透传**：`python3 scripts/zy_platform.py request --product <产品> --method GET --path=<相对API根的路径> [--query-str 'k=v&k2=v2'] [--data '{"..."}']`
   - `--path` 是相对该产品 API 根（`/api/v1`）的路径且**不要以 `/` 开头**，如 `--path=metrics/catalog?limit=5` 会请求 `<base>/api/v1/metrics/catalog?limit=5`；`--path=health` 打到服务器根 `/health`。body 接口用 `--data` 传 JSON 字符串，如 `--data '{"query":"..."}'`。
2. **按安装目录自读官方文档（推荐先用这个）**：当用户告知平台**解压/安装目录**时（如"装在 D:\zyaction"或"就在下载目录"），用 Read/Grep 阅读该目录内随包的权威资料后再操作，避免臆测接口：
   - 根目录 `README.md`（产品/端口/启动）、`API 接入及测试方法参考.txt`（跨产品接口规范 S01–S12、认证、curl 示例）；
   - `docs/manuals/**`（分析师/管理员/运维/FDE 使用说明）、`docs/ai-action-demo-full.md`、`docs/story/**`（各产品剧情演示，含中文问法与边界陷阱）；
   - `api-demo/sence/*.py`（官方 HTTP 调用示例，`common.py` 含登录封装）；
   - `config.yaml.example`/`.env.example`（确认账号/端口/Key 配置项）。
   读到真实接口细节后，优先复用本脚本已内置命令；确需未内置接口再走通用透传。不要编写或运行会写数据/删数据的高风险操作，除非用户明确要求。

## 七、网关/跨机地址（备用）

默认本机直连端口已够用。若用户在别处访问：`--base-url` 可传网关地址，如 AIP `http://127.0.0.1/aip-api/v1`、Foundry `http://127.0.0.1/api/v1`、Apollo `/apollo-api/v1`、Gotham `/gotham-api/v1`、Swift `/swift-api/v1`（与直连路径等价），或以公网 `https://域名/...` 指向云端实例。传 `--base-url` 后 `health` 会打到该地址的服务器根 `/health`，个别网关形态下 health 不可用属正常，可用 `login`/列表命令间接验证连通。

## 八、安全与边界

- 全程**不在对话中明文展示用户口令**；不把 token/口令写进任何技能文件。token 只存 `~/.workbuddy/zy_action_session.json`。
- 涉及删除、批量写、发布类高风险动作一律先向用户复述确认，无授权不得执行。
- 遇网络错误（退出码 2）提示"确认平台已启动（双击 .exe）且 --product/--base-url 正确"；遇业务错误（退出码 5）把 message 转述给用户；无法判断时如实说明，不编造。
- 本技能只通过 script py 中 调用 REST API 工作。
