---
slug: "agent-browser-stagehand"
name: "agent-browser-stagehand"
version: 1.0.1
displayName: "Agent Browser Stageh"
summary: "自然语言驱动浏览器自动化,CLI直达交互,免去手写选择器的繁琐"
license: "Proprietary"
description: |-
  Automate web browser interactions using natural language via CLI commands。Use when the user asks。Use when 需要文本翻译、多语言转换、本地化处理时使用。不适用于专业医学法律翻译认证.
tags:
  - Research
  - Automation
tools:
  - read
  - exec
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "9.9 CNY/per_use"
pricing_tier: "L1-入门级"
pricing_model: "per_use"

---
# Agent Browser Stageh

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| 多标签页并行抓取 | 不支持 | 支持 |
| 反爬虫策略自动绕过 | 不支持 | 支持 |
| 页面结构变化自适应 | 不支持 | 支持 |
| 批量导出结构化数据 | 不支持 | 支持 |

## 核心能力

- Automate web browser interactions using natural language via CLI commands
- Use when the user asks
#
## 适用场景

| 场景 | 输入 | 输出 |
|:-----|:-----|:-----|
| 场景1: 自然语言驱动浏览器自动化 | 用户请求数据 | 结构化处理结果 |
| 场景2: CLI直达交互 | 用户请求数据 | 结构化处理结果 |
| 场景3: 免去手写选择器的繁琐 | 用户请求数据 | 结构化处理结果 |

**不适用于**：需要人工判断的复杂决策场景

## 使用流程

1. **初始化浏览器会话**: 启动无头浏览器实例,配置代理与用户代理参数
2. **执行页面交互**: 按照用户指令进行导航/点击/输入/提取等页面操作
3. **采集与返回数据**: 提取页面内容或操作结果,返回结构化数据与截图
4. **异常处理**: 如遇错误,参考错误处理章节中对应场景的处理方式

## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---:|---:|---:|---:|
| content | string | 否 | agent-browser-stagehand处理的内容输入 |,  |
| mode | string | 否 | 处理模式, 可选: json/text/markdown,  |
| max_retries | integer | 否 | 单步最大重试次数, 默认: 2 |
| skip_steps | array | 否 | 跳过的步骤编号(用于断点续传), 默认: [] |

## 输出格式

```json
{
  "success": true,
  "data": {
    "final_result": {
      "stagehand_result": "stagehand_result_value",
      "stagehand_metadata": "stagehand_metadata_value",
      "stagehand_status": "stagehand_status_value"
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

中间产物模板参考: `assets/agent-browser-stagehand_template`

## 异常处理

| 错误场景 | 原因 | 处理方式 |
|:---:|:---:|:---:|
| 页面加载超时 | 目标网站响应慢或网络延迟 | 增加超时阈值,启用重试机制,检查代理配置 |
| 页面结构变化导致选择器失效 | 目标网站更新了DOM结构 | 切换到可访问性树定位元素,或提示用户提供新的选择器 |
| 反爬虫机制触发 | 频繁请求被目标站点识别 | 降低请求频率,启用随机延迟,更换User-Agent |

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

```bash
browser navigate https://example.com
browser act "click the Sign In button"
browser extract "get the page title"
browser close
```

## 常见问题

### Q1: 如何开始使用Agent Browser Stageh？
A: 

## 错误处理

| 错误场景2 | 原因 | 处理方式 |
|---:|:---|---:|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

