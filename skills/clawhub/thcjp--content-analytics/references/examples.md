# 示例 - content-analytics

> 来源: skills/content-analytics/SKILL.md 示例章节

## 示例1: 单内容分析 (analyze)

### 输入

```json
{
  "action": "analyze",
  "content_id": "content_20260407_001",
  "platform": "douyin"
}
```

### 输出

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

> 评级 A (70-90): 保持当前策略。互动率 8% > 2% 告警阈值,无质量告警。

## 示例2: 常青内容识别 (evergreen_detect)

### 输入

```json
{
  "action": "evergreen_detect",
  "lookback_days": 30
}
```

### 输出

```json
{
  "success": true,
  "data": {
    "action": "evergreen_detect",
    "evergreen_contents": [
      {
        "content_id": "content_20260601_003",
        "platform": "xiaohongshu",
        "first_day_views": 500,
        "day30_avg_views": 180,
        "evergreen_ratio": 0.36,
        "evergreen": true
      }
    ],
    "total_checked": 45,
    "evergreen_count": 1
  },
  "error": null,
  "code": null
}
```

> 常青判定: 30天后日均播放 (180) > 发布首日30% (150),evergreen=true。

## 示例3: 发布时机优化 (timing_optimize)

### 输入

```json
{
  "action": "timing_optimize",
  "platform": "douyin",
  "lookback_days": 90
}
```

### 输出

```json
{
  "success": true,
  "data": {
    "action": "timing_optimize",
    "platform": "douyin",
    "best_hours": [12, 18, 21],
    "worst_hours": [2, 3, 4],
    "avg_engagement_by_hour": {
      "12": 0.085, "18": 0.092, "21": 0.078,
      "2": 0.012, "3": 0.008, "4": 0.010
    }
  },
  "error": null,
  "code": null
}
```
