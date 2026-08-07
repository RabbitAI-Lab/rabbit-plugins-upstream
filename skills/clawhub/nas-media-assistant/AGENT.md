---
name: nas-media-assistant-agent-rules
description: |
  nas-media-assistant 的 Agent 总规则。本文件定义对所有子技能通用的、与具体编排流程无关的
  硬约束：路径认知、操作确认、凭证自检、错误处理。编排流程与意图路由见根 SKILL.md；
  人类向概览见 docs/README.md。
---

# Agent 总规则（nas-media-assistant）

> 本文件定义 nas-media-assistant 的**硬规则唯一权威**。编排器与下游 agent 调用本技能时必须遵守。

## 路径认知规范

> **操作原则**：agent **不硬编码路径** —— 优先 `os.environ[ENV]`，未设则用代码内 fallback 并 `ls` 校验存在且可读/可写。**首次使用须向用户确认路径就位**。

### 核心路径（环境变量 + 读写属性）

| 区域 | 环境变量 | 读写属性 |
| --- | --- | --- |
| 影视库 | `MOVIES_DIR` | 可读写 |
| 迅雷下载暂存 | `XUNLEI_INBOX` | **可读写**（迅雷写入，`media-organizer` MV 迁出后源文件消失） |
| qBittorrent 下载 | `QB_SAVE_PATH` | 可读写 |

> 具体路径值（容器 vs 宿主）与挂载建议见根 SKILL.md 共享配置表 / `docs/README.md` Docker 挂载建议。

### 路径硬规则

- 操作前先 `ls` 父目录确认子目录真实存在；环境变量值同样要先 `ls` 校验
- **不硬编码任何路径** —— 用 `os.environ[ENV]`，fallback 在代码里
- **下载 → 落地下载暂存区 → `media-organizer` 整理 → MV 迁入影视库**；
- 根级目录保护：`电影/` `动漫/` `剧集/` `音乐/` 等分类根目录的创建、重命名、移动、删除**由用户负责**
- 命名规则权威定义在 [`media-organizer/references/naming.md`](./media-organizer/references/naming.md)

## 操作确认规范

- 任何**下载**、**覆盖已有媒体文件**、**跨文件系统移动/删除**、**清理无用文件**的操作，必须先取得用户确认
- 指令已隐含授权（如「下载并整理好」）可视为确认；其他情况先一句话说明将做什么，再执行
- 下载 → 先落地**下载暂存区**（迅雷 → `XUNLEI_INBOX` / qB → `QB_SAVE_PATH`）→ `media-organizer` 整理 → MV 迁入 `MOVIES_DIR`；
- 下载完成后再次确认目标路径与命名，输出整理信息与用户「确认」

## 凭证自检（执行前，模式 0 必跑）

> 编排流程与触发顺序见 [`SKILL.md` § 模式 0 · 首次引导](./SKILL.md)。本段定义**自检本身**的硬规则。

### 触发条件（任一满足即必跑）

1. **新会话首次进入本技能**（`session.metadata['onboarding_state']` 不存在 / `pending` / `failed`）
2. **用户主动要求**（"重新检查环境" / "环境变了" / "再检一次"）
3. **上次自检未通过后用户回应修复**（用户说"装好了"/"搞定了" → 重跑）

### 自检脚本（内联 shell 一把过，不另写文件）

```bash
# 1) TMDB（media-lookup 媒体识别必填,缺则识别链路阻断）
[ -n "${TMDB_API_KEY:-}" ] && echo "✅ TMDB" || echo "❌ TMDB_API_KEY 未设（必填,获取:themoviedb.org/settings/api）"

# 2) 下载器（QB 与迅雷至少一个,缺则检索后无法派发）
[ -n "${QB_URL:-}" ] && echo "✅ qBittorrent $QB_URL" || echo "❌ QB_URL 未设（必填,或 XUNLEI_SSE_URL 二选一）"
[ -n "${XUNLEI_SSE_URL:-}" ] && echo "✅ 迅雷 MCP" || echo "❌ XUNLEI_SSE_URL 未设（必填,或 QB_URL 二选一）"
[ -n "${QB_URL}${XUNLEI_SSE_URL}" ] || echo "❌ QB 与迅雷都未设,无法派发下载"

# 3) 路径（有默认值,未挂载则阻断检索/整理）
for d in "${MOVIES_DIR:-/media/movies}" "${XUNLEI_INBOX:-/media/xunlei-inbox}"; do
  [ -d "$d" ] && echo "✅ $d" || echo "❌ $d 不存在（检查 NAS 挂载）"
done

# 4) Python 依赖（media-search parser 强依赖,缺则整个检索链路挂）
python3 -c "import requests,bs4,lxml" 2>/dev/null && echo "✅ Python 依赖" || echo "❌ 缺 requests/bs4/lxml"
```

### 阻断条件（任一命中即不进模式 1-5,只给修复指引）

| 状态 | 含义 | 后续动作 |
|---|---|---|
| ❌ 下载器全无 | 检索后无法派发 | 阻断,给"二选一"指引(qB WebUI 启用 / 迅雷 Cloud MCP 注册) |
| ❌ 路径不可达 | 整理阶段无法写入 | 阻断,给"检查 Docker 挂载"指引 |
| ❌ Python 依赖缺 | media-search parser 加载失败 | 阻断,给 `apt-get install` 一行命令 |
| ❌ TMDB_API_KEY 未设 | 媒体识别无法工作 | 阻断,给 themoviedb.org 申请指引 |

### 状态缓存（会话级）

- 缓存键：`session.metadata['onboarding_state']`
- 值：`pending` | `passed` | `failed` | `bypassed`
- 通过后**本次会话不再重跑**（除非用户主动触发）
- 自检失败项需用户回应修复 → 重跑全量

> 自检结果按 ❌/⚠️ 项**逐条**报告（不一次性堆 4 段输出）。完整输出模板见下文「§ 首次引导提示模板」。

## 首次引导提示模板（onboarding 失败时输出）

> 模式 0 自检失败时,**严格按下面模板**输出。不要自由发挥,不要把全部 ❌/⚠️ 一次性堆在一条消息里。

### 模板 A:首次自检(无任何历史)

```
⚠️ 环境未就绪,先解决 {N} 项再继续(按优先级,逐条修复):

1. ❌ {缺失项 1} → {一句命令}
   例:Python 依赖 → sudo apt-get install -y python3-requests python3-bs4 python3-lxml
2. ❌ {缺失项 2} → {一句命令}
   例:MOVIES_DIR 不存在 → 检查 /volume1/影视库 是否挂到容器 /media/movies
...

修完跟我说一声,我重跑自检。
```

### 模板 B:用户回应修复后重跑

```
✅ 已重新自检:
- ✅ {已修复项}
- ❌ {仍未修复项} → 再给一次命令
- ⬜ {可选项未设,提醒但不阻断}
```

### 模板 C:全部通过

```
✅ 环境自检通过,链路就绪:
- TMDB:✅
- 下载器:qBittorrent @ http://...
- 路径:/media/movies ✅ /media/xunlei-inbox ✅
- Python 依赖:✅

要查什么?直接说片名即可。
```

### 反例(禁止输出)

- ❌ 把 4 段自检原始 echo 输出**直接复制**给用户(噪音过多)
- ❌ 自检失败后**继续**回答用户的具体查询(应阻断)
- ❌ 只说"环境有问题"不给命令(用户拿到后还要自己查)
- ❌ 自检通过后**每条消息**都重跑自检(应缓存)

---

## 错误处理总则

- 对 caller 的错误返回：统一带 `code` + `msg` 两字段，**不附带原始 stderr 文本**
- 全程保留 `job_id`（内部用），caller 可用于日志关联；不向终端用户直接展示
- 任一阶段失败且无法自动恢复时，给出"可选项"让用户决策（换片名 / 放宽清晰度 / 手动提供链接）

## 对话端点

- 任意**对话端点**（微信/企业微信/Telegram/飞书/Discord/Slack/网页，由 OpenClaw 接入）发来的指令统一经 OpenClaw 路由到本技能
- 本技能不绑定任何单一端点，回报统一走 OpenClaw 注入的当前会话
- 任何一步的最终状态都要回报**原对话端点**（成功摘要 / 失败原因 / 待确认选项）
