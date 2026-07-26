---
slug: "clawddocs"
name: "clawddocs"
version: 1.2.3
displayName: "Clawddocs"
summary: "SkillHub文档专家,带决策树导航,快速定位答案"
license: "Proprietary"
description: |-
  SkillHub documentation expert with decision tree navigation。核心能力:

  - 知识管理领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 知识捕获、文档管理、信息整理

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助
tags:
  - Knowledge
tools:
  - read
  - exec
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "29.9 CNY/per_use"
pricing_tier: "L3-专业级"
pricing_model: "per_use"

---
# Clawddocs

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| 复杂工作流可视化编排 | 不支持 | 支持 |
| 条件分支与异常重试 | 不支持 | 支持 |
| 定时触发与事件驱动 | 不支持 | 支持 |
| 执行日志与审计追踪 | 不支持 | 支持 |
| 分布式任务调度与负载均衡 | 不支持 | 支持 |

## 核心能力

- SkillHub documentation expert with decision tree navigation
#
## 适用场景

| 场景 | 输入 | 输出 |
|:-----|:-----|:-----|
| 文档处理 | 文件路径与格式选项 | 转换结果与页面信息 |
| 文档导航 | 问题与知识库范围 | 答案与参考链接 |
| SkillHub文档 | 目标数据与配置参数 | 处理结果与执行状态 |

**不适用于**：需要人工判断的复杂决策场景

## 使用流程

"When a user asks about SkillHub, first identify what they need:"

### 🎯 Decision Tree

1. **"How do I set up X?"** → Check `providers/` or `start/`

  + Discord, Telegram, WhatsApp, etc. → `providers/<name>`
  + First time? → `start/getting-started`, `start/setup`
2. **"Why isn't X working?"** → Check troubleshooting

  + General issues → `debugging`, `gateway/troubleshooting`
  + Provider-specific → `providers/troubleshooting`
  + Browser tool → `tools/browser-linux-troubleshooting`
3. **"How do I configure X?"** → Check `gateway/` or `concepts/`

  + Main config → `gateway/configuration`, `gateway/configuration-examples`
  + Specific features → relevant `concepts/` page
4. **"What is X?"** → Check `concepts/`

  + Architecture, sessions, queues, models, etc.
5. **"How do I automate X?"** → Check `automation/`

  + Scheduled tasks → `automation/cron-jobs`
  + Webhooks → `automation/webhook`
  + Gmail → `automation/gmail-pubsub`
6. **"How do I install/deploy?"** → Check `install/` or `platforms/`

  + Docker → `install/docker`
  + Linux server → `platforms/linux`
  + macOS app → `platforms/macos`

**结果验证**: 任务完成后,查看输出确认状态。成功时返回摘要和数据;失败时根据错误信息排查,参考恢复章节获取修复步骤.
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---:|---:|---:|---:|
| content | string | 否 | clawddocs处理的内容输入 |,  |
| mode | string | 否 | 处理模式, 可选: json/text/markdown,  |
| max_retries | integer | 否 | 单步最大重试次数, 默认: 2 |
| skip_steps | array | 否 | 跳过的步骤编号(用于断点续传), 默认: [] |

## 输出格式

```json
{
  "success": true,
  "data": {
    "final_result": {
      "clawddocs_result": "clawddocs_result_value",
      "clawddocs_metadata": "clawddocs_metadata_value",
      "clawddocs_status": "clawddocs_status_value"
    },
    "execution_log": [
      {
        "step": 1,
        "name": "按流程执行",
        "status": "completed",
        "duration_ms": 1200,
        "output_summary": "按流程执行"
      },
      {
        "step": 2,
        "name": "按流程执行",
        "status": "completed",
        "duration_ms": 3500,
        "output_summary": "按流程执行"
      },
      {
        "step": 3,
        "name": "按流程执行",
        "status": "completed",
        "duration_ms": 2100,
        "output_summary": "按流程执行"
      },
      {
        "step": 4,
        "name": "按流程执行",
        "status": "completed",
        "duration_ms": 800,
        "output_summary": "按流程执行"
      }
    ],
    "total_duration_ms": 7600,
    "gates_passed": 3,
    "gates_total": 3
  },
  "error": null
}
```

中间产物模板参考: `assets/clawddocs_template`

## 异常处理

| 错误场景 | 原因 | 处理方式 |
|:---:|:---:|:---:|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux

### 依赖说明(补充)
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:------|------:|:------|:------|
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
## 案例展示

**User:** "How do I make my bot only respond when mentioned in Discord?"

**You:**

1. Fetch `providers/discord` doc
2. Find the `requireMention` setting
3. Provide the config snippet:

```json
{
  "discord": {
    "guilds": {
      "*": {
        "requireMention": true
      }
    }
  }
}
```

4. Link: <https://docs.clawd.bot/providers/discord>

**User:** "What's new in the docs?"

**You:**

1. Run `（请参考skill目录中的脚本文件） 7`
2. Summarize recently updated pages
3. Offer to dive into any specific updates

## 常见问题

### Q1: 如何开始使用Clawddocs？
A: 

## 错误处理

| 错误场景(续)| 原因 | 处理方式 |
|----:|:----|----:|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

