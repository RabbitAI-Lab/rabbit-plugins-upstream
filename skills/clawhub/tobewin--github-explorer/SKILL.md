---
name: github-explorer
description: Discover and analyze top GitHub open-source projects in any domain via natural language. Search by stars/recency, fetch README, and get plain-language analysis of what a project does and how it helps you. 找 GitHub 优质项目、分析开源仓库。
version: 1.2.0
license: MIT-0
metadata: {"openclaw": {"emoji": "🔍", "requires": {"bins": ["python3"], "env": ["GITHUB_TOKEN"]}, "primaryEnv": "GITHUB_TOKEN", "permissions": [{"name": "cache", "type": "persistence", "path": "~/.cache/github-explorer/"}]}}
---

# GitHub Explorer

用自然语言发现并分析 GitHub 上的优质开源项目。帮用户解决两个痛点：**不知道去哪找**、**看不懂项目是干什么的**。

> ⚠️ **数据外发提醒**：搜索关键词、仓库名会发送至 GitHub API（api.github.com）。GitHub 可能不会返回私密仓库信息。
>
> ⚠️ **限额提醒**：未配置 Token 时 GitHub Search API 每分钟仅 10 次请求；设置 `GITHUB_TOKEN` 环境变量可提升到 30 次/分钟。超过会提示限流。
>
> ⚠️ **缓存持久化**：搜索结果和仓库分析会缓存到 `~/.cache/github-explorer/`（1 小时有效期），加速重复查询。加 `--no-cache` 跳过缓存。

---

## 核心能力

| 能力 | 用户怎么说 | 做什么 |
|------|-----------|--------|
| 🔍 **找项目** | "找一下做 LLM 推理加速的项目" | 调 GitHub 搜索，按 star + 近期活跃过滤，返回 Top 列表 |
| 📖 **析项目** | "帮我看看 langchain 是干啥的" | 拉 README + 元数据，生成结构化分析 |

---

## Triggers

用户明确表达想**找 GitHub 项目**或**了解某个仓库**时触发：

- "找一下做 [领域] 的开源项目" / "有什么好的 [领域] 项目"
- "GitHub 上 [领域] 有哪些优质仓库"
- "帮我看看 [owner/repo] 这个项目" / "[项目名] 是干什么的"
- "新兴的 [领域] 项目有哪些" → 用 trending 模式

**不要触发**：用户只是聊技术话题、提到公司名但不涉及找项目。

> 💡 **自助查参数**：脚本自带 `--help`（如 `search --help`、`analyze --help`），用户也可以直接跑 `help` / `cache status` / `cache clear` 查看或管理缓存。对于复杂的筛选需求，AI 可以直接拼接参数执行。

---

## 行为规则

### 1. 找项目（search）

用户说 "找 LLM 推理加速的项目" / "有什么好的向量数据库"：

```
python3 scripts/github_explorer.py search "<领域关键词>" [--mode classic|trending] [--lang python] [--topic <主题>] [--limit 10] [--stars >1000] [--created-after 2024-01-01] [--created-before 2024-06-01] [--license mit] [--sort stars|forks|updated] [--no-cache]
```

> 💡 **中文自动翻译**：脚本内置中英技术关键词映射表，用户直接说中文也能搜。如 "大模型 推理加速" 自动翻译为 `"large language model inference acceleration"`。不在映射表中的中文词会原样保留传给 GitHub（部分场景仍能匹配）。

- **classic（默认）**：经典优质，按 star 排序 + 近 6 个月有更新
- **trending（启发式）**：新兴热门，按 star 排序 + 近 1 年创建。注意：GitHub 无"涨最快"原生排序，这是"近期创建且已积累高 star"的近似，并非真实增速排名

返回后格式化为排行列表（用**用户的语言**输出）：

```
🔍 [领域] 相关优质项目 (共找到 N 个，显示前 10)

1. owner/repo ⭐ 52.3k
   📝 一句话描述
   🏷️ 语言 · 主题标签
   🔗 https://github.com/owner/repo

2. ...
```

**引导**："要我深入分析其中哪个项目吗？或者换个关键词/模式再搜？"

### 2. 析项目（analyze）

用户说 "帮我看看 langchain-ai/langchain" / "这个仓库是干啥的"：

```
python3 scripts/github_explorer.py analyze <owner/repo> [--readme-full] [--no-cache]
```

> 💡 **桥接规则**：如果用户只给了项目名（如"看看 langchain"）而没有 `owner/repo`，**先跑一次 search 找到精确仓库**，再对搜到的 `full_name` 调 analyze。不要凭猜测拼 owner/repo。
>
> 💡 **README 长度**：默认截断 8000 字符给 LLM 分析，避免溢出上下文。加 `--readme-full` 获取完整 README。

脚本返回结构化 JSON（stars/forks/语言/license/topics/README）。

**你（LLM）负责分析**，输出结构化解读（用**用户的语言**）：

```
📦 owner/repo
⭐ 52.3k · 🍴 8.1k · 🏷️ Python · MIT

一句话定位：
  [用大白话说明这是什么]

核心特点：
  · [特点1]
  · [特点2]
  · [特点3]

能为你做什么：
  · [结合用户语境，说明实际用途]
  · [适用场景]

上手难度：⭐⭐☆☆☆（[简单/中等/偏难]）
```

**分析要点**：
- 从 README + description 提炼"是什么"，避免堆术语
- "能为你做什么"要结合用户刚才提到的需求/领域
- 如果 README 很长，抓核心能力和典型用例

---

## 配置（可选）

```bash
export GITHUB_TOKEN="ghp_你的token"
```

不配置也能用（限流更严格）。Token 在 GitHub → Settings → Developer settings → Personal access tokens 生成，只需 `public_repo` 只读权限。

---

## 命令参考

```
search <query> [--mode classic|trending] [--lang <语言>] [--topic <主题>] [--limit N] [--stars <过滤>] [--created-after <日期>] [--created-before <日期>] [--license <类型>] [--sort stars|forks|updated] [--no-cache]
analyze <owner/repo> [--readme-full] [--no-cache]
cache [status|clear]
help
```

| 参数 | 说明 |
|------|------|
| `--mode` | classic（默认，按 star）/ trending（新兴，近 1 年创建） |
| `--lang` | 限定语言，如 python / rust / go |
| `--topic` | 限定主题标签，如 machine-learning |
| `--limit` | 返回数量，默认 10，最大 30 |
| `--stars` | star 数过滤，如 `>1000` / `>=5000` / `500..1000` |
| `--created-after` | 仓库创建时间下限，如 `2024-01-01` |
| `--created-before` | 仓库创建时间上限，如 `2024-06-01` |
| `--license` | 许可证类型，如 `mit` / `apache-2.0` / `gpl-3.0` |
| `--sort` | 排序字段，`stars`（默认）/ `forks` / `updated` |
| `--no-cache` | 跳过缓存，强制请求 GitHub API |
| `--readme-full` | analyze 专用，获取完整 README（默认截断 8000 字符） |

`cache` 子命令：
| 命令 | 说明 |
|------|------|
| `cache status` | 查看缓存统计（文件数、总大小） |
| `cache clear` | 清空所有本地缓存 |

---

## 错误处理

| 情况 | 怎么说 |
|------|--------|
| API 限流 (rate_limit) | "GitHub API 限流了。设置 GITHUB_TOKEN 可提升限额，或稍后再试。" |
| 仓库不存在 | "找不到这个仓库，确认一下 owner/repo 拼写？" |
| 网络错误 | "网络连接失败，请检查网络后重试。" |
