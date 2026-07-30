---
name: regulation-monitor
version: 2.0.0
description: |
  监控中国金融监管与行业管理机构网站（国家金融监管总局 NFRA、证监会 CSRC、
  央行 PBOC、国家外汇管理局 SAFE、工业和信息化部 MIIT），
  抓取最新监管政策、通知公告、风险提示等内容。
tags:
  - 金融监管
  - 监管政策
  - NFRA
  - CSRC
  - PBOC
  - SAFE
  - MIIT
  - 爬虫
author: LeisureLinux
---

# regulation-monitor / 监管动态追踪

## 核心指令

当用户需要查询中国金融监管或行业管理最新动态时，调用 `crawler.py` 脚本抓取。
将结果按机构分类整理为结构化 Markdown 输出，确保链接可点击。

**支持监管机构：**
- `nfra` — 国家金融监督管理总局
- `csrc` — 中国证券监督管理委员会
- `pboc` — 中国人民银行
- `safe` — 国家外汇管理局
- `miit` — 工业和信息化部
- `all` — 全部机构（默认）

## 触发条件

- "帮我看看最新的监管动态"
- "查一下最新监管政策"
- "最近央行/外管局/工信部发布了什么"
- "有没有新的处罚案例"
- "最近有什么监管新闻"

## 依赖

```bash
pip install requests beautifulsoup4 lxml cloudscraper
```

## 使用方法

```bash
# 所有机构最近 7 天动态
python crawler.py

# 指定回溯天数
python crawler.py --days 14

# 仅查单个机构
python crawler.py --regulator nfra --days 7
python crawler.py --regulator csrc --days 3650   # CSRC 历史数据
python crawler.py --regulator pboc --days 7
python crawler.py --regulator safe --days 30      # 外管局
python crawler.py --regulator miit --days 7       # 工信部

# JSON 格式输出
python crawler.py --json

# 指定代理
python crawler.py --proxy http://127.0.0.1:7890
```

## 技术细节

### 数据源

| 机构 | 爬取方式 | 数据时效 |
|------|----------|----------|
| **NFRA** | API via cloudscraper | 实时（有 WAF 限流） |
| **CSRC** | 静态 HTML `<li>` 解析 | 2021–至今 |
| **PBOC** | 静态 HTML `<li>` 解析 | 实时 |
| **SAFE** | 静态 HTML `<li>` 解析 | 实时 |
| **MIIT** | CMS API JSON | 实时 |

### 各机构列表示例

| 机构 | 栏目 |
|------|------|
| NFRA | 通知公告(itemId=925)、公示公告(itemId=923) |
| CSRC | 证监会要闻、通知公告 |
| PBOC | 沟通交流 |
| SAFE | 公告信息、政策法规、外汇新闻 |
| MIIT | 最新政策、通知公告 |

### 目录结构

```
regulation-monitor/
├── SKILL.md
└── crawler.py
```
