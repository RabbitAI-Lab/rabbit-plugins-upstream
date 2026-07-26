---
name: ai-daily-briefing
description: 生成每日 AI 资讯简报并发送到飞书。从多数据源采集 AI 资讯，整合为紧凑列表格式，以飞书卡片消息形式发送。当用户提到每日简报、AI 日报、AI 资讯、AI Daily 等意图时触发。
version: 1.1.0
metadata:
  openclaw:
    requires:
      env:
        - FEISHU_APP_ID
        - FEISHU_OPEN_ID
        - FEISHU_CHAT_ID
        - PH_API_TOKEN
      bins:
        - lark-cli
        - curl
    primaryEnv: FEISHU_APP_ID
    envVars:
      - name: FEISHU_APP_ID
        required: true
        description: 飞书应用 App ID
      - name: FEISHU_OPEN_ID
        required: true
        description: 飞书用户 Open ID，异常时私信通知
      - name: FEISHU_CHAT_ID
        required: true
        description: 飞书群聊 ID，简报发送目标
      - name: PH_API_TOKEN
        required: true
        description: Product Hunt GraphQL API token
      - name: FIRECRAWL_API_KEY
        required: false
        description: Firecrawl API key，用于抓取 Anthropic 等无 RSS 的博客
      - name: PROXY_URL
        required: false
        description: SOCKS5 代理地址，GitHub Topics 等需要时自动检查
      - name: HTTP_PROXY_URL
        required: false
        description: HTTP 代理地址（备用）
      - name: AI_DAILY_DB_PATH
        required: false
        description: 去重数据库路径，默认 ~/.openclaw/workspace/.data/ai-daily-briefing.db
    os:
      - linux
    install:
      - kind: node
        package: "@larksuite/cli"
        bins: [lark-cli]
---

# AI Daily Briefing

生成每日 AI 资讯简报，从 5 个板块采集、整合、去重、格式化，最终以飞书卡片发送到目标群聊。

## 目录结构

```
ai-daily-briefing/
├── SKILL.md                    # 本文件：协议定义 + 质量标准 + 使用说明
├── scripts/
│   ├── common.py               # 公共函数：环境检测、代理、HTTP 请求
│   ├── setup.py                # 首次安装：检测 OS/GUI、装依赖、配置指引
│   ├── preflight_check.py      # 执行前检查：环境变量、API 可用性、代理
│   ├── collect.py              # 统一采集：5 板块参数化（--section）
│   └── verify.py               # 去重 + URL 校验 + 入库 + 聚合发送
```

## 主流程（Big Picture）

```
┌─────────────────────────────────────────────────────────────────┐
│                         Main Agent                               │
│  1. python3 scripts/preflight_check.py                           │
│  2. spawn 5 sub agents（各板块并行采集）                          │
│  3. python3 scripts/verify.py aggregate --date <YYYY-MM-DD>      │
│     → 聚合 → URL 校验 → 入库 → 飞书卡片 → lark-cli 发送           │
└─────────────────────────────────────────────────────────────────┘
                                │
        ┌───────────┬───────────┼───────────┬───────────┐
        ▼           ▼           ▼           ▼           ▼
┌───────────┐ ┌───────────┐ ┌───────────┐ ┌───────────┐ ┌───────────┐
│ 行业动态   │ │ GitHub    │ │ Product   │ │ Agent     │ │ 前沿技术   │
│ Sub Agent │ │ Trending  │ │ Hunt      │ │ 工程      │ │ Sub Agent │
│           │ │ Sub Agent │ │ Sub Agent │ │ Sub Agent │ │           │
└─────┬─────┘ └─────┬─────┘ └─────┬─────┘ └─────┬─────┘ └─────┬─────┘
      │             │             │             │             │
      ▼             ▼             ▼             ▼             ▼
 collect.py    collect.py    collect.py    collect.py    collect.py
 --section     --section     --section     --section     --section
 industry      github        producthunt   agent_eng     frontier
      │             │             │             │             │
      ▼             ▼             ▼             ▼             ▼
 /tmp/ai-daily-briefing/<date>/
 ├── industry.json
 ├── github.json
 ├── producthunt.json
 ├── agent_eng.json
 └── frontier.json
      │
      ▼
┌─────────────────────────────────────────────────────────────────┐
│                    verify.py aggregate                            │
│  · 读取 5 个板块 JSON                                             │
│  · URL 校验（排除 Product Hunt 等已知限流站点）                                         │
│  · 去重入库（source_id / URL hash / SimHash）                      │
│  · 构造飞书卡片（紧凑列表 + hr 分隔）                               │
│  · lark-cli 发送到群聊                                            │
│  · 异常时私信用户                                                 │
└─────────────────────────────────────────────────────────────────┘
```

## 环境变量

**必需：** FEISHU_APP_ID, FEISHU_OPEN_ID, FEISHU_CHAT_ID, PH_API_TOKEN
**可选：** FIRECRAWL_API_KEY（Anthropic 等无 RSS 博客的抓取）、PROXY_URL（GitHub Topics 等需要时自动检查）、HTTP_PROXY_URL、AI_DAILY_DB_PATH

## 工具依赖

- lark-cli：飞书消息发送，需先绑定：`lark-cli config bind --source openclaw --app-id $FEISHU_APP_ID --identity bot-only --force`
- curl：基础 HTTP 工具
- Firecrawl（可选）：Anthropic 等无 RSS 博客的抓取，无 key 时自动跳过该源

## 前置检查

首次运行：
```bash
python3 <skill-dir>/scripts/setup.py
```

每次执行前：
```bash
python3 <skill-dir>/scripts/preflight_check.py
```

## 执行流程

1. 主 agent 运行前置检查
2. 并行 spawn 5 个 sub agent，各自执行采集脚本 + 质量判断 + 去重
3. `sessions_yield` 等待所有 sub agent 返回
4. 主 agent 执行聚合脚本：`python3 verify.py aggregate --date <YYYY-MM-DD>`
5. 异常时私信用户（不发群）

## 5 个 Sub Agent

每个 sub agent 的职责：执行采集脚本，对结果做质量判断和去重，写入约定文件。

| Sub Agent | 板块 | 采集命令 | 文件路径 | 目标条数 |
|-----------|------|----------|----------|----------|
| 1 | 行业动态 | `python3 collect.py --section industry` | `/tmp/ai-daily-briefing/<date>/industry.json` | 5-10 |
| 2 | GitHub Trending | `python3 collect.py --section github` | `/tmp/ai-daily-briefing/<date>/github.json` | 5 |
| 3 | Product Hunt | `python3 collect.py --section producthunt` | `/tmp/ai-daily-briefing/<date>/producthunt.json` | 5 |
| 4 | Agent 工程 | `python3 collect.py --section agent_eng` | `/tmp/ai-daily-briefing/<date>/agent_eng.json` | 5 |
| 5 | 前沿技术 | `python3 collect.py --section frontier` | `/tmp/ai-daily-briefing/<date>/frontier.json` | 5 |

每个 sub agent 的标准 task：
```
1. 执行采集脚本：python3 <skill-dir>/scripts/collect.py --section <section>
2. 读取脚本输出的 JSON 文件
3. 对每条结果执行质量判断（按下方标准过滤）
4. 对保留的条目执行去重检查（调用 `verify.py` 的 `is_duplicate`）
5. 去重通过后写入最终文件
6. 最多 3 次 loop，不足条目不凑数
```

脚本已处理：
- 环境判断（GUI vs 无 GUI）
- 数据提取和格式转换
- 字段映射（name → title 等）
- 中英文自动加空格
- 基础关键词过滤

sub agent 只需做：质量判断 + 去重检查。

## 质量检查标准

### ❌ 丢弃

- 使用体验安利（"用了 Claude 感觉很棒"）
- 教程/课程推广（"斯坦福免费课程"）
- 营销/变现（"AI 搞钱""点赞发教程"）
- 空洞预测（"AI 将取代 XX 职业"）

### ✅ 保留

- 模型/产品发布（新模型、新功能、官方公告）
- 技术论文/研究（有具体论文和发现，基准测试结果）
- 开源项目/工具（新开源、框架更新、基础设施）
- 行业事实/数据（融资、收购、市场数据、政策）
- 工程实践/架构（有技术细节的系统设计、性能对比）

### 判定三问

1. 有具体技术/产品/研究事实吗？→ 无则丢弃
2. 去掉品牌名后还有信息量吗？→ 无则丢弃
3. AI 工程师会觉得有用吗？→ 否则丢弃

## 去重

每个 sub agent 在质量判断通过后，执行去重检查。去重只读不写，写入由主 agent 汇总后执行。

```python
import sys
sys.path.insert(0, "<skill-dir>/scripts")
from verify import get_db, is_duplicate

conn = get_db()
is_dup, reason = is_duplicate(conn, title=title, url=url, description=description, section=section)
if is_dup:
    # 丢弃，不计数
    continue
```

板块名：industry, github, producthunt, agent_eng, frontier

三层去重：
1. source_id 精确匹配（tweet ID / arxiv ID / github repo / PH slug）
2. URL hash 精确匹配（SHA-256）
3. SimHash 语义近似（同板块最近 30 天，汉明距离 ≤ 5）

去重通过后，该条目计入目标条数。重复条目丢弃后继续采集。

## 主 Agent 汇总（聚合脚本）

主 agent 只需执行聚合脚本：

```bash
python3 <skill-dir>/scripts/verify.py aggregate --date <YYYY-MM-DD>
```

聚合脚本自动完成：
1. **读取所有板块文件**：从 `/tmp/ai-daily-briefing/<date>/*.json` 读取各板块结果
2. **入库**：将所有最终入选条目写入去重数据库
3. **构造飞书卡片**：按板块合并为紧凑列表格式
4. **发送**：调用 lark-cli 发送到目标群聊
5. **异常通知**：发送失败时私信用户，不发送群聊

如需调试，加 `--dry-run` 只输出卡片 JSON 不发送：
```bash
python3 <skill-dir>/scripts/verify.py aggregate --date 2026-07-19 --dry-run
```

## Loop 规则

每个 sub agent 独立循环：
- 标准完成：采集足够数量且通过质量检查
- 超限发送：loop > 3 次仍不满，用现有条目返回，不凑数
- 报错退出：连续失败 3 次，该板块为空

## 异常处理

异常时私信用户（不发群）：
```bash
lark-cli --profile $FEISHU_APP_ID --as bot im +messages-send \
  --user-id $FEISHU_OPEN_ID --msg-type text \
  --content '{"text":"⚠️ AI Daily 采集异常：<原因>"}'
```

异常场景：
- 前置检查失败且无法恢复
- 所有 5 个 sub agent 全部失败
- 飞书卡片发送失败

## 注意事项

- 宁缺毋滥：过滤后只剩 3 条就发 3 条
- 代理凭证不写入任何输出或日志
- 数据库自动保留 90 天数据
- 记录采集日志到 `memory/YYYY-MM-DD.md`
