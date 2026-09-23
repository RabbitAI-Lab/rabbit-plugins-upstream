---
name: competitor-analyzer
version: "1.0.0"
description: "竞品分析器,自动抓取对标商品标题/价格/销量/评价+差异化建议。触发:选品前/竞品监控/定价参考/竞品分析"
tools: [read, write]
dependencies: []
metadata:
  layer: plugin
  priority: P2
  category: content-matrix
  openclaw:
    emoji: "📝"
    os: ["win32", "linux", "darwin"]
    requires:
      bins: ["python"]
      env: ["SILICONFLOW_API_KEY"]
      config: ["mcp.servers.competitor-analyzer-mcp"]
---

<!-- 纯MCP调用型Skill,无exec脚本 -->

# 竞品分析器

自动分析对标商品，获取标题、价格、销量、评价等关键数据。

## 使用场景

1. 选品前竞品调研
2. 竞品价格监控
3. 爆款标题分析
4. 评价关键词提取

## 工作流

1. 读取竞品关键词或 URL 列表
   - 输入校验: keywords 非空且长度 ≤50，platform 在允许列表内
   - 失败→返回 CA-ERR-04
2. **先通过fishclaw-mcp获取市场数据**（推荐模式）
   - 调用fishclaw-mcp的search_market工具搜索竞品数据
   - 将返回的市场数据作为market_data参数传入后续分析工具
   - 架构说明: OpenClaw下MCP间调用由Agent编排，不应MCP间直接HTTP调用
3. 调用competitor-analyzer-mcp的search_competitors搜索竞品
   - 参数: keywords关键词列表, platform平台, sort_by排序方式, count数量, market_data(可选,传入已搜索数据)
   - 传入market_data时跳过fishclaw-mcp调用，直接使用该数据
   - 未传入market_data时降级为HTTP直连fishclaw-mcp(需fishclaw-mcp以HTTP模式运行)
   - 抓取被限流→返回 CA-ERR-01，自动降频重试
4. 调用competitor-analyzer-mcp的analyze_competitor_trends分析竞品趋势
   - 参数: keywords关键词列表, count数量, market_data(可选,传入已搜索数据)
   - AI分析标题公式、价格区间、评价关键词分析、竞争建议
   - 字段缺失→使用默认值(价格=0, 销量=0)，标记 data_incomplete=true
   - 全部字段缺失→返回 CA-ERR-02
4.1 **获取竞品评价→好评/差评分类→关键词提取→改进建议**（评价分析流程）
   - 先通过fishclaw-mcp的get_item_reviews获取商品留言/评价内容
   - 将返回的评价数据作为reviews_data参数传入analyze_reviews
   - 闲鱼评价区域为"留言"而非传统电商"评价"，页面结构可能不稳定
   - 评价抓取失败→降级为get_item_stats的comments数量(fallback=true)
   - 评价为空→标记CA-ERR-06，跳过评价分析，继续后续流程
   - 抓取限流→同一商品5分钟内不重复抓取(内置缓存)，多商品间隔≥3秒
5. 调用competitor-analyzer-mcp的analyze_reviews分析评价情感
   - 参数: item_urls商品URL列表(逗号分隔), max_reviews_per_item每商品评价数, reviews_data(可选,传入已获取评价)
   - 输出: positive_keywords好评关键词 / negative_keywords差评关键词 / positive_ratio好评率
   - 输出: improvement_suggestions改进建议 / competitive_advantages竞争优势
   - LLM不可用时→基于关键词统计生成摘要分析
6. 调用competitor-analyzer-mcp的get_market_overview获取市场概览
   - 参数: keywords关键词列表, count数量, market_data(可选,传入已搜索数据)
   - 包含: avg_price / price_range / best_performing_title
7. 输出竞品分析报告
   - 同步写入 memory/competitor-analysis/YYYY-MM-DD.md

## MCP工具清单

<!-- R6复核修复(BUG-FAKE-121+): MCP工具已实现(competitor-analyzer-mcp/server.py),Agent直接调用;exec编排脚本可选 -->

### competitor-analyzer-mcp

| 工具名 | 功能 | 参数 |
|:-------|:-----|:-----|
| search_competitors | 搜索竞品商品 | keywords, platform, sort_by, count, market_data(可选) |
| analyze_competitor_trends | AI分析竞品趋势 | keywords, count, market_data(可选) |
| get_market_overview | 获取市场概览 | keywords, count, market_data(可选) |
| analyze_reviews | 评价情感分析 | item_urls, max_reviews_per_item, reviews_data(可选) |

### fishclaw-mcp(评价相关)

| 工具名 | 功能 | 参数 |
|:-------|:-----|:-----|
| get_item_reviews | 获取商品留言/评价 | item_url, max_reviews(默认20) |
| get_item_stats | 获取商品数据统计(降级用) | item_url |

## 输入格式

```json
{
  "keywords": ["OpenClaw", "AI代写"],
  "platform": "xianyu",
  "sort_by": "sales",
  "count": 20
}
```

## 输出格式

```json
{
  "success": true,
  "data": {
    "competitors": [
      {
        "title": "商品标题",
        "price": 1.0,
        "sales": 100,
        "want_count": 50,
        "top_reviews": [
          {"content": "评价内容", "sentiment": "positive"},
          {"content": "评价内容", "sentiment": "negative"}
        ],
        "title_formula": "数字+结果",
        "tags": ["AI", "教程"]
      }
    ],
    "avg_price": 2.5,
    "price_range": [0.1, 10.0],
    "competitor_count": 20,
    "best_performing_title": "最高销量标题",
    "review_analysis": {
      "positive_keywords": ["快", "专业", "实惠"],
      "negative_keywords": ["慢", "敷衍"],
      "positive_ratio": 0.8,
      "improvement_suggestions": ["关注并改善'慢'相关体验"],
      "competitive_advantages": ["强化'专业'优势作为卖点"],
      "review_summary": "共分析3个商品，15条评价，好评率0.8"
    }
  },
  "error": null,
  "code": null
}
```

> **与price-dynamic的数据衔接**: price-dynamic的competitor_data输入要求price_range为对象格式{min,max}，而本SKILL输出price_range为数组格式[min,max]。Agent编排层需执行格式转换: `price_range[0]→min, price_range[1]→max`。competitor_count字段由get_market_overview工具提供。

## 验证步骤（C5新增）

分析完成后必须执行以下验证（来源: 05文档§6.3 C5验收标准）:

| 步骤 | 验证项 | 验证方式 | 通过标准 |
|:-----|:-------|:---------|:---------|
| V1 | 竞品数据非空 | 检查competitors数组长度 | >=3条有效数据 |
| V2 | 数据时效性 | 检查数据时间戳 | <24h |
| V3 | 价格数据有效 | 检查price>0 | 全部price>0 |
| V4 | 关键词非空 | 检查keywords输入 | keywords非空 |

## 异常处理

| 异常编号 | 错误代码 | 触发条件 | 处理方式 | 恢复策略 |
|:---------|:---------|:---------|:---------|:---------|
| CA-ERR-01 | RATE_LIMITED | 抓取被限流 | 降低频率，切换代理IP | 等待60s后重试，最多3次 |
| CA-ERR-02 | DATA_INCOMPLETE | 数据不完整(>50%字段缺失) | 使用已有数据分析，标记data_incomplete | 扩大关键词范围重新搜索 |
| CA-ERR-03 | COMPETITOR_DELISTED | 竞品已下架 | 标记"已下架"，使用历史数据 | 从memory/读取上次分析结果 |
| CA-ERR-04 | INVALID_INPUT | keywords为空或platform无效 | 返回错误，提示修正输入 | 等待用户提供有效输入 |
| CA-ERR-05 | MCP_UNAVAILABLE | fishclaw-mcp不可用 | 返回错误，提示检查MCP服务 | 检查MCP进程状态，重启后重试 |
| CA-ERR-06 | NO_REVIEWS | 评价数据为空(闲鱼留言区无内容) | 跳过评价分析，继续后续流程 | 标记review_analysis=null，不影响主流程 |
| CA-ERR-07 | REVIEW_RATE_LIMITED | 评价抓取限流 | 使用5分钟缓存，避免重复抓取 | 等待5分钟后重试，降级为comments数量 |

## 示例

输入:
```json
{
  "keywords": ["AI代写文案", "AI绘画头像"],
  "platform": "xianyu",
  "sort_by": "sales",
  "count": 10
}
```

输出:
```json
{
  "success": true,
  "data": {
    "competitors": [
      {
        "title": "AI代写文案 润色修改 一键生成",
        "price": 1.5,
        "sales": 230,
        "want_count": 85,
        "top_reviews": [
          {"content": "速度快，质量好", "sentiment": "positive"},
          {"content": "价格实惠，推荐", "sentiment": "positive"}
        ],
        "title_formula": "服务名+动作+效果",
        "tags": ["AI", "文案", "代写"]
      },
      {
        "title": "AI绘画头像定制 专属卡通形象",
        "price": 3.0,
        "sales": 156,
        "want_count": 62,
        "top_reviews": [
          {"content": "很有创意，出图快", "sentiment": "positive"},
          {"content": "回复太慢了", "sentiment": "negative"}
        ],
        "title_formula": "服务名+差异化卖点",
        "tags": ["AI", "绘画", "头像"]
      }
    ],
    "avg_price": 2.25,
    "price_range": [1.0, 5.0],
    "competitor_count": 10,
    "best_performing_title": "AI代写文案 润色修改 一键生成",
    "review_analysis": {
      "positive_keywords": ["快", "实惠", "创意"],
      "negative_keywords": ["慢"],
      "positive_ratio": 0.75,
      "improvement_suggestions": ["关注并改善'慢'相关体验"],
      "competitive_advantages": ["强化'快'优势作为卖点", "强化'实惠'优势作为卖点"],
      "review_summary": "共分析2个商品，4条评价，好评率0.75"
    }
  },
  "error": null,
  "code": null
}
```

## 变更历史

| 版本 | 日期 | 变更说明 |
|:-----|:-----|:---------|
| v1.0.0 | 2026-04-09 | 初始实现，基础竞品分析功能 |
| v1.1.0 | 2026-05-14 | 补充详细工作流步骤、异常处理错误码、示例章节 |
| v1.2.0 | 2026-05-22 | 修复MCP间调用架构: 3个工具添加market_data参数，支持Agent编排模式(推荐)和HTTP直连模式(降级) |
| v1.3.0 | 2026-05-23 | 补充competitor_count输出字段(来源:get_market_overview工具)，添加与price-dynamic的数据衔接说明和格式映射规则 |
| v1.4.0 | 2026-05-23 | 新增好评/差评分析能力: fishclaw-mcp新增get_item_reviews工具, competitor-analyzer-mcp新增analyze_reviews工具, SKILL.md工作流增加步骤4.1评价分析流程, top_reviews结构从字符串数组改为{content,sentiment}对象数组, 新增review_analysis输出段, 新增CA-ERR-06/CA-ERR-07异常 |

## 历史记录

| 版本 | 操作 | 时间 | 原因 |
|------|------|------|------|
| cycle_20260622 | optimized | 2026-06-22T06:52:35.824876+00:00 | 自生长周期优化触发(metrics_based) |

| 版本 | 操作 | 时间 | 原因 |
|------|------|------|------|
| cycle_20260725 | optimized | 2026-07-25T12:20:31.262108+00:00 | 自生长周期优化触发(metrics_based) |
| 版本 | 操作 | 时间 | 原因 |
|------|------|------|------|
| cycle_20260726 | optimized | 2026-07-25T23:25:32.369112+00:00 | 自生长周期优化触发(metrics_based) |
| 版本 | 操作 | 时间 | 原因 |
|------|------|------|------|
| cycle_20260729 | optimized | 2026-07-28T19:18:46.264164+00:00 | 自生长周期优化触发(metrics_based) |
| 版本 | 操作 | 时间 | 原因 |
|------|------|------|------|
| cycle_20260729 | optimized | 2026-07-28T19:19:36.145781+00:00 | 自生长周期优化触发(metrics_based) |
| 版本 | 操作 | 时间 | 原因 |
|------|------|------|------|
| cycle_20260730 | optimized | 2026-07-29T22:09:36.590963+00:00 | 自生长周期优化触发(metrics_based) |
| 版本 | 操作 | 时间 | 原因 |
|------|------|------|------|
| cycle_20260801 | optimized | 2026-07-31T19:36:51.675530+00:00 | 自生长周期优化触发(metrics_based) |
| 版本 | 操作 | 时间 | 原因 |
|------|------|------|------|
| cycle_20260802 | optimized | 2026-08-01T18:34:53.196243+00:00 | 自生长周期优化触发(metrics_based) |
| 版本 | 操作 | 时间 | 原因 |
|------|------|------|------|
| cycle_20260803 | optimized | 2026-08-03T01:00:42.388844+00:00 | 自生长周期优化触发(metrics_based) |
| 版本 | 操作 | 时间 | 原因 |
|------|------|------|------|
| cycle_20260804 | optimized | 2026-08-03T18:34:23.218652+00:00 | 自生长周期优化触发(metrics_based) |
| 版本 | 操作 | 时间 | 原因 |
|------|------|------|------|
| cycle_20260804 | optimized | 2026-08-03T18:34:35.788397+00:00 | 自生长周期优化触发(metrics_based) |
| 版本 | 操作 | 时间 | 原因 |
|------|------|------|------|
| cycle_20260804 | optimized | 2026-08-03T18:34:50.184220+00:00 | 自生长周期优化触发(metrics_based) |
| 版本 | 操作 | 时间 | 原因 |
|------|------|------|------|
| cycle_20260805 | optimized | 2026-08-04T18:36:23.512490+00:00 | 自生长周期优化触发(metrics_based) |
| 版本 | 操作 | 时间 | 原因 |
|------|------|------|------|
| cycle_20260805 | optimized | 2026-08-04T18:36:38.635879+00:00 | 自生长周期优化触发(metrics_based) |
| 版本 | 操作 | 时间 | 原因 |
|------|------|------|------|
| cycle_20260806 | optimized | 2026-08-05T18:34:49.982423+00:00 | 自生长周期优化触发(metrics_based) |
| 版本 | 操作 | 时间 | 原因 |
|------|------|------|------|
| cycle_20260806 | optimized | 2026-08-05T18:35:02.277184+00:00 | 自生长周期优化触发(metrics_based) |
| 版本 | 操作 | 时间 | 原因 |
|------|------|------|------|
| cycle_20260807 | optimized | 2026-08-06T18:35:53.294060+00:00 | 自生长周期优化触发(metrics_based) |
| 版本 | 操作 | 时间 | 原因 |
|------|------|------|------|
| cycle_20260810 | optimized | 2026-08-09T19:18:59.256352+00:00 | 自生长周期优化触发(metrics_based) |
| 版本 | 操作 | 时间 | 原因 |
|------|------|------|------|
| cycle_20260811 | optimized | 2026-08-10T18:36:35.448293+00:00 | 自生长周期优化触发(metrics_based) |
| 版本 | 操作 | 时间 | 原因 |
|------|------|------|------|
| cycle_20260811 | optimized | 2026-08-10T18:36:50.550427+00:00 | 自生长周期优化触发(metrics_based) |
| 版本 | 操作 | 时间 | 原因 |
|------|------|------|------|
| cycle_20260812 | optimized | 2026-08-12T02:37:48.143899+00:00 | 自生长周期优化触发(metrics_based) |
| 版本 | 操作 | 时间 | 原因 |
|------|------|------|------|
| cycle_20260813 | optimized | 2026-08-12T23:33:44.214101+00:00 | 自生长周期优化触发(metrics_based) |
| 版本 | 操作 | 时间 | 原因 |
|------|------|------|------|
| cycle_20260814 | optimized | 2026-08-13T18:35:35.385787+00:00 | 自生长周期优化触发(metrics_based) |