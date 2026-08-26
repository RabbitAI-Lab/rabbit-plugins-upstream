---
name: sql-data-analyst
description: "使用场景: 当用户要在本机分析 CSV、JSON、XLSX 或 Parquet，提出数据问题、运行只读 SQL，或制作本地 XLSX/HTML 报告时使用。"
metadata:
    {
        "packageVersion": "1.2.0",
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

## Skill 安装与配置

1. 在 AI Skills 平台“产品管理”中开通 SQL 数据分析。
2. 进入「API Key」，选择该产品，创建并复制 API Key。
3. 在 OpenClaw 中安装 `sql-data-analyst` Skill，并按安装提示在 Skill 目录运行一次 `./scripts/install.sh`。安装器会自动准备 Runner 并完成 doctor 检查。
4. 将复制的 Key 配置到本 Skill 的 API Key 环境变量，然后重启 Gateway：

```sh
openclaw config set env.SQL_DATA_ANALYST_API_KEY "你的平台APIKey"
openclaw gateway restart
```

## Skill 使用

配置完成后，用户只需给出本地文件路径和分析目标，例如：

- “分析 `~/Downloads/sales.xlsx`，按月份汇总销售额，并说明变化趋势。”
- “检查 `orders.csv` 中是否有重复订单，并列出重复数量最多的客户。”

## 执行规则

1. 先确认本地 Runner 可用，再读取数据集结构。
2. 宿主模型根据结构和用户问题生成一条只读 `SELECT` 或 `WITH` SQL。
3. 所有文件读取、查询和报告生成必须交给 Runner 在用户本机执行，不得改用 DuckDB CLI、Python REPL 或其他执行器绕过 Runner。
4. 只解释 Runner 返回的有限结果，并明确说明截断或样本限制。

平台仅接收计费授权所需的 `operation`、`runner_version`、`installation_id`、`input_fingerprint` 四个元数据字段。Runner 自动处理 `Authorization: Bearer`、`Idempotency-Key`、摘要校验和签名票据；这些都不是用户需要配置的内容。

## 详细参考

- [API Key 配置](https://github.com/YouTeacher/ai-skills-platform/blob/main/openclaw/sql-data-analyst/references/API-KEY.md)：仅在安装或更换 Key 时阅读。
- [本地执行流程与完整命令](https://github.com/YouTeacher/ai-skills-platform/blob/main/openclaw/sql-data-analyst/references/USAGE.md)：仅在开发或排障时阅读。
- [隐私和安全边界](https://github.com/YouTeacher/ai-skills-platform/blob/main/openclaw/sql-data-analyst/references/SECURITY.md)：处理敏感数据或审计时阅读。
- [计费说明](https://github.com/YouTeacher/ai-skills-platform/blob/main/openclaw/sql-data-analyst/references/BILLING.md)：用户询问价格或免费操作时阅读。
- [平台授权接口](https://github.com/YouTeacher/ai-skills-platform/blob/main/openclaw/sql-data-analyst/references/openapi.json)：维护授权客户端时阅读。
