---
name: "Agent Browser Assistant 核心处理"
slug: "agent-browser-assistant"
displayName: "浏览器代理助手"
version: 0.1.1
summary: "AI浏览器代理助手,自动化网页交互与数据采集,支持复杂页面操作流程"
description: |-
  API封装工具。适用于需要调用外部API的场景，API请求参数→API响应数据.
  Use when 用户说"Agent Browser Assistant 智能分析"、Agent Browser Assistant 智能分析时使用.
  不适用于需要人工判断的复杂场景.
license: "Proprietary"
tools:
  - read
  - exec
homepage: "https://skillhub.cn"
tags:
  - 智能助手
# 定价元数据
suggested_price: "29.9 CNY/per_use"
pricing_tier: "L3-专业级"
pricing_model: "per_use"

---
# Agent Browser Assistant 批量处理

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| 浏览器代理助手化网页交互与数据采集 | 不支持 | 支持 |
| 多标签页并行抓取 | 不支持 | 支持 |
| 反爬虫策略自动绕过 | 不支持 | 支持 |
| 页面结构变化自适应 | 不支持 | 支持 |
| 批量导出结构化数据 | 不支持 | 支持 |

## 核心能力

- Agent Browser Assistant 错误重试
- Agent Browser Assistant 多格式支持
- Agent Browser Assistant 扩展能力9
#
## 适用场景

- 用户说"Agent Browser Assistant 扩展能力10" → 执行API调用
- 用户说"Agent Browser Assistant 扩展能力11" → 执行API调用
- 用户说"Agent Browser Assistant 扩展能力12" → 执行API调用
- 不适用: 需要人工判断的复杂场景

## 使用流程

### Step 1: 初始化浏览器会话
启动无头浏览器实例,配置代理与用户代理参数
### Step 2: 执行页面交互
按照用户指令进行导航/点击/输入/提取等页面操作
### Step 3: 采集与返回数据
提取页面内容或操作结果,返回结构化数据与截图
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|:-----|:-----|:-----|:-----|

## 输出格式

```json
{
  "success": true,
  "data": {
    result: "assistant 相关配置参数",
    result: "assistant 相关配置参数"
  },
  "error": null
}
```

## 异常处理

| 错误场景 | 原因 | 处理方式 |
|---:|---:|---:|
| 页面加载超时 | 目标网站响应慢或网络延迟 | 增加超时阈值,启用重试机制,检查代理配置 |
| 页面结构变化导致选择器失效 | 目标网站更新了DOM结构 | 切换到可访问性树定位元素,或提示用户提供新的选择器 |
| 反爬虫机制触发 | 频繁请求被目标站点识别 | 降低请求频率,启用随机延迟,更换User-Agent |

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux

### 依赖项
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:---:|:---:|:---:|:---:|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
需要配置对应API Key，详见上文环境配置章节

### 可用性分类
- **分类**: MD+EXEC（）

**API Key配置方式**:
```bash
export API_KEY="your_api_key_here"
```
配置后需重启会话或开启新终端生效。API Key应妥善保管,避免泄露到版本控制系统.
## 案例展示

### 示例1: 基础用法
**输入**: 示例数据
**输出**: 示例数据

## 错误处理

| 错误场景2 | 原因 | 处理方式 |
|:-------|-------:|:-------|
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

- 需要LLM支持
- 动态渲染页面可能需要额外等待时间
- 目标网站反爬策略升级可能导致抓取失败
- 复杂交互流程的稳定性取决于页面结构一致性

