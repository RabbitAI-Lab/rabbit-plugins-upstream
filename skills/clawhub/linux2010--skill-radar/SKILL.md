---
name: skill-radar
description: 多源技能扫描雷达 — 从 skills.sh、GitHub 和本地聚合搜索技能，语义理解 + 关键词优化，带质量验证和风险提示。当用户说"找个 xxx 技能""有没有 xxx 的 skill""find a skill for X"时触发，或 Agent 遇到不熟悉任务、缺少合适工具时主动调用。
trigger: skill-radar, 技能雷达, find skill, 找技能, 搜索技能, skill search
auto: true
priority: 80
license: MIT
metadata:
  author: hope
  version: 1.0.0
  created: 2026-07-26
  review_interval_days: 30
tags:
  - skill-discovery
  - search
  - agent-tools
  - installation
---

# Skill Radar — 技能雷达

多源聚合 + 语义优先 + 质量验证 + 智能触发。

## 触发条件（双触发）

1. **用户主动**: "找个 xxx 技能"、"有没有 xxx 的 skill"、"find a skill for X"、"搜索技能"
2. **Agent 自主**: 遇到不熟悉任务、多次尝试未解决、缺少合适工具时，可主动触发本技能搜索外部帮助

## 工作流（5 步）

### Step 1: 意图理解 + 关键词提取

先从用户需求中提取搜索关键词：

**去停用词** — 去掉: how, do, I, can, you, help, me, want, need, a, an, the, is, are, for, to, of, 帮, 我, 一个, 怎么, 如何

**保留两类词**:
- 领域词: react, go, python, docker, kubernetes, kafka, nextjs, typescript, css, tailwind, design, testing, deploy, security, database, api, graphql
- 动作词: deploy, test, monitor, review, lint, build, debug, refactor, generate, analyze, scan, migrate, backup, optimize

**提取规则**:
- 2-4 个关键词最佳
- 全小写
- 准备 2-3 组同义词变体备用

### Step 2: 三源并行搜索

按优先级并行搜索三个来源：

#### 2a. 本地优先 — 检查已安装

检查以下目录中是否已有匹配的技能：
```bash
ls ~/.agents/skills/*/SKILL.md 2>/dev/null && ls */references/*/SKILL.md 2>/dev/null
```

如果本地已有匹配技能，先告知用户，避免重复安装。

#### 2b. skills.sh 搜索 — 官方生态（主力）

```bash
npx -y skills@latest find <keywords> -y 2>&1
```

优点：安装量数据最全、来源可追溯。

#### 2c. GitHub 搜索 — 发现未上架技能（补充）

```bash
gh search repos "<keywords> skill claude" --sort stars --limit 10 2>/dev/null
```

当 skills.sh 结果不足或想找更新鲜的技能时使用。

### Step 3: 质量验证

对搜索结果逐一验证：

| 维度 | 规则 | 阈值 |
|------|------|------|
| 安装量 | 优先推荐高安装量 | 1K+ 优先，<100 谨慎标记 |
| 来源声誉 | 官方/知名来源优先 | vercel-labs, anthropics, microsoft 等可信 |
| GitHub Stars | 检查源仓库活跃度 | <100 需标注"新技能/低活跃" |
| 更新时间 | 避免推荐已废弃技能 | 超过 1 年未更新需标注 |
| 依赖风险 | 检查是否需要外部 API/服务 | 标注"需 API key"等依赖 |

**风险标记**:
- `[需 API Key]` — 需要第三方 API 密钥
- `[低活跃]` — Stars <100 或超过 1 年未更新
- `[仅 Mac]` / `[仅 Linux]` — 平台限制

### Step 4: 排序推荐

按以下权重综合排序后输出 TOP 5：

1. 相关性（与用户需求匹配度）
2. 安装量 / Stars
3. 来源声誉
4. 更新活跃度

**输出格式（严格参照）**:

```
为你扫描到以下技能：

| # | 技能 | 来源 | 推荐理由 | 安装量/Stars |
|---|------|------|---------|-------------|
| 1 | {name} | skills.sh | {reason} | 50K+ |
| 2 | {name} | GitHub | {reason} | ⭐ 320 |

最优推荐 #1 {name}（{推荐理由}）。告诉我编号或名字即可安装。
```

**异常输出**:
- 本地已匹配 → "本地已有相似技能 {name}，是否直接使用？"
- 三源均无结果 → "没有找到匹配的技能，建议换个关键词或简短描述再试一次。我也可以直接用通用能力帮你完成这个任务，需要吗？"
- 搜索报错 → "搜索服务暂时不可用，建议稍后重试。"

### Step 5: 安装

用户确认选择后（支持"1"、"装第一个"、技能名等方式）：

```bash
# 检查本地是否已安装
test -f ~/.agents/skills/{name}/SKILL.md && echo "INSTALLED" || echo "NOT_INSTALLED"

# 安装（来自 skills.sh）
npx -y skills@latest add "{owner/repo@skill}" -g -y
```

**结果反馈**:
- 成功 → "{name} 已安装成功。要用这个 skill 来完成你的任务吗？"
- 已安装 → "该 skill 已安装，无需重复安装。是否直接运行？"
- 失败 → "{name} 安装失败。建议检查网络后重试，或尝试手动安装：npx skills add {package}"

## 搜索技巧

以下技巧辅助提升搜索命中率，详见 `references/search-tips.md`：

- **从窄到宽**: 先用精确词搜索，结果少再放宽
- **领域+动作**: "react testing" 优于 "testing"
- **同义词轮换**: "deploy" / "deployment" / "ci-cd" 分别尝试
- **中英文混合**: 中文需求翻译为英文关键词搜索
- **关注 leaderboard**: https://skills.sh/ 查看热门技能排行

## 常见分类参考

| 类别 | 典型关键词 |
|------|-----------|
| Web 开发 | react, nextjs, vue, svelte, tailwind, css, component |
| 测试 | testing, jest, playwright, e2e, unit-test, coverage |
| DevOps | deploy, docker, kubernetes, ci-cd, terraform, aws |
| 数据 | database, sql, migration, etl, analytics, visualization |
| 文档 | docs, readme, changelog, api-docs, markdown |
| 代码质量 | review, lint, refactor, best-practices, formatting |
| 设计 | ui, ux, design-system, accessibility, figma |
| 安全 | security, audit, vulnerability, secret-scan, auth |
| AI/ML | llm, prompt, embedding, rag, fine-tuning, agent |
| 生产力 | git, workflow, automation, template, scaffold |

## 核心工具

| 命令 | 用途 |
|------|------|
| `npx skills find <kw>` | skills.sh 官方搜索 |
| `gh search repos` | GitHub 仓库搜索 |
| `npx skills add <pkg>` | 安装技能 |
| `npx skills list` | 查看已安装技能 |