---
slug: "chart-generator-2-0-0"
name: "chart-generator-2-0-0"
version: 1.0.1
displayName: "Chart Generator 2 0"
summary: "数据可视化出SVG图表,柱/线/饼图即需即出"
license: "Proprietary"
description: |-
  Data visualization tool producing SVG charts。Use when you need bar
  charts, line charts, pie char。Use when 需要数据分析、报表生成、统计洞察、数据可视化时使用。不适用于实时流数据处理.
tags:
  - Other
tools:
  - read
  - exec
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "19.9 CNY/per_use"
pricing_tier: "L2-标准级"
pricing_model: "per_use"

---
# Chart Generator 2 0

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| 高清分辨率与无损输出 | 不支持 | 支持 |
| 批量生成与风格预设 | 不支持 | 支持 |
| 自定义模型微调 | 不支持 | 支持 |
| 商用版权授权 | 不支持 | 支持 |
| 多版本对比与A/B优选 | 不支持 | 支持 |

## 核心能力

- Data visualization tool producing SVG charts
- Use when you need bar
  charts, line charts, pie char
- 0, charts, producing
#
## 适用场景

| 场景 | 输入 | 输出 |
|:-----|:-----|:-----|
| 数据处理 | 数据源与处理规则 | 清洗结果与统计摘要 |
| 图表生成 | 数据集与图表类型 | SVG图表文件 |
| 数据可视化 | 数值序列与维度 | 可视化图表与图例 |

**不适用于**：需要人工判断的复杂决策场景

## 使用流程

1. 确认运行环境满足依赖说明中的要求
2. 根据适用场景选择合适的使用方式
3. 执行操作并检查输出结果
4. 如遇错误，参考错误处理章节

#
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---:|---:|---:|---:|
| content | string | 否 | chart-generator-2-0-0处理的内容输入 |,  |
| content | string | 否 | chart-generator-2-0-0处理的内容输入 |, 可选值: json/text/markdown |
| style | string | 否 | 输出风格, 参考 `references/style.md` |

## 输出格式

```json
{
  "success": true,
  "data": {
    result: "0 相关配置参数",
    result: "0 相关配置参数",
    result: "0 相关配置参数",
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

### 柱状图 (bar)

```text
$ chart.sh bar "销售:85,市场:62,研发:93,运维:41" --title "部门预算(万)"
# ...
  部门预算(万)
  销售  ████████████████████░  85
  市场  ███████████████░░░░░░  62
  研发  ██████████████████████ 93
  运维  ██████████░░░░░░░░░░░  41
```

### 迷你趋势图 (sparkline)

```text
$ chart.sh sparkline "3,7,2,8,5,9,1,6"
▃▆▁█▄█▁▅
```

---

💬 Feedback & Feature Requests: <https://bytesagain.com/feedback>
Powered by BytesAgain | bytesagain.com

## 常见问题

### Q1: 如何开始使用Chart Generator 2 0？
A: 

## 错误处理

| 错误场景(续)| 原因 | 处理方式 |
|----:|:----|----:|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

