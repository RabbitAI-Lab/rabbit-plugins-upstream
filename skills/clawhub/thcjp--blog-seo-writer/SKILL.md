---
slug: "blog-seo-writer"
name: "blog-seo-writer"
version: 1.0.1
displayName: "blog-seo-writer"
summary: "写Google高排名SEO博文,内置关键词/元描述/结构化,流量可期"
license: "Proprietary"
description: |-
  Create SEO-optimized blog posts that rank higher on Google。Includes
  keyword integration, meta de。Use when 需要SEO优化、关键词分析、排名提升、搜索流量优化时使用。不适用于黑帽SEO手段.
tags:
  - Productivity
tools:
  - read
  - exec
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "19.9 CNY/per_use"
pricing_tier: "L2-标准级"
pricing_model: "per_use"

---
# blog-seo-writer

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| 跨平台任务同步 | 不支持 | 支持 |
| 智能优先级排序 | 不支持 | 支持 |
| 团队协作与权限管理 | 不支持 | 支持 |
| 自动化提醒与跟进 | 不支持 | 支持 |

## 核心能力

- Create SEO-optimized blog posts that rank higher on Google
- Includes
  keyword integration, meta de
#
## 适用场景

| 场景 | 输入 | 输出 |
|:-----|:-----|:-----|
| SEO博文生成 | 关键词和目标主题 | SEO优化博文和元数据 |
| 关键词分析 | 目标关键词列表 | 搜索量和竞争度分析 |
| 内容优化 | 现有博文内容 | SEO改进建议和优化版本 |

**不适用于**：非SEO导向的技术文档和API文档编写

## 使用流程

1. **解析输入参数**: 读取用户提供的输入数据,校验参数完整性与格式合法性
2. **执行核心处理**: 调用skill核心逻辑对输入数据进行加工或转换
3. **验证并返回结果**: 检查输出结果的完整性与格式,返回结构化数据
4. **异常处理**: 如遇错误,参考错误处理章节中对应场景的处理方式

## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---:|---:|---:|---:|
| keywords | string | 是 | 目标SEO关键词, 逗号分隔 |
| content_tone | string | 否 | 内容语气, 可选: professional/casual/technical, 默认: professional |

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
## 案例展示

### 示例1: 基础用法
**输入**:
```json
{
  "content": "示例内容",
  "strict_level": "normal"
}
```
**输出**:
```
评级: B级(良好) - 总分: 85/100
# ...
检查详情:
- 代码风格: 通过(95分) - 检查通过
- 安全合规: 警告(75分) - 检查通过
- 无障碍性: 通过(85分) - 检查通过
# ...
改进建议:
1. [高优先级] 建议优化
2. [中优先级] 建议优化
```

### 示例2: 进阶用法
**输入**:
```json
{
  "content": "示例内容",
  "strict_level": "strict"
}
```
**输出**:
```
评级: C级(及格) - 总分: 70/100
# ...
检查详情:
- 代码风格: 通过(90分) - 检查通过
- 安全合规: 不通过(50分) - 检查通过
- 无障碍性: 警告(70分) - 检查通过
# ...
改进建议:
1. [高优先级] 建议优化
2. [高优先级] 建议优化
3. [低优先级] 建议优化
```

### 示例3: 边界情况 - 边界情况
**输入**:
```json
{
  "content": "示例内容"
}
```
**输出**:
```
评级: D级(不及格) - 总分: 45/100
# ...
检查详情:
- 代码风格: 不通过(40分) - 检查通过
- 安全合规: 不通过(30分) - 检查通过
- 无障碍性: 通过(65分) - 检查通过
# ...
改进建议:
1. [紧急] 建议优化
2. [高优先级] 建议优化
```

## 常见问题

### Q1: 如何开始使用blog-seo-writer？
A: 

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|:------|------:|:------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

- 需要API Key，无Key环境无法使用
