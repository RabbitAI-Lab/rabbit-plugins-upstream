---
name: sql-data-analyst
description: "使用场景: 用户要求在本机分析 CSV、JSON、XLSX、Parquet，运行只读 SQL 或生成本地报告时。"
license: MIT-0
metadata:
    {
        "packageVersion": "1.7.1",
        "openclaw": {
            "emoji": "▦",
            "homepage": "https://ai-skills.open-idea.net",
            "primaryEnv": "SQL_DATA_ANALYST_API_KEY",
            "envVars": [
                {
                    "name": "AI_SKILLS_API_KEY",
                    "required": false,
                    "description": "通用平台 Key；与产品专用变量任选其一。"
                },
                {
                    "name": "SQL_DATA_ANALYST_API_KEY",
                    "required": false,
                    "description": "兼容产品专用 Key；设置时优先使用。"
                }
            ]
        }
    }
---

# SQL 数据分析

## Skill 简介

SQL 数据分析 Skill 用于在本机分析 CSV、JSON、XLSX 和 Parquet 文件，通过自然语言提问或只读 SQL 获取结果，并在本地生成 XLSX 或 HTML 报告；原始数据不上传平台。

在 OpenClaw（龙虾）中用自然语言分析本地数据。宿主模型理解用户问题并解释结果，随 Skill 安装的 Runner 在用户本机读取文件、执行只读 SQL 和生成报告；文件内容、SQL 与结果不会发送给平台。

## 平台入口与注册

1. 打开 [AI Skills 平台](https://ai-skills.open-idea.net/)，新用户可直接进入 [注册页面](https://ai-skills.open-idea.net/register)，已有账号进入 [登录页面](https://ai-skills.open-idea.net/login)。
2. 登录后进入 [产品管理](https://ai-skills.open-idea.net/dashboard/products) 开通本 Skill，再到 [API 密钥管理](https://ai-skills.open-idea.net/dashboard/keys) 创建密钥。

## Skill 安装与配置

当前控制台直接创建通用 Key，无需选择产品；每个账号最多保留一把未撤销的通用 Key，已有时直接复制复用，更换时先撤销旧 Key。下列产品选择说明适用于旧版控制台。

1. 在 [API 密钥管理](https://ai-skills.open-idea.net/dashboard/keys)中选择已开通的产品，创建并复制 API 密钥。
2. 在 OpenClaw 中安装本 Skill，并按安装提示完成安装。
3. 将复制的密钥配置到本 Skill 的 API 密钥环境变量，然后重启 Gateway：

```sh
openclaw config set env.AI_SKILLS_API_KEY "你的平台APIKey"
openclaw gateway restart
```

推荐创建账号通用 Key，以上全局变量只需配置一次即可供各 Skill 使用；仍需在产品管理中开通目标产品。原有产品专用 Key 仅能调用对应产品。

兼容旧配置：如需隔离本产品，可改用 `openclaw config set env.SQL_DATA_ANALYST_API_KEY "你的平台APIKey"`，然后重启 Gateway。调用时优先读取 `SQL_DATA_ANALYST_API_KEY`，为空时读取 `AI_SKILLS_API_KEY`；两者均缺失时停止调用并引导创建密钥。不要输出、记录或要求用户在对话中粘贴完整密钥。


## Skill 使用

配置完成后，用户只需给出本地文件路径和分析目标，例如：

- “分析 `~/Downloads/sales.xlsx`，按月份汇总销售额，并说明变化趋势。”
- “检查 `orders.csv` 中是否有重复订单，并列出重复数量最多的客户。”

数据读取、查询和报告生成都在用户本机完成，原始数据不会上传平台。用户只需提供文件路径和分析目标；安装、授权和安全细节由 Skill 自动处理。

## 完成标准

- 在用户已授权范围内完成本地读取、只读查询与所需报告；以 Runner 的实际状态和产物为准，不套用平台异步任务轮询。
- 可恢复的授权故障按 USAGE.md 复用本次调用的持久化幂等键有界重试；输入、安全或验签错误停止并说明原因，不绕过 Runner。
- 交付可核验的结果或报告路径，保留截断与失败限制；多文件任务逐项说明完成、失败和未处理部分。

## 参考资料

按当前任务读取对应资料；无需预读全部文档。

- 首次配置或排查鉴权时：[API 密钥配置](https://ai-skills.open-idea.net/skill-docs/sql-data-analyst/API-KEY.md)
- 执行本地分析前，查 Runner 命令与输入契约：[本地执行流程与完整命令](https://ai-skills.open-idea.net/skill-docs/sql-data-analyst/USAGE.md)
- 执行前，确认本地隐私、只读与授权边界：[隐私和安全边界](https://ai-skills.open-idea.net/skill-docs/sql-data-analyst/SECURITY.md)
- 付费执行前，确认计费规则：[计费说明](https://ai-skills.open-idea.net/skill-docs/sql-data-analyst/BILLING.md)
- 实现或排查平台授权客户端时：[平台授权接口](https://ai-skills.open-idea.net/skill-docs/sql-data-analyst/openapi.json)
