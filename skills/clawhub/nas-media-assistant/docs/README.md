# 绿联 NAS 影音管家（nas-media-assistant）

任意**对话端点**（微信/企业微信/Telegram/飞书/Discord/Slack/网页）-> **OpenClaw** ->
本技能包，完成「影视识别 → 资源搜索 → 下载任务 → 文件整理」全生命周期的家庭 NAS 影音助手。

- Agent 编排入口与生命周期见根 [`SKILL.md`](../SKILL.md)
- Agent 总规则（路径/确认硬约束）见根 [`AGENT.md`](../AGENT.md)
- 命名规则权威定义在 [`media-organizer/references/naming.md`](../media-organizer/references/naming.md)

> 场景示例：用户在对话端点发「帮我下载电影功夫」-> 按需识别、多链路检索、按高清优先筛选、派发 qBittorrent/迅雷下载、失败自动换链、下载完归档入库并回报。

---

## 目录结构

```
nas-media-assistant/
├── AGENT.md / SKILL.md / meta.json / docs/README.md
├── references/                         # 根级：routing.md + lifecycle.md
├── media-lookup/                       # TMDB 媒体识别（按需）
│   ├── SKILL.md / tmdb_lookup.py
│   └── references/{design.md, fallback.md}
├── media-search/                       # 网页磁力/种子检索
│   ├── SKILL.md / scripts/
│   └── references/{design.md, search-strategy.md, source-registry.md, quality-scoring.md, source-evaluation.md}
├── downloader-manager/                 # 下载分发、监控与失败重试
│   ├── SKILL.md / scripts/{router, adapters/}
│   └── references/{design.md, routing.md, failure-handling.md}
└── media-organizer/                    # 归档分类、无用清理与迁移
    ├── SKILL.md / scripts/ / data/
    └── references/{design.md, naming.md}
```

---

## 能力概览

| 子技能 | 关键词 | 核心能力 |
|--------|--------|---------|
| media-lookup | 是哪年的/消歧 | TMDB 媒体识别 + 豆瓣 fallback（**按需**） |
| media-search | 搜索/找资源 | 分层 tier1 优先；title_parser；高清优先排序 |
| downloader-manager | 下载/下个 | 迅雷优先 + qB 回退；失败自动换链 |
| media-organizer | 整理/归类/入库 | 离线归档；系列四级检测；规范命名；[信息]三级回退 |

---

## 前置依赖

| 类型 | 配置项 | 说明 |
|------|--------|------|
| **TMDB API** | `TMDB_API_KEY` | **必填（初始化第一步）**，themoviedb.org 免费申请 |
| **迅雷 Cloud MCP** | `XUNLEI_SSE_URL` | **默认优先**，全协议 magnet/ed2k/thunder/http，落 `/media/xunlei-inbox` |
| **qBittorrent** | `QB_URL` / `QB_USER` / `QB_PASS` | 迅雷回退；本地 .torrent 强制；落 `/media/downloads/qBittorrent下载` |
| **OpenClaw** | - | 把目标对话端点接入，并注册本技能包 |

**Docker部署的 Agent 需挂载**：
   - qB下载路径：`/volume1/Downloads/` 挂到容器 `/media/downloads/`
   - 迅雷下载下载路径： `/volume1/迅雷下载` 挂到容器 `/media/xunlei-inbox`
   - 影视目录读写路径：  `/volume1/影视库` 挂到容器  `/media/movies`
---

## 初始化配置方式
1. `media-search/assets/config_template.json` -> 复制为 `config.json`，按需调整启用的源列表
2. `TMDB_API_KEY`（先配）`QB_*` `XUNLEI_SSE_URL`（后配）由 agent 在用户首次调用时声明并注入环境变量，后续复用，不逐次索取
> 完整变量表 / 协议路由 / 失败码详见各子技能 `SKILL.md` / `references/`。

---

## 端到端示例

```
对话端点：帮我下载电影功夫
  |
  +- ① media-search -> 多链路并行召回 + title_parser 解析 -> 过滤枪版 -> 高清优先排序
  |     -> 顶层命中即下，携带归一化元数据
  |
  +- ② downloader-manager -> 迅雷会员优先派发；不可用/慢速回退 qBittorrent -> 监控
  |     +- 成功 -> 完成事件（含 file_path + metadata 回传）
  |     +- 失败(死链) -> 回报 DL_DEAD + 回 ① 取下一候选（最多 3 次）
  |
  +- ③ media-organizer -> 识别主 mkv -> 系列四级检测（疑似衍生剧未确认则 pending_lookup）
        -> [信息]标签提取 -> 清理无用 -> 迁移到 /media/movies/电影/功夫 (2004)/
        -> 触发 Emby 刷新 -> 回报「已入库」
```

> media-lookup **按需**触发：片名清晰可跳过；title_parser 也能从结果文件名补年份/清晰度/编码。

---

