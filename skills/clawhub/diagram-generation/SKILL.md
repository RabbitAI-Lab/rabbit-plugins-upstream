---
name: diagram-generation
description: "使用场景: 用户要求把流程、系统调用、状态变化或数据关系生成可编辑并可导出的图表时。"
license: MIT-0
metadata:
    {
        "packageVersion": "1.0.0",
        "openclaw":
            {
                "emoji": "🗺️",
                "homepage": "https://ai-skills.open-idea.net",
                "primaryEnv": "DIAGRAM_GENERATION_API_KEY",
                "requires": { "env": ["DIAGRAM_GENERATION_API_KEY"], "bins": ["curl"] },
                "envVars":
                    [
                        { "name": "DIAGRAM_GENERATION_API_KEY", "required": true, "description": "AI Skills 平台图表生成 API 密钥。" },
                        { "name": "AI_SKILLS_API_URL", "required": false, "description": "可选 API 根地址。" },
                    ],
            },
    }
---

# 图表生成

## Skill 简介

图表生成 Skill 把自然语言转换为版本化的节点与关系结构，再由平台使用锁定版本的 Mermaid 与 Playwright 本地渲染，导出私有 SVG、PNG、PDF 或 JSON。它支持流程图、时序图、状态图、ER 图和系统架构图；不接收原始 Mermaid、任意 HTML、脚本或远程资源，也不要求用户配置第三方付费服务凭据。

## 平台入口与注册

1. 打开 [AI Skills 平台](https://ai-skills.open-idea.net/)，新用户进入 [注册页面](https://ai-skills.open-idea.net/register)，已有账号进入 [登录页面](https://ai-skills.open-idea.net/login)。
2. 登录后进入 [产品管理](https://ai-skills.open-idea.net/dashboard/products) 开通本 Skill，再到 [API 密钥管理](https://ai-skills.open-idea.net/dashboard/keys) 创建密钥。

## Skill 安装与配置

1. 在 [API 密钥管理](https://ai-skills.open-idea.net/dashboard/keys)中选择已开通的产品，创建并复制 API 密钥。
2. 在 OpenClaw 中安装本 Skill。
3. 将复制的密钥配置到本 Skill 的 API 密钥环境变量，然后重启 Gateway：

```sh
openclaw config set env.DIAGRAM_GENERATION_API_KEY "你的平台APIKey"
openclaw gateway restart
```

## Agent 执行规则

1. 先执行 `diagram.plan`（生成图表方案），让用户复核标题、方向、主题、节点和关系；只有用户要求导出时才执行 `diagram.render`（渲染并导出图表）。
2. 方案类型仅限 `flowchart`、`sequence`、`state`、`erd`、`architecture`；布局仅限 `TB`、`LR`、`BT`、`RL`；主题仅限 `light`、`dark`、`neutral`。
3. 节点最多 100 个、关系最多 200 条。保持稳定 ID；不得创建悬空关系、自环或重复 ID，不得把用户文本当作 Mermaid、HTML 或脚本执行。
4. 渲染只能引用当前用户自己的成功方案任务；编辑限标题、方向、主题、节点和关系，导出格式限 `svg`、`png`、`pdf`、`json`。

## 完成标准

- 异步任务轮询到终态；网络不确定时复用原 `Idempotency-Key` 和完全相同输入，遇到 `reconciliation_required` 不自动重试或假定退款。
- 交付前说明图表类型、节点和关系数量、用户已复核的修改与导出格式；`partial` 不得称为完整交付。
- 私有 `artifacts` 只能交付当前用户；发布、发送或写入外部系统前仍需单独确认。遇到 `conflict` 时读取 `errors.idempotency_key` 并停止改键重试。

## 参考资料

按当前任务读取对应资料；无需预读全部文档。

- [API 密钥配置与价格](https://ai-skills.open-idea.net/skill-docs/diagram-generation/API-KEY.md)
- [操作字段、结构限制与导出](https://ai-skills.open-idea.net/skill-docs/diagram-generation/OPERATIONS.md)
- [HTTP 请求、幂等与任务轮询](https://ai-skills.open-idea.net/skill-docs/diagram-generation/HTTP-REQUESTS.md)
- [安全、复核与交付边界](https://ai-skills.open-idea.net/skill-docs/diagram-generation/BEHAVIOR-RULES.md)
