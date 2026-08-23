---
name: content-analytics
description: "内容效果分析(v25.0合并content-closed-loop)，计算播放/完播/互动/转化指标，生成S/A/B/C评级和优化建议+6步闭环(publish→recommend→feedback→analyze→optimize→learn)。触发词：内容分析/播放数据/完播率/互动统计/内容评级/闭环/CP-07 不触发：内容发布/内容模板/趋势发现"
version: 2.0.0
user-invocable: false
tools: [read, exec]
dependencies: [data-copilot]
metadata:
  layer: plugin
  priority: P1
  category: infra-ops
  openclaw:
    emoji: "📊"
    os: ["win32", "linux", "darwin"]
    requires:
      bins: ["python"]
      config: ["mcp.servers.data-copilot-mcp"]
      env: ["DATA_COPILOT_MCP_URL"]
---

> **v25.0合并**: content-closed-loop已合并到本Skill(R75.5 Skill去重)。6步闭环引擎(publish→recommend→feedback→analyze→optimize→learn)由content_closed_loop.py执行。原content-closed-loop目录已删除。

> **运行环境**: exec脚本必须使用 **Python 3.11.x** (`.venv/Scripts/python.exe`) 执行。

# Content Analytics Skill

内容效果分析、评级生成、优化建议、6步闭环。**版本**: v2.0(v25.0合并closed-loop) | **优先级**: P1

## 使用场景

1. 效果分析: 发布后24小时/CEO查询 → 分析内容效果
2. 评级生成: 分析完成后 → S/A/B/C评级
3. **6步闭环(v25.0合并)**: CP-07内容闭环 → publish→recommend→feedback→analyze→optimize→learn
3. 优化建议: 评级低于B时 → 生成优化建议
4. 批量分析: Cron每日10:00 → 批量分析近期内容
5. 常青内容识别: 30天持续获得流量→标记为常青内容(DEF-51新增)
6. 发布时机优化: 分析历史数据推荐最佳发布时段(DEF-51新增)

## 工作流

### 效果分析流程
1. 接收(content_id/platform)，验证内容存在+平台有效
2. 读取memory/YYYY-MM-DD.md发布日志，获取发布记录
3. exec调用content_analytics.py获取互动数据(数据源优先级: data-copilot-mcp > postgres-mcp > analytics_cache > memory发布记录)
   - R6复核修复(BUG-FAKE-121+): exec使用psycopg2直连PG(data-copilot-mcp/postgres-mcp的MCP接口由Agent层调用,exec直连PG为CLI场景降级方案)
4. 计算指标: 播放量/完播率=complete_views/views / 互动率=(likes+comments+shares)/views / 转化率=follows/views
5. 生成评级: S(>90) / A(70-90) / B(50-70) / C(<=50)
6. 生成优化建议: C→详细 / B→基础 / A/S→成功要素总结
7. 存储至memory/analytics/{content_id}.json，评级C时通知CEO

### 常青内容识别流程(DEF-51新增)
1. 扫描30天内发布的内容
2. 检查持续流量指标: 30天后日均播放>发布首日30%
3. 标记为常青内容→写入data/content-analytics/evergreen.json
4. 常青内容策略: 定期更新/重发/关联新内容(来源:02手册§五5.2)

### 发布时机优化(DEF-51新增)
1. 分析历史发布数据，按平台+时段统计平均互动率
2. 推荐最佳发布时段(来源:02手册§五5.1)
3. 输出: {platform: "douyin", best_hours: [12,18,21], worst_hours: [2,3,4]}

### 批量分析流程
1. Cron每日10:00触发 → 查询过去24小时未分析内容
2. 逐个执行效果分析 → 生成汇总报告(平均评级/各平台对比/Top3/Bottom3)
3. 存储至memory/reports/daily_content_analytics.md

### 内容闭环流程(full-loop)
1. **同步**: 从tenant_publish_records同步最近7天成功发布的内容(含真实互动指标view_count/like_count等)到content_publish_log
2. **推荐**: 为内容推荐目标好友(基于兴趣embedding相似度)
3. **反馈**: 尝试通过opencli获取最新平台数据(opencli不可用时使用已同步的真实指标)
4. **分析**: 基于真实指标计算engagement_score/conversion_rate/roi_score,生成表现评级
5. **优化**: 汇总近期内容表现,生成优化策略(urgent/engagement/content/scale/maintain)
6. **学习**: 将分析结果存储为有意义经验(标题/平台/指标/互动率/ROI/建议)到agent_memory,供orchestrator注入后续内容生成

> **Fix-B/C/E**: 闭环基于tenant_publish_records真实发布数据,不再创建fake content_id。经验文本包含标题、平台、真实指标、互动率、ROI和优化建议,orchestrator的_query_agent_memory_lessons可查询并注入到内容生成提示词。

## 评级标准

综合评分权重: 播放量25% + 完播率25% + 互动率20% + 转化率20% + 分享率10%

| 评级 | 综合分 | 处理 |
|:-----|:-------|:-----|
| S | >90 | 总结成功要素，复制模式 |
| A | 70-90 | 保持当前策略 |
| B | 50-70 | 基础优化建议 |
| C | <=50 | 详细优化建议，复盘 |

告警阈值(来源: 02手册§十一11.1): 互动率<2%→内容质量告警 / 发布成功率<95%→发布链路排查

## 输入格式

```json
{
  "action": "analyze|batch_analyze|evergreen_detect|timing_optimize",
  "content_id": "content_20260407_001",
  "platform": "douyin|weibo|xiaohongshu|zhihu|bilibili|all",
  "date_range": {"start": "2026-06-01", "end": "2026-06-30"},
  "lookback_days": 30
}
```

字段说明:
- `action`: 操作类型(analyze单内容分析/batch_analyze批量分析/evergreen_detect常青内容识别/timing_optimize发布时机优化)
- `content_id`: 内容ID(analyze操作必填)
- `platform`: 平台筛选(douyin抖音/weibo微博/xiaohongshu小红书/zhihu知乎/bilibili哔哩哔哩/all全部)
- `date_range`: 日期范围(batch_analyze/report操作使用)
- `lookback_days`: 回溯天数(evergreen_detect默认30/timing_optimize默认90)

## 输出格式

```json
{
  "success": true,
  "data": {
    "action": "analyze",
    "content_id": "content_20260407_001",
    "platform": "douyin",
    "rating": "A",
    "score": 75,
    "metrics": {
      "views": 10000,
      "completion_rate": 0.65,
      "engagement_rate": 0.08,
      "conversion_rate": 0.02,
      "share_rate": 0.03
    },
    "score_breakdown": {
      "views_score": 80,
      "completion_score": 75,
      "engagement_score": 70,
      "conversion_score": 65,
      "share_score": 85
    },
    "suggestions": ["开头3秒吸引力不错", "中段完播率下降,建议优化节奏"],
    "evergreen": false,
    "analyzed_at": "2026-04-08T10:00:00Z"
  },
  "error": null,
  "code": null
}
```

字段说明:
- `rating`: 评级(S>90/A 70-90/B 50-70/C<=50)
- `score`: 综合评分(0-100,权重:播放25%+完播25%+互动20%+转化20%+分享10%)
- `metrics`: 核心指标(views播放/completion_rate完播率/engagement_rate互动率/conversion_rate转化率/share_rate分享率)
- `score_breakdown`: 各维度得分(用于定位优化方向)
- `suggestions`: 优化建议数组(评级C→详细/B→基础/A/S→成功要素)
- `evergreen`: 是否常青内容(evergreen_detect操作返回)

## 异常处理

| 异常 | 错误码 | 处理 |
|:-----|:-------|:-----|
| 内容不存在 | CONTENT_NOT_FOUND | 返回错误提示 |
| 数据不足 | INSUFFICIENT_DATA | 返回空分析，标注数据不足 |
| 平台数据获取失败 | PLATFORM_DATA_ERROR | 记录错误，跳过该内容 |
| 脚本执行失败 | SCRIPT_ERROR | 记录错误日志，通知CEO |

## 示例

### 单内容分析

1. 输入: {content_id:"content_20260407_001", platform:"douyin"}
2. exec调用content_analytics.py → 计算指标 → 评级A(75分)
3. 输出: `{success:true, data:{rating:"A", score:75, metrics:{views:10000, completion_rate:0.65, engagement_rate:0.08}, suggestions:["开头3秒吸引力不错"]}}`
