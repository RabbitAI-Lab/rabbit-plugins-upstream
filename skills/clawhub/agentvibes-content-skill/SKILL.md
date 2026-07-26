---
name: "agentvibes-content-skill"
slug: "agentvibes-content-skill"
displayName: "AgentVibes内容技能"
version: 4.6.7
summary: "AgentVibes内容创作与管理技能,支持多模态内容生成与发布"
description: |-
  API封装工具。适用于需要调用外部API的场景，API请求参数→API响应数据.
  Use when 用户说"Agentvibes Content Skill 核心处理"、Agentvibes Content Skill 核心处理时使用.
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
# Agentvibes Content Skill 智能分析

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| AgentVibes内容技能bes内容创作与管理 | 不支持 | 支持 |
| AgentVibes内容技能支持多模态内容生成 | 不支持 | 支持 |
| 多租户管理与权限分配 | 不支持 | 支持 |
| 操作审计与合规日志 | 不支持 | 支持 |
| 自定义仪表盘与报表 | 不支持 | 支持 |

## 核心能力

- Agentvibes Content Skill 实时监控
- Agentvibes Content Skill 错误重试
- Agentvibes Content Skill 多格式支持
#
## 适用场景

- 用户说"Agentvibes Content Skill 扩展能力9" → 执行API调用
- 用户说"Agentvibes Content Skill 扩展能力10" → 执行API调用
- 用户说"Agentvibes Content Skill 扩展能力11" → 执行API调用
- 不适用: 需要人工判断的复杂场景

## 使用流程

### Step 1: 登录与鉴权
验证用户身份与权限,加载平台配置信息
### Step 2: 选择操作模块
根据用户意图定位目标功能模块与管理对象
### Step 3: 执行管理操作
调用平台API执行创建/修改/查询/删除操作并返回结果
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|:-----|:-----|:-----|:-----|

## 输出格式

```json
{
  "success": true,
  "data": {
    result: "skill 相关配置参数",
    result: "skill 相关配置参数"
  },
  "error": null
}
```

## 异常处理

| 错误场景 | 原因 | 处理方式 |
|---:|---:|---:|
| 管理操作权限不足 | 当前用户角色无操作权限 | 提示联系管理员授权,或切换到有权限的管理账号 |
| 平台API限流 | 短时间请求量超过阈值 | 启用请求队列与指数退避,降低调用频率后重试 |
| 配置变更未生效 | 缓存未刷新或配置同步延迟 | 清除平台缓存,确认配置广播状态,必要时手动重启服务 |

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

## 常见问题

### Q: 如何使用此Skill?
A: 请参考使用流程章节

## 错误处理

| 错误场景2 | 原因 | 处理方式 |
|:-------|-------:|:-------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

- 需要LLM支持
- 需要LLM支持,无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力与网络状况
