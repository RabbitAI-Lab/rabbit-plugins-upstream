# 错误码定义 - content-analytics

> 来源: skills/content-analytics/SKILL.md 异常处理表

## 错误码列表

| 错误码 | 描述 | 处理方案 |
|:-------|:-----|:---------|
| CONTENT_NOT_FOUND | 内容不存在 | 返回错误提示 |
| INSUFFICIENT_DATA | 数据不足 | 返回空分析,标注数据不足 |
| PLATFORM_DATA_ERROR | 平台数据获取失败 | 记录错误,跳过该内容 |
| SCRIPT_ERROR | 脚本执行失败 | 记录错误日志,通知 CEO |

## 错误处理说明

### CONTENT_NOT_FOUND

- 触发条件: content_id 在发布记录中不存在
- 处理: 返回 `{"success": false, "error": "内容不存在", "code": "CONTENT_NOT_FOUND"}`
- 降级: 无降级,需提供有效的 content_id

### INSUFFICIENT_DATA

- 触发条件: 内容发布时间过短,互动数据不足
- 处理: 返回空分析结果,标注"数据不足",建议稍后重试

### PLATFORM_DATA_ERROR

- 触发条件: 平台数据获取失败 (API 超时/返回错误)
- 处理: 记录错误日志,跳过该内容,继续处理其他内容 (批量分析场景)

### SCRIPT_ERROR

- 触发条件: exec 脚本执行异常 (Python 错误/数据库连接失败)
- 处理: 记录错误日志,通知 CEO

## 数据源降级链

当主数据源不可用时,按以下优先级降级:

1. data-copilot-mcp (优先,Agent 层调用)
2. postgres-mcp (Agent 层调用)
3. analytics_cache (缓存数据)
4. memory 发布记录 (最后降级,数据可能不完整)

> R6复核修复: exec 使用 psycopg2 直连 PG,为 CLI 场景降级方案
