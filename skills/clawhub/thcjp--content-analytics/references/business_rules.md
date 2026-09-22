# 业务规则 - content-analytics

> 来源: skills/content-analytics/SKILL.md (引用 02手册§五5.1/5.2, 02手册§十一11.1, DEF-51)

## 规则列表

### 评级标准

综合评分权重: 播放量 25% + 完播率 25% + 互动率 20% + 转化率 20% + 分享率 10%

| 评级 | 综合分 | 处理策略 |
|:-----|:-------|:---------|
| S | > 90 | 总结成功要素,复制模式 |
| A | 70 - 90 | 保持当前策略 |
| B | 50 - 70 | 基础优化建议 |
| C | <= 50 | 详细优化建议,复盘 |

### 指标计算公式

- 完播率: `completion_rate = complete_views / views`
- 互动率: `engagement_rate = (likes + comments + shares) / views`
- 转化率: `conversion_rate = follows / views`
- 分享率: `share_rate = shares / views`

### 告警阈值 (来源: 02手册§十一11.1)

- 互动率 < 2%: 内容质量告警
- 发布成功率 < 95%: 发布链路排查

### 常青内容识别 (DEF-51新增)

- 扫描范围: 30 天内发布的内容
- 常青判定: 30 天后日均播放 > 发布首日 30%
- 常青策略: 定期更新 / 重发 / 关联新内容 (来源: 02手册§五5.2)
- 存储位置: `data/content-analytics/evergreen.json`

### 发布时机优化 (DEF-51新增)

- 分析范围: 历史发布数据,按平台+时段统计平均互动率
- 推荐最佳发布时段 (来源: 02手册§五5.1)
- 输出格式: `{platform: "douyin", best_hours: [12,18,21], worst_hours: [2,3,4]}`

### 数据源优先级

1. data-copilot-mcp (优先)
2. postgres-mcp
3. analytics_cache
4. memory 发布记录 (最后降级)

> R6复核修复: exec 使用 psycopg2 直连 PG (MCP 接口由 Agent 层调用,exec 直连 PG 为 CLI 场景降级方案)

### 优化建议生成规则

- 评级 C: 详细优化建议
- 评级 B: 基础优化建议
- 评级 A/S: 成功要素总结

### 批量分析

- Cron 频率: 每日 10:00
- 范围: 过去 24 小时未分析内容
- 汇总报告: 平均评级 / 各平台对比 / Top3 / Bottom3
- 存储位置: `memory/reports/daily_content_analytics.md`

### 评级 C 通知

- 评级为 C 时: 通知 CEO,存储至 `memory/analytics/{content_id}.json`
- 评级为 C 时: 生成详细优化建议并复盘

### 6步闭环 (v25.0合并 closed-loop)

- 闭环引擎: publish → recommend → feedback → analyze → optimize → learn
- 执行脚本: content_closed_loop.py
- 来源: R75.5 Skill 去重,原 content-closed-loop 已合并