---
slug: "apple-health-skill-free"
name: "apple-health-skill-free"
version: "1.0.0"
displayName: "运动健康数据基础版"
summary: "基础运动健康数据查询，获取训练方案和训练记录"
license: "MIT"
description: |-
  使用AI与运动健康数据对话的免费版。支持获取每日训练方案（无需认证）和查询训练记录.
  适用于基础训练数据查看场景。升级至完整版可解锁AI教练对话、性能管理图表、
  性能统计和聊天历史功能.
tools:
  - read
  - exec
homepage: "https://skillhub.cn"
tags:
  - 生活服务

---
# 运动健康数据（免费版）

使用AI与运动健康数据对话的免费版。支持获取每日训练方案（无需认证）和查询训练记录。通过健康数据同步服务获取运动手环/手表同步的健康数据.
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| input | string | 是 | 运动健康数据基础版处理的输入数据或指令 |
| options | object | 否 | 附加配置选项,如模式选择、格式偏好等 |
| callback_url | string | 否 | 异步处理完成后的回调通知URL |

## 配置说明

1. 下载健康数据同步服务应用，授予健康数据访问权限
2. 进入 Settings > API Keys，点击 Generate New Key
3. 设置环境变量：

```bash
export HEALTH_API_KEY="[REDACTED]"
```

认证端点需在请求头中携带 `X-API-Key`。`GET /api/v1/wod` 端点无需认证.
## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux

### 依赖项
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-----|:-----|:-----|:-----|
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
通过 `GET /api/v1/wod?sport=run&duration=45` 获取随机结构化训练方案，无需认证。参数 `sport` 支持 `run`（跑步）、`bike`（骑行）、`swim`（游泳）、`strength`（力量），默认 `run`。参数 `duration` 指定训练时长（10-300分钟），默认45。适用于快速获取训练建议.
**输出**: 返回每日训练生成的处理结果,包含执行状态码、结果数据和执行日志.
### 2. 获取训练记录
通过 `GET /api/v1/workouts?start=2026-02-09&end=2026-02-15` 获取指定日期范围内的训练记录。必填参数 `start` 和 `end`（YYYY-MM-DD格式），最大查询范围90天。返回训练列表，包含训练类型、时长、距离、心率等详细数据。免费版配额100次/天。适用于训练历史回溯.
**处理**: 解析获取训练记录的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
### 3. 运动员档案

通过 `GET /api/v1/profile` 获取运动员档案信息。返回用户的基本信息、运动偏好、历史训练摘要等数据。适用于用户画像构建和基础数据获取。- 验证返回数据的完整性和格式正确性
- 参考`运动员档案`的配置文档进行参数调优
#
## 升级提示

以下为完整版（apple-health-skill）独有功能，免费版不可用：

- **AI教练对话**：`POST /api/v1/coach/chat` 自然语言提问健康数据，完整版配额100次/天
- **性能管理图表（PMC）**：`GET /api/v1/performance/pmc` 获取CTL/ATL/TSB训练负荷数据
- **性能统计**：`GET /api/v1/performance/stats` 获取FTP、阈值配速、心率区间等指标
- **聊天历史**：`GET /api/v1/coach/history` 回顾AI教练对话记录

升级至完整版以获取全部能力.
## 使用流程

1. 使用 `GET /api/v1/wod` 获取训练方案（无需认证），指定 `sport` 和 `duration` 参数
2. 配置环境变量 `HEALTH_API_KEY`，通过 `GET /api/v1/workouts` 查询训练记录（YYYY-MM-DD格式，最大90天）
3. 通过 `GET /api/v1/profile` 获取运动员档案信息
4. 如需AI教练对话、性能管理图表或性能统计功能，升级至完整版

#
## 示例

### 示例1：获取训练方案（无需认证）

```bash
# 获取45分钟跑步训练方案
curl "https://health-api.example.com/api/v1/wod?sport=run&duration=45"
# 响应包含结构化训练计划：热身、主训练、放松等阶段
# ...
# 获取30分钟力量训练方案
curl "https://health-api.example.com/api/v1/wod?sport=strength&duration=30"
```

### 示例2：查询训练记录

```bash
# 获取最近一周的训练记录
curl -H "X-API-Key: $HEALTH_API_KEY" \
  "https://health-api.example.com/api/v1/workouts?start=2026-02-09&end=2026-02-15"
# 响应包含训练类型、时长、距离、心率等数据
# ...
# 获取运动员档案
curl -H "X-API-Key: $HEALTH_API_KEY" \
  "https://health-api.example.com/api/v1/profile"
```

## 错误处理

| 错误场景 | HTTP状态 | 原因 | 处理方式 |
|---:|---:|---:|---:|
| API Key未设置 | 401 | `HEALTH_API_KEY` 环境变量缺失或为空 | 在健康数据同步服务中生成API Key并设置环境变量 |
| 日期范围超过90天 | 400 | `start` 和 `end` 间隔超过最大范围 | 将查询范围缩小到90天以内，分段查询 |
| 日期格式错误 | 400 | `start` 或 `end` 非YYYY-MM-DD格式 | 使用标准日期格式，如 `2026-02-09` |
| sport参数无效 | 400 | 传入了不支持的sport值 | 使用有效值：`run`/`bike`/`swim`/`strength` |
| duration超出范围 | 400 | duration不在10-300分钟范围内 | 调整duration值到10-300范围内，默认45分钟 |
| 免费配额用尽 | 429 | 超出100次/天读取限制 | 等待次日重置，或升级至完整版获取10000次/天配额 |
| 请求AI教练功能 | 403 | 免费版不支持 `POST /api/v1/coach/chat` | 升级至完整版以使用AI教练对话功能 |

## 常见问题

### Q1: WOD端点需要认证吗？

不需要。`GET /api/v1/wod` 是唯一无需认证的端点。参数 `sport` 支持 `run`/`bike`/`swim`/`strength`（默认 `run`），`duration` 范围10-300分钟（默认45）。适用于快速获取训练方案，无需配置API Key.
### Q2: 如何获取API Key？

在健康数据同步服务应用中，进入 Settings > API Keys，点击 Generate New Key 生成密钥。将生成的密钥设置到环境变量 `HEALTH_API_KEY` 中。认证端点（`workouts`、`profile`）需在请求头中携带 `X-API-Key: $HEALTH_API_KEY`.
### Q3: 免费版可以查询训练记录吗？

可以。`GET /api/v1/workouts` 支持查询训练记录，免费版配额100次/天。参数 `start` 和 `end` 使用YYYY-MM-DD格式，最大查询范围90天。返回训练类型、时长、距离、心率等详细数据.
### Q4: 免费版可以使用AI教练吗？

不可以。`POST /api/v1/coach/chat` AI教练对话是完整版独有功能。免费版仅支持训练方案生成、训练记录查询和运动员档案获取。如需AI教练对话，请升级至完整版.
### Q5: 免费版可以查看性能管理图表吗？

不可以。`GET /api/v1/performance/pmc`（CTL/ATL/TSB训练负荷数据）和 `GET /api/v1/performance/stats`（FTP、心率区间等）是完整版独有功能。如需性能分析和训练负荷监控，请升级至完整版.
### Q6: 日期格式有什么要求？

所有日期参数使用YYYY-MM-DD格式（如 `2026-02-09`）。`GET /api/v1/workouts` 端点的 `start` 和 `end` 参数之间的最大查询范围为90天，超过会返回400错误。需要查询更长时间范围时，分段多次查询.
## 已知限制

- 不支持AI教练对话（`POST /api/v1/coach/chat`），完整版可用
- 不支持性能管理图表（`GET /api/v1/performance/pmc`），完整版可用
- 不支持性能统计（`GET /api/v1/performance/stats`），完整版可用
- 不支持聊天历史（`GET /api/v1/coach/history`），完整版可用
- 训练记录查询最大范围90天，超长范围需分段查询
- 免费版读取配额100次/天，需等待次日重置

## 输出格式

```json
{
  "success": true,
  "data": {
    "result": "运动健康数据基础版处理结果",
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
