---
slug: "apple-health-skill"
name: "apple-health-skill"
version: 1.0.1
displayName: "运动健康数据"
summary: "与运动健康数据对话，查询训练、心率、活动量和VO2 Max趋势"
license: "Proprietary"
description: |-
  使用AI与运动健康数据对话。支持查询训练记录、心率趋势、活动量环、VO2 Max、
  性能管理图表（CTL/ATL/TSB）等。通过健康数据同步服务获取数据，AI教练提供
  个性化训练建议。适用于运动训练分析、恢复评估和健身数据管理场景.
tools:
  - read
  - exec
homepage: "https://skillhub.cn"
tags:
  - 生活服务
# 定价元数据
suggested_price: "29.9 CNY/per_use"
pricing_tier: "L3-专业级"
pricing_model: "per_use"

---
# 运动健康数据

使用AI与运动健康数据对话。查询训练记录、心率趋势、活动量环、VO2 Max、性能管理图表等。通过健康数据同步服务获取运动手环/手表同步的健康数据，AI教练提供个性化训练建议.
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| input | string | 是 | 运动健康数据处理的输入数据或指令 |
| options | object | 否 | 附加配置选项,如模式选择、格式偏好等 |
| callback_url | string | 否 | 异步处理完成后的回调通知URL |

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|:-----|:-----|:-----|
| 基础功能 | 支持 | 支持 |
| 复杂工作流可视化编排 | 不支持 | 支持 |
| 条件分支与异常重试 | 不支持 | 支持 |
| 定时触发与事件驱动 | 不支持 | 支持 |
| 执行日志与审计追踪 | 不支持 | 支持 |
| 分布式任务调度与负载均衡 | 不支持 | 支持 |

## 配置说明

1. 下载健康数据同步服务应用，授予健康数据访问权限
2. 进入 Settings > API Keys，点击 Generate New Key
3. 设置环境变量：

```bash
export HEALTH_API_KEY="[REDACTED]"
```

所有认证端点需在请求头中携带 `X-API-Key`.
## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux

### 依赖项
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|---:|---:|---:|---:|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
如需调用外部API，请参考环境配置章节设置对应密钥

### 可用性分类
- **分类**: MD+EXEC（）

**API Key配置方式**:
```bash
export API_KEY="your_api_key_here"
```
配置后需重启会话或开启新终端生效。API Key应妥善保管,避免泄露到版本控制系统.
## 核心能力

### 1. 每日训练生成

通过 `GET /api/v1/wod?sport=run&duration=45` 获取随机结构化训练方案，无需认证。参数 `sport` 支持 `run`（跑步）、`bike`（骑行）、`swim`（游泳）、`strength`（力量），默认 `run`。参数 `duration` 指定训练时长（10-300分钟），默认45。适用于快速获取训练建议和运动计划生成.
### 2. AI教练对话
通过 `POST /api/v1/coach/chat` 向AI教练提问健康数据相关问题。请求体包含 `message` 字段（自然语言问题），AI教练拥有用户训练和健康指标的完整上下文。支持查询如"最近一个月静息心率变化"、"本周做了多少次训练"、"VO2 Max趋势如何"等问题。适用于自然语言健康数据查询场景.
**处理**: 解析AI教练对话的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回AI教练对话的处理结果,包含执行状态码、结果数据和执行日志.
### 3. 获取训练记录

通过 `GET /api/v1/workouts?start=2026-02-09&end=2026-02-15` 获取指定日期范围内的训练记录。必填参数 `start` 和 `end`（YYYY-MM-DD格式），最大查询范围90天。返回训练列表，包含训练类型、时长、距离、心率等详细数据。适用于训练历史回溯和数据分析.
### 4. 性能管理图表（PMC）
通过 `GET /api/v1/performance/pmc` 获取性能管理图表数据。返回CTL（慢性训练负荷，反映健身水平）、ATL（急性训练负荷，反映疲劳度）和TSB（训练压力平衡，反映状态/形态）。TSB低于-20表示运动员处于疲劳状态，建议安排恢复日。适用于训练负荷监控和恢复评估.
**输入**: 用户提供性能管理图表（PMC）所需的指令和必要参数.
**处理**: 解析性能管理图表（PMC）的输入参数,执行核心处理逻辑,返回结构化结果和执行状态。- 验证返回数据的完整性和格式正确性
- 参考`性能管理图表（PMC）`的配置文档进行参数调优
### 5. 性能统计
通过 `GET /api/v1/performance/stats` 获取从健康数据推导的性能指标。返回FTP（功能阈值功率）、阈值配速、心率区间分布和其他运动表现指标。适用于运动能力评估和训练强度设定.
**输入**: 用户提供性能统计所需的指令和必要参数.
**处理**: 解析性能统计的输入参数,执行核心处理逻辑,返回结构化结果和执行状态。- 验证返回数据的完整性和格式正确性
- 参考`性能统计`的配置文档进行参数调优
### 6. 运动员档案

通过 `GET /api/v1/profile` 获取运动员档案信息。返回用户的基本信息、运动偏好、历史训练摘要等数据。适用于用户画像构建和个性化建议基础数据获取。- 验证返回数据的完整性和格式正确性
- 参考`运动员档案`的配置文档进行参数调优
### 7. 聊天历史

通过 `GET /api/v1/coach/history` 获取AI教练的聊天历史记录。返回之前的对话内容，包含用户问题和AI教练回复。适用于对话上下文回顾和连续性对话场景。- 验证返回数据的完整性和格式正确性
- 参考`聊天历史`的配置文档进行参数调优
#
## 使用流程

1. 配置环境变量 `HEALTH_API_KEY`，确保健康数据同步服务已授权
2. 使用 `GET /api/v1/wod` 获取训练方案（无需认证），或通过 `POST /api/v1/coach/chat` 直接向AI教练提问
3. 需要具体训练数据时，调用 `GET /api/v1/workouts` 获取指定日期范围记录（YYYY-MM-DD格式，最大90天）
4. 评估训练负荷时，调用 `GET /api/v1/performance/pmc` 检查CTL/ATL/TSB，若TSB低于-20建议安排恢复日
5. 需要运动能力数据时，调用 `GET /api/v1/performance/stats` 获取FTP、心率区间等指标
6. 通过 `GET /api/v1/coach/history` 回顾之前的AI教练对话

#
## 示例

### 示例1：获取训练方案并查询AI教练

```bash
# 获取45分钟跑步训练方案（无需认证）
curl "https://health-api.example.com/api/v1/wod?sport=run&duration=45"
# 响应包含结构化训练计划：热身、主训练、放松等阶段
# ...
# 向AI教练提问
curl -X POST "https://health-api.example.com/api/v1/coach/chat" \
  -H "X-API-Key: $HEALTH_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"message": "How has my resting heart rate changed over the last month?"}'
# AI教练返回静息心率变化趋势分析
```

### 示例2：查询训练记录并评估疲劳状态

```bash
# 获取最近一周的训练记录
curl -H "X-API-Key: $HEALTH_API_KEY" \
  "https://health-api.example.com/api/v1/workouts?start=2026-02-09&end=2026-02-15"
# ...
# 检查训练负荷和疲劳状态
curl -H "X-API-Key: $HEALTH_API_KEY" \
  "https://health-api.example.com/api/v1/performance/pmc"
# 响应包含 CTL（健身）、ATL（疲劳）、TSB（状态）
# 若 TSB < -20，建议安排恢复日
# ...
# 获取性能统计（FTP、心率区间等）
curl -H "X-API-Key: $HEALTH_API_KEY" \
  "https://health-api.example.com/api/v1/performance/stats"
```

## 错误处理

| 错误场景 | HTTP状态 | 原因 | 处理方式 |
|:---:|:---:|:---:|:---:|
| API Key未设置 | 401 | `HEALTH_API_KEY` 环境变量缺失或为空 | 在健康数据同步服务中生成API Key并设置环境变量 |
| 日期范围超过90天 | 400 | `start` 和 `end` 间隔超过最大范围 | 将查询范围缩小到90天以内，分段查询 |
| 日期格式错误 | 400 | `start` 或 `end` 非YYYY-MM-DD格式 | 使用标准日期格式，如 `2026-02-09` |
| sport参数无效 | 400 | 传入了不支持的sport值 | 使用有效值：`run`/`bike`/`swim`/`strength` |
| duration超出范围 | 400 | duration不在10-300分钟范围内 | 调整duration值到10-300范围内，默认45分钟 |
| 免费配额用尽 | 429 | 超出100次/天读取或3次/天AI对话限制 | 等待次日重置，或升级至付费配额（10000次/天读取、100次/天AI对话） |
| TSB低于-20 | 200 | 运动员疲劳过度，训练压力平衡偏低 | 建议安排恢复日，减少高强度训练直到TSB回升 |

## 常见问题

### Q1: 如何获取API Key？

在健康数据同步服务应用中，进入 Settings > API Keys，点击 Generate New Key 生成密钥。将生成的密钥设置到环境变量 `HEALTH_API_KEY` 中。所有认证端点需在请求头中携带 `X-API-Key: $HEALTH_API_KEY`.
### Q2: 日期格式有什么要求？

所有日期参数使用YYYY-MM-DD格式（如 `2026-02-09`）。`GET /api/v1/workouts` 端点的 `start` 和 `end` 参数之间的最大查询范围为90天，超过会返回400错误。需要查询更长时间范围时，分段多次查询.
### Q3: WOD端点需要认证吗？

不需要。`GET /api/v1/wod` 是唯一无需认证的端点。参数 `sport` 支持 `run`/`bike`/`swim`/`strength`（默认 `run`），`duration` 范围10-300分钟（默认45）。适用于快速获取训练方案，无需配置API Key.
### Q4: PMC图表的CTL/ATL/TSB分别代表什么？

CTL（Chronic Training Load）反映慢性训练负荷，代表长期健身水平。ATL（Acute Training Load）反映急性训练负荷，代表近期疲劳度。TSB（Training Stress Balance）是CTL减去ATL的差值，反映当前状态/形态。TSB为正值表示状态良好，低于-20表示疲劳过度，建议安排恢复日.
### Q5: 免费版和付费版的配额分别是多少？

免费版配额：读取端点100次/天，AI端点（`coach/chat`）3次/天。付费版配额：读取端点10000次/天，AI端点100次/天。超限后返回429状态码，需等待次日重置或升级配额.
### Q6: AI教练可以回答哪些问题？

AI教练拥有用户健康数据的完整上下文，可以回答："最近一个月静息心率变化"、"本周做了多少次训练"、"VO2 Max趋势如何"、"本周睡眠趋势"、"对比本月和上月跑步配速"、"根据近期训练是否应该安排恢复日"等问题。通过 `POST /api/v1/coach/chat` 发送自然语言问题即可.
## 已知限制

- 认证端点需配置 `HEALTH_API_KEY` 环境变量
- 训练记录查询最大范围90天，超长范围需分段查询
- 免费版AI对话限制3次/天，高频使用需升级付费版
- 需要健康数据同步服务已授权并同步数据
- 不适用于实时流数据处理场景

## 输出格式

```json
{
  "success": true,
  "data": {
    "result": "运动健康数据处理结果",
    "execution_time": "0.5s",
    "metadata": {
      "version": "1.0",
      "processor": "apple-health-skill"
    }
  },
  "execution_log": [
    "解析输入参数",
    "执行核心处理",
    "格式化输出结果"
  ],
  "error": null
}
```
