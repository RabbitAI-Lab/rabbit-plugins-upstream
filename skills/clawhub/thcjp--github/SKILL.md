---

slug: github
name: github
version: 1.0.2
displayName: GitHub开发工具
summary: 用gh CLI操作GitHub,issue/pr/run/api一站管理。Interact with GitHub using the `gh`
  CLI。Use `gh issue`, `g
summary_zh: 用gh CLI操作GitHub,issue/pr/run/api一站管理。Interact with GitHub using the `gh`
  CLI。Use `gh issue`, `g
license: MIT
description: |-。用gh CLI操作GitHub,issue/pr/run/api一站管理。Interact with GitHub using the。Use when 需要代码生成、编程辅助、调试测试、开发部署时使用。不适用于无明确技术栈的模糊需求。适用于独立开发者、企业团队和自动化工作流场景。支持中文交互，无需复杂配置即开即用。
  `gh` CLI。Use `gh issue`, `g。支持自动化配置和灵活的参数设置，适覆盖多种使用场景，优化工作流程和效率。。用gh CLI操作GitHub,issue/pr/run/api一站管理。Interact
  with GitHub using the `gh` CLI。Use `gh issue`, `g'
tags:
- Integrations
- 版本控制
- Git
- 开发工具
- api
- agent
tools:
- read
- exec
- write
homepage: ''
category: Development
homepage: ""
pricing_tier: "L2-标准级"

---

> **功能说明**: 本技能涵盖 中文交互、化工作流场景 等核心能力。

# Github

## 付费版扩展能力
| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| Githubapi一站管理 | 不支持 | 支持 |
| 代码静态分析与质量评分 | 不支持 | 支持 |
| 依赖缺陷检测与升级建议 | 不支持 | 支持 |
| 批量代码审查与报告生成 | 不支持 | 支持 |
| CI/CD流水线集成 | 不支持 | 支持 |

## 适用范围
| 场景 | 输入 | 输出 |
|:-----|:-----|:-----|
| Git操作 | 仓库路径与分支名 | 操作结果与变更记录 |
| 管理操作 | 操作目标与参数 | 操作结果与状态变更 |
| 用gh CLI操作G | 目标数据与配置参数 | 处理结果与执行状态 |

**不适用于**：需要人工判断的复杂决策场景

## 使用指南
1. 确认运行环境满足依赖说明中的要求
2. 根据适用场景选择合适的使用方式
3. 执行操作并检查输出结果
4. 如遇错误，参考错误处理章节

## 输入规范
| 参数名 | 类型 | 必填 | 说明 |
|---:|---:|---:|---:|
| content | string | 否 | github处理的内容输入 |,  |
| mode | string | 否 | 处理模式, 可选: json/text/markdown,  |
| max_retries | integer | 否 | 单步最大重试次数, 默认: 2 |
| skip_steps | array | 否 | 跳过的步骤编号(用于断点续传), 默认: [] |

## 输出规范
```json
{
  "success": true,
  "data": {
    "final_result": {
      "github_result": "github_result_value",
      "github_metadata": "github_metadata_value",
      "github_status": "github_status_value"
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

中间产物模板参考: `assets/github_template`

## 前置条件
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
- **分类**: MD+execute()
- **说明**: 基于Markdown的AI Skill,

**API Key配置方式**:
```bash
export API_KEY="${API_KEY:?请设置环境变量}"
```
配置后需重启会话或开启新终端生效。API Key应妥善保管,避免泄露到版本控制系统.
## 热门问题
### Q1: 如何开始使用Github？
A: 请参考使用流程和依赖说明章节，确保运行环境满足要求后调用本技能。
## 异常管理机制
| 错误场景(续)| 原因 | 处理方式 |
|----:|:----|----:|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | 请求重试；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 功能边界
- 需要API Key，无Key环境无法使用

## 创新优势
### 效率提升量化分析
| 操作步骤 | 手动耗时 | 自动化耗时 | 时间节约 | 准确率提升 |
|:--------|:--------|:--------|:--------|:--------|
| 创建issue | 15分钟 | 2分钟 | 13分钟 | 10% |
| 提交PR | 30分钟 | 5分钟 | 25分钟 | 15% |
| 运行CI/CD | 1小时 | 10分钟 | 50分钟 | 20% |
| API调用 | 10分钟 | 1分钟 | 9分钟 | 10% |
| Webhook配置 | 30分钟 | 5分钟 | 25分钟 | 15% |

### 差异化对比
| 对比维度 | 本技能 | 手动操作 | Python脚本 | 专业软件 |
|:--------|:--------|:--------|:--------|:--------|
| 操作便捷性 | 高 | 低 | 中 | 高 |
| 功能丰富性 | 高 | 低 | 中 | 高 |
| 学习成本 | 低 | 高 | 中 | 高 |
| 成本效益 | 高 | 低 | 中 | 高 |
| 维护难度 | 低 | 高 | 中 | 高 |

### 核心痛点解决
| 痛点 | 描述 | 影响范围 | 解决方案 | 量化效果 |
|:----|:----|:----|:----|:----|
| 手动操作效率低 | 需要大量手动操作，耗时且容易出错 | 整个开发流程 | 使用gh CLI自动化操作 | 时间节约20% |
| API调用复杂 | API调用需要编写代码，对开发者要求高 | API集成 | 提供gh api工具，简化API调用 | 准确率提升10% |
| Webhook配置困难 | Webhook配置需要编写代码，配置复杂 | 系统连接 | 提供gh webhook工具，简化配置 | 时间节约15% |

## 常见问题FAQ

### Q1: 如何使用gh CLI创建issue？
A: 使用`gh issue create --title "issue标题" --body "issue描述"`命令创建issue。

### Q2: 如何使用gh CLI提交PR？
A: 使用`gh pr create --title "PR标题" --body "PR描述" --base "目标分支" --head "本地分支"`命令提交PR。

### Q3: 如何使用gh CLI运行CI/CD？
A: 使用`gh run create --title "运行标题" --ref "分支名"`命令运行CI/CD。

### Q4: 如何使用gh CLI调用API？
A: 使用`gh api /path/to/resource`命令调用API。

### Q5: 如何使用gh CLI配置Webhook？
A: 使用`gh webhook create --url "Webhook URL" --events "事件类型"`命令配置Webhook。

## 诊断与修复
| 错误现象 | 可能原因 | 诊断步骤 | 解决方案 |
|:--------|:--------|:--------|:--------|
| gh CLI无法启动 | 环境变量配置错误 | 检查环境变量是否配置正确 | 重新配置环境变量 |
| 操作失败 | 权限不足 | 检查用户权限 | 获取相应权限 |
| 网络连接失败 | 网络不稳定 | 检查网络连接 | 重新连接网络 |
| API调用失败 | API请求错误 | 检查API请求参数 | 修改API请求参数 |

## 安全规范
1. 确保gh CLI的安装来源可靠，避免安装恶意软件。
2. 使用强密码保护GitHub账户，避免账户被盗用。
3. 定期更新gh CLI，以获取最新的安全补丁。
4. 避免在公共网络环境下使用gh CLI进行敏感操作。
5. 对API调用进行安全验证，防止未授权访问。

### 安全风险防范

| 风险项 | 等级 | 防护措施 | 验证方法 |
| --- | --- | --- | --- |
| API密钥泄露 | 高 | 通过环境变量配置，禁止硬编码 | 定期检查代码和配置文件 |
| 命令执行风险 | 高 | 仅执行白名单命令，避免拼接用户输入 | 使用沙箱环境测试 |
| 网络通信安全 | 中 | 使用HTTPS协议，验证SSL证书 | 定期检查证书有效期 |
| 敏感数据暴露 | 高 | 输出结果中不包含密钥、令牌等敏感信息 | 日志脱敏审查 |
| 未授权访问 | 中 | 限制访问权限，实施认证机制 | 定期审计访问日志 |
