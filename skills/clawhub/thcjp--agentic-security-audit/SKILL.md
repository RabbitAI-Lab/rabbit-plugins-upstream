---
slug: "agentic-security-audit"
name: "agentic-security-audit"
version: 1.0.1
displayName: "Agentic Security Aud"
summary: "审计代码库/基础设施/Agent AI系统安全,覆盖传统与新型风险,一键出报告"
license: "Proprietary"
description: |-
  Audit codebases, infrastructure, AND agentic AI systems for security
  issues。Covers traditional s。Use when 需要安全检测、合规审计、漏洞扫描、加密防护时使用。不适用于渗透测试未授权目标.
tags:
  - Security
  - Agents
tools:
  - read
  - exec
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "29.9 CNY/per_use"
pricing_tier: "L3-专业级"
pricing_model: "per_use"

---
# Agentic Security Aud

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| 深度漏洞扫描与CVE关联 | 不支持 | 支持 |
| 安全基线合规审计 | 不支持 | 支持 |
| 批量资产风险评分 | 不支持 | 支持 |
| 威胁情报实时订阅与告警 | 不支持 | 支持 |

## 核心能力

- Audit codebases, infrastructure, AND agentic AI systems for security
  issues
- Covers traditional s
#
## 适用场景

| 场景 | 输入 | 输出 |
|:-----|:-----|:-----|
| 代码库安全审计 | 源代码仓库路径或URL | 安全漏洞清单和修复优先级 |
| 基础设施审计 | 云资源配置和部署清单 | 基础设施安全评估和合规报告 |
| AI Agent安全审查 | Agent系统架构和工具定义 | Agent安全风险和缓解措施 |

**不适用于**：非安全相关的功能测试和性能优化场景

## 使用流程

1. **解析输入参数**: 读取用户提供的输入数据,校验参数完整性与格式合法性
2. **执行核心处理**: 调用skill核心逻辑对输入数据进行加工或转换
3. **验证并返回结果**: 检查输出结果的完整性与格式,返回结构化数据
4. **异常处理**: 如遇错误,参考错误处理章节中对应场景的处理方式

## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---:|---:|---:|---:|
| target_path | string | 是 | 待审计的目标路径或代码库URL |
| audit_scope | string | 否 | 审计范围, 可选: code/infra/agent/all, 默认: all |

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

### Q1: 如何开始使用Agentic Security Aud？
A: 

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|:------|------:|:------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

