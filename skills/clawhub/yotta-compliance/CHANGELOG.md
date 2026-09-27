# 更新日志

## v0.1.0 (2026-09-24)

初始发布：

- 定位：元规 —— 本地、确定性、可复算的合规条款审查技能（零依赖，Python 3.8+ 标准库）。
- 规则包：PIPL 11 条 + 数据出境 4 条（`pack_version` 2026.09.1，`coverage_level=baseline_review`）；GDPR / HIPAA / SOC2 / PCI-DSS / ISO27001 / 等保 仅做 `mapping_only` 主题映射，不输出独立合规结论。
- 内核：规范化与偏移映射、结构解析（heading / clause / item / paragraph）、确定性匹配原语、断言求值（absent / present / 数值 / 日期 / 时长）、证据链、Markdown + JSON 报告、规则包校验闸门。
- CLI：`review` / `rules list` / `rules show` / `rules validate`；退出码 0 / 1 / 2 / 3 / 4；支持 `--frameworks`、`--format json`、`--gate`、`--out`、`--stdin`、`--include-safe`。
- 可信契约：每条结论带原文位置、命中规则、框架覆盖级别与来源条款；没有证据不输出风险结论；同一输入得到同一结果。
- 边界：只做基于确定性规则的审查建议，不构成法律意见；核心路径不调用 LLM、不联网；v0.1 不解析 PDF / docx；不判断合同效力或诉讼结果。
- 测试：116 项，Python 3.8.20 / 3.11.9 / 3.13.15 全绿；正式规则包下全护栏样例 0 finding、缺口样例 11 finding（`--gate high` 退出码 1）。
- 文档：SKILL.md + references（rule-authoring / report-format / coverage）+ 中英 README + 四方式安装 + banner。
