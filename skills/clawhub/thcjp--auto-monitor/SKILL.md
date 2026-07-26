---
slug: "auto-monitor"
name: "auto-monitor"
version: 1.0.1
displayName: "Auto Monitor"
summary: "主动监控系统状态。定期检查服务器健康，主动汇报，无需等待指令。"
license: "Proprietary"
description: |-
  主动监控系统状态。定期检查服务器健康，主动汇报，无需等待指令。Use when 需要系统监控、日志分析、运维告警、部署管理时使用。不适用于物理硬件维修。Use when 需要系统监控、日志分析、运维告警、部署管理时使用。不适用于物理硬件维修.
tags:
  - Operations
tools:
  - read
  - exec
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "9.9 CNY/per_use"
pricing_tier: "L1-入门级"
pricing_model: "per_use"

---
# Auto Monitor

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| Auto Monitor主动监控 | 不支持 | 支持 |
| 多源数据聚合与去重 | 不支持 | 支持 |
| 语义搜索与智能摘要 | 不支持 | 支持 |
| 定时监控与变化推送 | 不支持 | 支持 |
| 研究结论结构化导出 | 不支持 | 支持 |

## 核心能力

- 定期检查服务器健康，主动汇报，无需等待指令
#
## 适用场景

| 场景 | 输入 | 输出 |
|:-----|:-----|:-----|
| 场景1: 主动监控系统状态 | 用户请求数据 | 结构化处理结果 |
| 场景2: 定期检查服务器健康 | 用户请求数据 | 结构化处理结果 |
| 场景3: 无需等待指令 | 用户请求数据 | 结构化处理结果 |

**不适用于**：需要人工判断的复杂决策场景

## 使用流程

1. **构建API请求**: 根据用户输入组装API请求参数与请求头
2. **调用服务接口**: 发送HTTP请求到目标服务端点,处理响应或超时
3. **解析响应数据**: 提取API返回的关键字段,转换为用户可读格式
4. **异常处理**: 如遇错误,参考错误处理章节中对应场景的处理方式

## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---:|---:|---:|---:|
| content | string | 否 | auto-monitor处理的内容输入 |,  |
| content | string | 否 | auto-monitor处理的内容输入 |, 可选值: json/text/markdown |
| style | string | 否 | 输出风格, 参考 `references/style.md` |

## 输出格式

```json
{
  "success": true,
  "data": {
    result: "monitor 相关配置参数",
    result: "monitor 相关配置参数",
    result: "monitor 相关配置参数",
    "metadata": {
      "template_used": "reviewer",
      "word_count": 0,
      "style": "专业"
    }
  },
  "error": null
}
```

输出模板参考: `assets/output.json`

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
## 常见问题

### Q1: 如何开始使用Auto Monitor？
A: 

## 错误处理

| 错误场景2 | 原因 | 处理方式 |
|---:|:---|---:|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

