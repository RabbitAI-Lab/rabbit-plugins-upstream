---
name: "unified-search"
description: "统一搜索：百度/17引擎中文搜索/Tavily/Brave/Google Scholar/skills发现，智能fallback链"
user-invocable: true
metadata:
  openclaw:
    emoji: "🔍"
    tags: ["search", "baidu", "tavily", "brave", "scholar"]
---

# Unified Search v2.0

## Fallback 链
百度 → 搜狗(微信/知乎) → 必应 → DuckDuckGo → Brave → Tavily → Google
每源3次重试后切换。

## 中文搜索
百度AI搜索(中文最佳)/搜狗/必应中国/360搜索

## 英文搜索
Brave(隐私)/Tavily(AI优化)/DuckDuckGo(免费)/Google

## 学术搜索
Google Scholar / CNKI / 万方

## Skills 发现
ClawHub API + GitHub `SKILL.md` 搜索

## API Keys(可选)
```bash
export BRAVE_API_KEY="***"
export TAVILY_API_KEY="***"
```

## 结果处理
标题+URL+摘要+来源 | 去重合并 | 按相关度排序 | 标注时效 | 时间筛选(day/week/month/year)
