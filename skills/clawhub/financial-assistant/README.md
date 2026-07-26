![License](https://img.shields.io/github/license/LittleBeaverStudio/KingdeeDataAnalyzer?label=license)
# 小河狸财报助手 Skill

这是给本机智能体使用的“小河狸财报助手”数据读取 Skill。它通过小河狸财报助手提供的本机只读接口，查询已导入的公司、期间、财务报表、指标、趋势和本地问答结果。

仓库地址：

https://github.com/LittleBeaverStudio/FinancialAssistant

## 适用场景

- 让本机智能体读取小河狸财报助手中的历史财报数据。
- 根据已导入数据回答“某年营业收入”“资产负债率趋势”“经营现金流变化”等问题。
- 在智能体工作流中补充本地财务数据上下文。

## 使用前提

- 已安装并打开小河狸财报助手 `v1.7.4` 或更高版本。
- 智能体与小河狸财报助手运行在同一台电脑。
- 小河狸财报助手本地服务可访问，通常为 `http://127.0.0.1:8765`。

## 安全说明

- 本 Skill 只访问 `127.0.0.1` 或 `localhost`。
- 本 Skill 只调用 `/api/local-agent/*` 只读接口。
- 本 Skill 不直接读取数据库文件，不执行导入、删除、修改、分享等操作。
- 返回的财务数据属于用户本地私有数据，未经用户明确要求，不应发送给云端模型做深度分析。

## 命令示例

```bash
python scripts/financial_assistant_client.py health
python scripts/financial_assistant_client.py companies
python scripts/financial_assistant_client.py periods --company "公司名称" --period-type year
python scripts/financial_assistant_client.py metrics --period-id 1
python scripts/financial_assistant_client.py statement --period-id 1 --statement income_statement
python scripts/financial_assistant_client.py trend --company "公司名称" --period-type year --metric revenue
python scripts/financial_assistant_client.py ask "2021年营业收入是多少"
```

## 更新说明

如果本仓库发布新版本，是否自动提醒取决于用户所使用的智能体或 Skill 管理工具。若智能体未自动更新，可以手动拉取本仓库最新内容。

## License

MIT License
