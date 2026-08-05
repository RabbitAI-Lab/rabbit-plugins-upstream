---
name: nas-media-assistant
description: |
  绿联 NAS 智能影视助手 -- 面向家庭 NAS 的「对话式」影视全生命周期管理总控技能。
  角色与规则：影视识别 -> 网页磁力/种子检索 -> 下载任务 -> 文件整理。
  当用户经任意对话端点（微信/企业微信/Telegram/飞书/Discord/Slack/网页等，由 OpenClaw
  接入）发出搜索、下载、整理影视资源的指令时触发,例如"帮我下载电影功夫"、"下个权游 S03 1080p"。
  首次使用需先完成环境自检（模式 0 首次引导）,通过后才进入正常检索/下载/整理模式。
homepage: https://www.skillhub.cn/skills/user_2645d56b/nas-media-assistant
metadata:
  openclaw:
    emoji: 🎬
    requires:
      binaries: [node, python3, curl]
    primaryEnv: QB_URL
  security:
    credentials_usage: |
      检索为直连公开资源站抓取（media-search），不依赖第三方密钥。
      下载请求仅发往用户自有下载客户端（qBittorrent WebUI / 迅雷 Cloud MCP）。凭证不离开本地/局域网。
      对话端点消息经 OpenClaw 连接器接入，会话身份由 OpenClaw 托管，本技能不直接持有端点凭证。
    allowed_domains:
      - '*.local'
      - '*.lan'
      - '*.xunlei.com'
---

# 绿联 NAS 智能影视助手（nas-media-assistant）
**版本**：2.1.2

**角色**：绿联 NAS 智能影视助手 Agent，管理家庭 NAS 影视全生命周期（识别→搜索→下载→整理）。
本文件是技能包的**编排入口**，含生命周期主线、6 模式速查表（含模式 0 首次引导）、意图路由表与共享配置。

> **Agent 总规则**（路径/确认/凭证/错误/端点）见 [`AGENT.md`](./AGENT.md)，**所有操作前必读**。
> 模式判定详情、路由子技能传参见 [`references/routing.md`](./references/routing.md)。
> 5 阶段流程图长版（异常分支/重试/状态机）见 [`references/lifecycle.md`](./references/lifecycle.md)。
> 人类向概览与前置依赖见 [`docs/README.md`](./docs/README.md)。

---

## 模式 0 · 首次引导（onboarding，新会话 / 首次触发）

> **优先级最高**：任何用户消息进入时，**先判断会话是否已 onboarded**。未 onboarded → 先跑模式 0 引导；onboarded → 直接进模式 1-5。

### 触发条件（任一满足即触发）

1. **新会话开始**（OpenClaw 注入的会话 ID 之前未见过本技能）
2. **首次触发本技能**（该 agent 上 nas-media-assistant 首次被调用）
3. **上次自检未通过**（会话级缓存 `onboarding_state: failed`）
4. **用户主动要求**（"重新检查环境" / "环境变了" / "再检一次"）

### 引导动作（4 步，按序执行，失败即停）

1. **凭证自检**：跑 `AGENT.md`「凭证自检」段的 4 段内联 shell（TMDB / 下载器 / 路径 / Python 依赖）
2. **结果归类**：
   - 全部 ✅ → 写 `onboarding_state: passed` → 进入模式 1-5 判定
   - 有 ❌/⚠️ → 写 `onboarding_state: failed` → 走"修复指引卡片"（模板见 `AGENT.md` § 首次引导提示模板）
3. **修复指引卡片**：按 ❌ 项**逐条**给命令（不一次性堆），结尾说"修完跟我说一声，我重跑自检"
4. **不进模式 1-5**：自检未通过时**不响应具体查询**，只给修复指引

### 状态缓存（会话级）

- `onboarding_state`：`pending`（默认）| `passed` | `failed`
- 缓存到 OpenClaw 会话 metadata（`session.metadata['onboarding_state']`）
- 自检通过后**本次会话不再重跑**（除非用户说"重新检查"）
- 新会话自动重置为 `pending`

### 旁路：人工跳过

用户可说"先别管环境，先帮我查火遮眼" → agent 把 `onboarding_state` 标为 `bypassed`（会话级），进入模式 1-5 但**仍要在结果里提示**哪些项缺失。

任意**对话端点**（用户消息）-> **OpenClaw**（连接器 + LLM 编排）-> 本技能 -> 子技能协作完成
「影视识别 → 资源搜索 → 下载任务 → 文件整理」全生命周期，并把结果回报到原对话端点。

典型指令：`帮我下载电影功夫` / `下个权力的游戏 S03 1080p 双语` / `找部 4K 的盗梦空间，要 Remux`。

---

## 全生命周期（5 阶段，主线）

```
用户需求
  │
  ▼ ① 查询归一化 + 按需识别         → media-lookup（按需触发）
  ▼ ② 多链路检索（并行 + 合并 + 评分）  → media-search
  ▼ ③ 下载任务（派发 · 监控 · 换链） → downloader-manager
  ▼ ④ 文件整理（分类 · 命名 · 迁移） → media-organizer
  ▼
回报对话端点：「✅ 已入库：功夫 (2004) -> /media/movies/电影/功夫 (2004)/功夫 (2004)[信息].mkv」
```

> **异常分支**（候选稀薄/同名多义/死链换链/衍生剧 pending_lookup/失败码处置）见 [`references/lifecycle.md`](./references/lifecycle.md)。

---

## 6 模式速查表（编排器从用户原话判定进入哪个模式）

> **模式 0 先于 1-5**：每次用户消息先按"模式 0 · 首次引导"判定，未 onboarded → 先走模式 0。onboarded → 按下表**自上而下匹配，命中即停**：

| # | 触发条件 | 模式 | 后续动作 |
|---|---|---|---|
| 0 | 会话未 onboarded（或 `onboarding_state=failed`） | **首次引导** | 跑凭证自检 → 全部 ✅ 才放行，否则只给修复指引卡片（不响应具体查询） |
| 1 | 含「下/下载/搞个/帮我下 + 片名」 | **下载模式** | 顶层候选命中即下，不列列表 |
| 2 | 含「查/检索/找/搜 + 片名」 | **检索模式** | 呈现带号列表等用户选号 |
| 3 | 含数字编号（1/2/3 / 第一个/三） | **选号续派** | 回查会话 `candidates[N]` 派发 |
| 4 | 含「整理/归类/入库/归档/规范」 | **整理模式** | 调 `media-organizer`（预演 → 确认 → `--commit`） |
| 5 | 其它 / 不明 | 引导用户明确意图 | 列出可选模式让用户选 |

> 判定流程与边界 case 见 [`references/routing.md §一`](./references/routing.md)。

---

## 意图路由表

| 用户意图 | 路由到 |
| --- | --- |
| 识别/消歧/补全元数据 | `media-lookup`（按需） |
| 检索模式跑出列表 | `media-search` |
| 下载模式 / 选号续派 | `media-search` → `downloader-manager` |
| 下载任务卡住/失败/换链 | `downloader-manager`（已派发任务） |
| 整理/归类/入库 | `media-organizer` |
| 跨阶段（识别→搜→下→整理） | 依次读取各子技能 SKILL.md |

> 路由子技能时的传参约定、契约、跨链路衔接见 [`references/routing.md §二`](./references/routing.md)。

---

## 共享配置（关键环境变量）

| 变量 | 用途 | 宿主默认路径（容器路径） | 获取 / 启用方式 | 必填 |
| --- | --- | --- | --- | --- |
| `XUNLEI_SSE_URL` | 迅雷 Cloud MCP（默认优先下载器，全协议） | - | 迅雷云盘网页 → 设置 → Cloud MCP 启用,复制 SSE 连接串 | 与 `QB_URL` 至少其一 |
| `QB_URL` / `QB_USER` / `QB_PASS` | qBittorrent WebUI（迅雷回退；本地 .torrent 强制） | `QB_SAVE_PATH` 默认 `/volume1/Downloads/qBittorrent下载`（`/media/downloads/qBittorrent下载`） | qB WebUI → 设置 → WebUI → 启用 + 设端口 + 反代；`admin/adminadmin` 是默认 | 配 qB 时必填 |
| `MOVIES_DIR` | 影音库路径 | `/volume1/影视库`（`/media/movies`） | NAS 上任意有读写权限的目录 | 是 |
| `XUNLEI_INBOX` | 迅雷下载暂存 | `/volume1/迅雷下载`（`/media/xunlei-inbox`） | NAS 上给迅雷客户端用的下载目录 | 是 |
| `TMDB_API_KEY` | media-lookup 媒体识别 | - | [themoviedb.org/settings/api](https://www.themoviedb.org/settings/api) 申请,免费 | 是 |
| `DEFAULT_QUALITY` / `PREFERRED_CODEC` / `PREFERRED_LANG` | 默认偏好 | - | 可选,默认 1080p / x265 / 双语 | 否 |

> **Agent 总规则**（路径 `ls` 校验 / 操作确认 / 凭证自检 / 错误处理 / 对话端点）见 [`AGENT.md`](./AGENT.md)。

---

## 子技能文件索引

- `media-lookup/SKILL.md` - TMDB 媒体识别（按需；自动豆瓣 fallback）
- `media-search/SKILL.md` - 网页磁力/种子检索与筛选（tier1 优先）
- `downloader-manager/SKILL.md` - 下载分发、监控与失败重试（迅雷优先 + qB 回退）
- `media-organizer/SKILL.md` - 下载后归档分类、无用清理与迁移

> 每个子技能以独立目录承载；目录内 `SKILL.md` 为 Agent 操作手册，`references/design.md` 为架构/技术细节（开发者参考）。`media-search` / `media-organizer` 另含 `scripts/` 与 `references/`（策略/账本/评分）。`media-lookup` 为轻量插件（`SKILL.md` + `tmdb_lookup.py`）。根 `SKILL.md` 为编排入口，`AGENT.md` 为总规则，`docs/README.md` 为人类向概览。
