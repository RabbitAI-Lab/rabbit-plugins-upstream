---
slug: "azure"
name: "azure"
version: 1.0.1
displayName: "Azure"
summary: "用经实战检验的模式部署监控管理Azure服务,稳定上云"
license: "Proprietary"
description: |-
  Deploy, monitor, and manage Azure services with battle-tested patterns。核心能力:

  - 运维工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 系统运维、监控告警、资源管理

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助
tags:
  - Operations
tools:
  - read
  - exec
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "19.9 CNY/per_use"
pricing_tier: "L2-标准级"
pricing_model: "per_use"

---
# Azure

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| Azure战检验的模式部署监控 | 不支持 | 支持 |
| 多源数据聚合与去重 | 不支持 | 支持 |
| 语义搜索与智能摘要 | 不支持 | 支持 |
| 定时监控与变化推送 | 不支持 | 支持 |
| 研究结论结构化导出 | 不支持 | 支持 |

## 核心能力

- Deploy, monitor, and manage Azure services with battle-tested patterns
#
## 适用场景

| 场景 | 输入 | 输出 |
|:-----|:-----|:-----|
| 场景1: 用经实战检验的模式部署监控管理Azure服务 | 用户请求数据 | 结构化处理结果 |

**不适用于**：需要人工判断的复杂决策场景

## 使用流程

1. **登录与鉴权**: 验证用户身份与权限,加载平台配置信息
2. **选择操作模块**: 根据用户意图定位目标功能模块与管理对象
3. **执行管理操作**: 调用平台API执行创建/修改/查询/删除操作并返回结果
4. **异常处理**: 如遇错误,参考错误处理章节中对应场景的处理方式

## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---:|---:|---:|---:|
| content | string | 否 | azure处理的内容输入 |,  |
| mode | string | 否 | 处理模式, 可选: json/text/markdown,  |
| max_retries | integer | 否 | 单步最大重试次数, 默认: 2 |
| skip_steps | array | 否 | 跳过的步骤编号(用于断点续传), 默认: [] |

## 输出格式

```json
{
  "success": true,
  "data": {
    "final_result": {
      "azure_result": "azure_result_value",
      "azure_metadata": "azure_metadata_value",
      "azure_status": "azure_status_value"
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

中间产物模板参考: `assets/azure_template`

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

### Q1: 如何开始使用Azure？
A: 

## 错误处理

| 错误场景2 | 原因 | 处理方式 |
|---:|:---|---:|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

- 依赖云服务，需要网络连接
- 需要有效的云服务凭证和配置好的CLI环境
- 产生的云资源可能产生费用，使用前请确认计费方式
- 不同区域的服务可用性和功能支持可能存在差异
