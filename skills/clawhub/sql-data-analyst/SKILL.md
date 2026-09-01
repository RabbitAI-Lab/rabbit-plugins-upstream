---
name: sql-data-analyst
description: "使用场景: 当用户要在本机分析 CSV、JSON、XLSX 或 Parquet，提出数据问题、运行只读 SQL，或制作本地 XLSX/HTML 报告时使用。"
metadata:
    {
        "packageVersion": "1.4.0",
        "openclaw":
            {
                "emoji": "▦",
                "homepage": "https://ai-skills.open-idea.net",
                "primaryEnv": "SQL_DATA_ANALYST_API_KEY",
                "requires": { "env": ["SQL_DATA_ANALYST_API_KEY"] },
            },
    }
---

# SQL Data Analyst

## Skill 简介

SQL 数据分析 Skill 用于在本机分析 CSV、JSON、XLSX 和 Parquet 文件，通过自然语言提问或只读 SQL 获取结果，并在本地生成 XLSX 或 HTML 报告；原始数据不上传平台。

在 OpenClaw（龙虾）中用自然语言分析本地数据。宿主模型理解用户问题并解释结果，随 Skill 安装的 Runner 在用户本机读取文件、执行只读 SQL 和生成报告；文件内容、SQL 与结果不会发送给平台。

## 平台入口与注册

1. 打开 [AI Skills 平台](https://ai-skills.open-idea.net/)，新用户可直接进入 [注册页面](https://ai-skills.open-idea.net/register)，已有账号进入 [登录页面](https://ai-skills.open-idea.net/login)。
2. 登录后进入 [产品管理](https://ai-skills.open-idea.net/dashboard/products) 开通本 Skill，再到 [API Key 管理](https://ai-skills.open-idea.net/dashboard/keys) 创建密钥。

## Skill 安装与配置

1. 在 OpenClaw 中安装 `sql-data-analyst` Skill，并按安装提示完成安装。
2. 将复制的 Key 配置到本 Skill 的 API Key 环境变量，然后重启 Gateway：

```sh
openclaw config set env.SQL_DATA_ANALYST_API_KEY "你的平台APIKey"
openclaw gateway restart
```

## Skill 使用

配置完成后，用户只需给出本地文件路径和分析目标，例如：

- “分析 `~/Downloads/sales.xlsx`，按月份汇总销售额，并说明变化趋势。”
- “检查 `orders.csv` 中是否有重复订单，并列出重复数量最多的客户。”

数据读取、查询和报告生成都在用户本机完成，原始数据不会上传平台。用户只需提供文件路径和分析目标；安装、授权和安全细节由 Skill 自动处理。

## 参考资料

- [API Key 配置](https://ai-skills.open-idea.net/skill-docs/sql-data-analyst/API-KEY.md)
- [本地执行流程与完整命令](https://ai-skills.open-idea.net/skill-docs/sql-data-analyst/USAGE.md)
- [隐私和安全边界](https://ai-skills.open-idea.net/skill-docs/sql-data-analyst/SECURITY.md)
- [计费说明](https://ai-skills.open-idea.net/skill-docs/sql-data-analyst/BILLING.md)
- [平台授权接口](https://ai-skills.open-idea.net/skill-docs/sql-data-analyst/openapi.json)
