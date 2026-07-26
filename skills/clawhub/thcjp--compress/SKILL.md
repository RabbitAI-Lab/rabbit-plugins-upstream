---
slug: "compress"
name: "compress"
version: 1.0.1
displayName: "Compress"
summary: "语义压缩文本,迭代校验+锚点校验和,信息无损瘦身"
license: "Proprietary"
description: |-
  Compress text semantically with iterative validation, anchor checksums,
  and verified information 。Use when 用户需要Compress相关功能时使用。不适用于超出本技能能力范围的复杂需求.
tags:
  - Other
tools:
  - read
  - exec
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "9.9 CNY/per_use"
pricing_tier: "L1-入门级"
pricing_model: "per_use"

---
# Compress

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| Compress语义压缩 | 不支持 | 支持 |
| Compress迭代校验 | 不支持 | 支持 |
| Compress锚点校验 | 不支持 | 支持 |
| 复杂工作流可视化编排 | 不支持 | 支持 |
| 条件分支与异常重试 | 不支持 | 支持 |

## 核心能力

- Compress text semantically with iterative validation, anchor checksums,
  and verified information
#
## 适用场景

| 场景 | 输入 | 输出 |
|:-----|:-----|:-----|
| 语义压缩 | 长文本内容和压缩目标 | 压缩后文本和锚点校验 |
| 迭代验证 | 压缩文本和原始内容 | 压缩质量评分和损失分析 |
| 锚点校验 | 压缩文本和校验和 | 完整性验证和恢复信息 |

**不适用于**：需要无损还原的精确保密通信场景

## 使用流程

1. 确认运行环境满足依赖说明中的要求
2. 根据适用场景选择合适的使用方式
3. 执行操作并检查输出结果
4. 如遇错误，参考错误处理章节

## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---:|---:|---:|---:|
| text_content | string | 是 | 待压缩的文本内容 |
| compression_ratio | string | 否 | 目标压缩比, 如: 50%/30%, 默认: 50% |

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

### Q1: 如何开始使用Compress？
A: 

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|:------|------:|:------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

**This is SEMANTIC compression, not bit-perfect lossless.**

* L1-L2: Verified reconstruction, production-ready
* L3-L4: Experimental, may lose subtle information
* **Never use for:** Medical dosages, legal text, financial figures, safety-critical data

---
