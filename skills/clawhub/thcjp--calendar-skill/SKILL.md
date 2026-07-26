---
slug: "calendar-skill"
name: "calendar-skill"
version: 1.0.5
displayName: "Calendar"
summary: "安全管理Google日历/Outlook/Exchange,一处排程多端同步"
license: "Proprietary"
description: |-
  Calendar Management - secure Google Calendar, Microsoft Outlook & Exchange。Use when the user wan。Use when 需要项目管理、任务规划、进度跟踪、团队协作时使用。不适用于实际人员绩效评估.
tags:
  - Productivity
tools:
  - read
  - exec
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "29.9 CNY/per_use"
pricing_tier: "L3-专业级"
pricing_model: "per_use"

---
# Calendar

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| Calendar安全管理 | 不支持 | 支持 |
| 深度漏洞扫描与CVE关联 | 不支持 | 支持 |
| 安全基线合规审计 | 不支持 | 支持 |
| 批量资产风险评分 | 不支持 | 支持 |
| 威胁情报实时订阅与告警 | 不支持 | 支持 |

## 核心能力

- Calendar Management - secure Google Calendar, Microsoft Outlook & Exchange
- Use when the user wan
#
## 适用场景

| 场景 | 输入 | 输出 |
|:-----|:-----|:-----|
| 安全日历管理 | 日历凭据和事件信息 | 加密日历事件和访问控制 |
| 跨平台同步 | Google/Outlook/Exchange账户 | 多平台日历合并视图 |
| 会议调度 | 参会者日程和会议室 | 最优会议时间和预约确认 |

**不适用于**：无日历API访问权限的离线日程规划

## 使用流程

1. **登录与鉴权**: 验证用户身份与权限,加载平台配置信息
2. **选择操作模块**: 根据用户意图定位目标功能模块与管理对象
3. **执行管理操作**: 调用平台API执行创建/修改/查询/删除操作并返回结果
4. **异常处理**: 如遇错误,参考错误处理章节中对应场景的处理方式

## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---:|---:|---:|---:|
| provider | string | 是 | 日历服务提供商, 可选: google/outlook/exchange |
| timezone | string | 否 | 时区设置, 如: Asia/Shanghai, 默认: 系统时区 |

## 输出格式

```json
{
  "success": true,
  "data": {
    "overall_grade": "A",
    "total_score": 92,
    "max_score": 100,
    "summary": "处理完成",
    "details": [
      {
        "item": "代码风格",
        "status": "pass",
        "score": 95,
        "comment": "符合规范"
      },
      {
        "item": "安全合规",
        "status": "warn",
        "score": 80,
        "comment": "符合规范"
      }
    ],
    "improvements": [
      {
        "priority": "high",
        "suggestion": "建议优化",
        "expected_gain": "+5分"
      },
      {
        "priority": "medium",
        "suggestion": "建议优化",
        "expected_gain": "+3分"
      }
    ]
  },
  "error": null
}
```

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux

### 工具依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:---:|:---:|:---:|:---:|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 

### 可用性分类
- **分类**: MD+EXEC()
- **说明**: 基于Markdown的AI Skill,

**API Key配置方式**:
```bash
export API_KEY="your_api_key_here"
```
配置后需重启会话或开启新终端生效。API Key应妥善保管,避免泄露到版本控制系统.
## 常见问题

### Q1: 如何开始使用Calendar？
A: 

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|:------|------:|:------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

