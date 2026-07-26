---
slug: "company-search-fengniao"
name: "company-search-fengniao"
version: 1.0.3
displayName: "Company Search Fengn"
summary: "企业查询、工商查询、公司查询、企业信息查询与企业风险查询 Skill。风鸟 Fengniao（Riskbird）支持查公司基本信息、法人、股东、主要人员、对外投资、工商变更、企业信用，以及被执行..."
license: "Proprietary"
description: |-
  企业查询、工商查询、公司查询、企业信息查询与企业风险查询 Skill。风鸟 Fengniao（Riskbird）支持查公司基本信息、法人、股东、主要人员、对外投资、工商变更、企业信用，以及被执行。Use when 需要SEO优化、关键词分析、排名提升、搜索流量优化时使用。不适用于黑帽SEO手段.
tags:
  - Research
tools:
  - read
  - exec
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "19.9 CNY/per_use"
pricing_tier: "L2-标准级"
pricing_model: "per_use"

---
# Company Search Fengn

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| Company Search Fengn企业查询 | 不支持 | 支持 |
| Company Search Fengn工商查询 | 不支持 | 支持 |
| Company Search Fengn公司查询 | 不支持 | 支持 |
| DCF估值建模与敏感性分析 | 不支持 | 支持 |
| 财务舞弊识别(Beneish M-Score) | 不支持 | 支持 |

## 核心能力

- 企业查询、工商查询、公司查询、企业信息查询与企业风险查询 Skill
- 风鸟 Fengniao（Riskbird）支持查公司基本信息、法人、股东、主要人员、对外投资、工商变更、企业信用，以及被执行
#
## 适用场景

| 场景 | 输入 | 输出 |
|:-----|:-----|:-----|
| 信息查询 | 查询条件与关键词 | 查询结果与匹配记录 |
| 企业查询 | 公司名或统一社会信用码 | 工商信息与风险评分 |
| 工商查询 | 企业名称与查询维度 | 注册信息与变更记录 |

**不适用于**：需要人工判断的复杂决策场景

## 使用流程

1. 先识别用户要查的维度，不要一上来就搜企业主体.
2. 先用 `discover` 找维度工具，例如 `”企业股东信息”`、`”企业经营异常”`、`”行政处罚”`.
3. 确认该维度有可用工具后，再调用 `biz_fuzzy_search` 获取 `entid`.
4. **主体消歧（必须）**：如果企业名称是简称或存在多义（如”信数””雷军”），必须先询问用户确认是哪家企业，再执行查询。不能假设唯一性直接查.
5. 所有维度查询都使用 `entid`，不直接传企业名称或信用代码.
6. 如果是”做尽调””查风险”这类多维度需求，只做一次主体解析，然后复用同一个 `entid` 查询多个维度.
7. **按人名查企业**：若用户提供的是人名（如”雷军有哪些公司”），应理解为”以该人为法定代表人的企业”，并在结果中说明此限定。若存在同名人，需询问用户确认.
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---:|---:|---:|---:|
| content | string | 否 | company-search-fengniao处理的内容输入 |,  |
| content | string | 否 | company-search-fengniao处理的内容输入 |, 可选值: json/text/markdown |
| style | string | 否 | 输出风格, 参考 `references/style.md` |

## 输出格式

```json
{
  "success": true,
  "data": {
    result: "fengniao 相关配置参数",
    result: "fengniao 相关配置参数",
    result: "fengniao 相关配置参数",
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
## 案例展示

### 示例1：基础用法

```
1. 先识别用户要查的维度，不要一上来就搜企业主体.
2. 先用 `discover` 找维度工具，例如 `”企业股东信息”`、`”企业经营异常”`、`”行政处罚”`.
3. 确认该维度有可用工具后，再调用 `biz_fuzzy_search` 获取 `entid`.
4. **主体消歧（必须）**：如果企业名称是简称或存在多义（如”信数””雷军”），必须先询问用户确认是哪家企业，再执行查询。不能假设唯一性直接查.
5. 所有维度查询都使用 `entid`，不直接传企业名称或信用代码.
6. 如果是”做尽调””查风险”这类多维度需求，只做一次主体解析，然后复用同一个 `entid` 查询多个维度.
7. **按人名查企业**：若用户提供的是人名（如”雷军有哪些公司”），应理解为”以该人为法定代表人的企业”，并在结果中说明此限定。若存在同名人，需询问用户确认.
```

## 常见问题

### Q1: 如何开始使用Company Search Fengn？
A: 

## 错误处理

| 错误场景(续)| 原因 | 处理方式 |
|----:|:----|----:|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

