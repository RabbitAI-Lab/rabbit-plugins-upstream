---
name: daily-news
version: 1.1.0
description: "Aggregate and deliver daily news digests from multiple sources"
tags: [communication, data, report-generation, api-integration, visual]
---

# 每日新闻聚合 v1.1

从多个新闻源自动获取当日热搜/热点，汇总排序后输出�?
## 什么时候使�?
- 用户要求查看今日热搜/新闻
- 用户要求获取今日热点
- 用户要求新闻简�?- 定时任务触发（如每日 8:00 推送）
- 用户提到"热搜"�?新闻"�?今日热点"�?头条"

## 核心功能

### 多源新闻聚合
- **百度热搜**：抓取百度实时热搜榜 Top 10
- **Google Trends**：获�?Google 每日搜索趋势 Top 5（美国区�?- **自动合并去重**：多源结果合并，按热度排序，�?Top 10

### 输出格式
```
现在是北京时�?YYYY-MM-DD HH:MM:SS，今日热搜榜单如下：
1. 热点话题1
2. 热点话题2
...
10. 热点话题10
```

## 运行方式

```bash
cd skills/daily-news
python daily_news.py
```

## 数据源架�?
| 数据�?| 类型 | 获取方式 | 状�?|
|--------|------|---------|------|
| 百度热搜 | HTML 爬取 | requests + BeautifulSoup | 可用 |
| Google Trends | RSS Feed | feedparser | 可用（需网络访问 Google�?|

## 错误处理与降级策�?
### 数据源故�?| 场景 | 处理方式 |
|------|---------|
| 百度热搜请求超时 | 等待 10s 超时 �?跳过百度源，仅使�?Google Trends |
| 百度热搜页面结构变化 | CSS 选择器失�?�?输出空列�?�?提示"百度热搜暂不可用" |
| Google Trends 不可访问 | 网络受限 �?跳过 Google 源，仅使用百度热�?|
| 所有数据源均失�?| 输出"当前无法获取新闻，请检查网络连�? |
| RSS Feed 解析失败 | 跳过�?Feed，不影响其他�?|

### 数据质量
| 场景 | 处理方式 |
|------|---------|
| 热搜条目为空字符�?| 自动过滤，不计入排行 |
| 重复条目 | 基于文本精确匹配去重 |
| 结果不足 10 �?| 有多少输出多少，不凑�?|

### 网络异常
| 场景 | 处理方式 |
|------|---------|
| DNS 解析失败 | 提示检查网络连�?|
| HTTP 403/429 | 提示"请求被限制，稍后重试" |
| SSL 证书错误 | 提示检查网络环�?|

## 依赖

```bash
pip install beautifulsoup4 requests feedparser
```

## 配置说明

脚本位于 `skills/daily-news/daily_news.py`，无需额外配置�?
### 可选扩�?- 修改 `get_baidu_hot()` 中的数量参数调整百度热搜条数
- 修改 `get_google_trends()` 中的 `geo` 参数切换地区
- 添加新的数据源函数，�?`get_daily_news()` 中合�?
## 注意事项

- 百度热搜数据依赖页面 HTML 结构，百度改版可能导致解析失�?- Google Trends 在中国大陆需要科学上�?- 建议在每�?8:00-22:00 之间获取，此时段数据最完整
- 脚本输出编码�?UTF-8

## 版本历史

| 版本 | 日期 | 变更 |
|------|------|------|
| 1.1.0 | 2026-06-29 | 增加版本号、完善文档、错误处理、降级策略、依赖声�?|
| 1.0.0 | 2026-06-15 | 初始版本，百度热�?+ Google Trends |
