---
slug: "bailian-web-search"
name: "bailian-web-search"
version: 1.0.5
displayName: "Bailian Web Search"
summary: "调百炼(阿里ModelStudio)API做AI优化网搜,多源精炼结果"
license: "Proprietary"
description: |-
  AI-optimized web search via Bailian(Alibaba ModelStdio) API。Returns
  multisourced, concise web se。Use when 需要AI模型调用、智能对话、Agent编排、LLM应用时使用。不适用于需要100%确定性的关键决策.
tags:
  - Research
tools:
  - read
  - exec
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "9.9 CNY/per_use"
pricing_tier: "L1-入门级"
pricing_model: "per_use"

---
# Bailian Web Search

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| 大数据集流式处理 | 不支持 | 支持 |
| 多数据源关联查询 | 不支持 | 支持 |
| 可视化图表自动生成 | 不支持 | 支持 |
| 定时数据同步与增量更新 | 不支持 | 支持 |

## 核心能力

- AI-optimized web search via Bailian(Alibaba ModelStdio) API
- Returns
  multisourced, concise web se
#
## 适用场景

| 场景 | 输入 | 输出 |
|:-----|:-----|:-----|
| 场景1: 调百炼(阿里ModelStudio)API做AI优化网搜 | 用户请求数据 | 结构化处理结果 |
| 场景2: 多源精炼结果 | 用户请求数据 | 结构化处理结果 |

**不适用于**：需要人工判断的复杂决策场景

## 使用流程

1. **构建API请求**: 根据用户输入组装API请求参数与请求头
2. **调用服务接口**: 发送HTTP请求到目标服务端点,处理响应或超时
3. **解析响应数据**: 提取API返回的关键字段,转换为用户可读格式
4. **异常处理**: 如遇错误,参考错误处理章节中对应场景的处理方式

## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---:|---:|---:|---:|

## 输出格式

```json
{
  "success": true,
  "data": {
    result: "search 相关配置参数",
    result: "search 相关配置参数"
  },
  "error": null
}
```

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
## 错误处理

| 错误场景2 | 原因 | 处理方式 |
|---:|:---|---:|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## FAQ

### 如何开始使用？

阅读使用流程章节,按步骤配置环境和参数后即可开始使用。首次使用建议先阅读依赖说明章节确认环境就绪.
### 遇到错误怎么办？

查看错误处理章节,对照错误场景找到对应的处理方式。如错误处理章节未覆盖,收集错误信息后通过已知限制章节了解skill能力边界.
## 已知限制

- 需要API Key，无Key环境无法使用
- 
