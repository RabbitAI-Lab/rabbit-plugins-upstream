# 审稿核验器（Claim-to-Source Auditor）

> 审稿 / 事实核验 / 来源追溯 / 跨平台一致性检查。提取可核验主张，溯源至 L0 一手或 L1 可靠二手来源，逐条标记为 通过 / 部分支持 / 缺证 / 错误 / 判断，输出带 P0–P2 严重度的结构化审计报告；支持跨平台版本比对与回归 gold-set 重跑。

[![ClawHub](https://img.shields.io/badge/ClawHub-claim--to--source--auditor--skill-blue)](https://clawhub.ai/haiyangchenbj/claim-to-source-auditor-skill)
[![GitHub](https://img.shields.io/badge/GitHub-haiyangchenbj-black)](https://github.com/haiyangchenbj/claim-to-source-auditor-skill)

---

## 它做什么

从长文、报告或系列中提取高风险主张，溯源至 L0 一手或 L1 可靠二手来源，逐条判为 通过 / 部分支持 / 缺证 / 错误 / 判断，并输出带 P0–P2 严重度的结构化审计报告。同时支持跨平台版本比对与回归 gold-set 重跑。

## 何时使用

- 发布前对长文、报告或分析做事实核验。
- 核验已发布主张是否仍成立。
- 检查同一文章多平台版本的事实一致性。
- 审计学术引用、监管结论、财务数字、内部数据或直接引语。
- 为后续修订建立回归 gold-set。

## 何时不使用

- 风格 / 结构 / 论证强度批评 → 本 Skill 只审计事实与来源。
- 跨材料口径一致性 → `cross-material-consistency-auditor`。
- 营销稿完整发布前合规 → 本地已安装的专门合规审查 Skill。

## 关键硬规则

- 仅 L0 或 L1 可使主张通过；L2 仅补充。
- 无可核验来源的主张默认判 缺证，而非 通过。
- 事故三层分离：仅「公认事实」层可作为已核验事实，平台表述与作者解读不得混写。
- 绝不编造证据，如实报告缺口。

## 目录结构

```
claim-to-source-auditor/
├── SKILL.md
├── SKILL_zh.md
├── README.md
├── README_zh.md
└── _meta.json
```

## 许可证

MIT
