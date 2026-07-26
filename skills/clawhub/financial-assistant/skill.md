---
name: littlebeaver-financial-assistant
description: Use this skill to read and analyze data from the local Xiaoheli Financial Statement Assistant app. It connects only to localhost read-only APIs exposed by 小河狸财报助手, including companies, periods, statements, metrics, trends, and local financial Q&A.
---

# LittleBeaver Financial Assistant

Use this skill when the user asks to query or analyze data already imported into **小河狸财报助手** on the same computer.

The skill reads local data through the app's localhost-only read API. It does not access the SQLite database directly and does not upload data by itself.

## Requirements

- 小河狸财报助手 must be running on the user's computer.
- The app must be version `1.7.4` or later.
- The local API is normally available at `http://127.0.0.1:8765`.
- If the app selected another port, use the client script's auto-discovery.

## Safety Rules

- Only call `127.0.0.1` or `localhost`.
- Do not call LAN IP addresses or public URLs for this skill.
- Use only `/api/local-agent/*` endpoints.
- Treat returned financial data as private user data.
- Do not send detailed financial data to cloud models unless the user explicitly asks for cloud analysis.
- Do not perform imports, deletes, company edits, or sharing operations with this skill.

## Quick Use

Prefer the bundled script:

```bash
python scripts/financial_assistant_client.py health
python scripts/financial_assistant_client.py companies
python scripts/financial_assistant_client.py periods --company "公司名称" --period-type year
python scripts/financial_assistant_client.py metrics --period-id 1
python scripts/financial_assistant_client.py statement --period-id 1 --statement income_statement
python scripts/financial_assistant_client.py trend --company "公司名称" --period-type year --metric revenue
python scripts/financial_assistant_client.py ask "2021年营业收入是多少"
```

If the user asks a natural-language question, use `ask` first. If the answer needs verification or a chart/table, call `companies`, `periods`, `metrics`, `statement`, or `trend` as needed.

## Endpoint Summary

Base URL is discovered from ports `8765-8784` on localhost.

- `GET /api/local-agent/health`
- `GET /api/local-agent/companies`
- `GET /api/local-agent/periods?company=...&period_type=year|quarter|month`
- `GET /api/local-agent/metrics?period_id=...`
- `GET /api/local-agent/statement?period_id=...&statement=balance_sheet|income_statement|cash_flow`
- `GET /api/local-agent/trend?company=...&period_type=year|quarter|month&metric=revenue`
- `POST /api/local-agent/ask`

## Common Metrics

Useful metric keys include:

- `revenue`: 营业收入
- `net_profit`: 净利润
- `gross_margin`: 毛利率
- `net_margin`: 净利率
- `operating_cash_flow`: 经营活动现金流量净额
- `debt_ratio`: 资产负债率
- `cash`: 货币资金
- `receivables`: 应收账款
- `inventory`: 存货

## Answering Style

- Answer in Chinese unless the user requests another language.
- Mention the company and period used.
- If the app is not running, tell the user to open 小河狸财报助手 first.
- If a requested period or metric is missing, say so directly and suggest checking whether the relevant report period was imported.
