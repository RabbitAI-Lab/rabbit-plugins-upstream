# 跨材料口径一致性审计（Cross-Material Consistency Auditor）

> 针对同一主题或同一事件的多份材料，在发布前对比产品名、数字、事实表述、术语、来源标记、结构承诺和跨平台表达差异。输出带严重度的差异矩阵与统一口径建议，绝不修改原文。

[![ClawHub](https://img.shields.io/badge/ClawHub-cross--material--consistency--auditor--skill-blue)](https://clawhub.ai/haiyangchenbj/cross-material-consistency-auditor-skill)
[![GitHub](https://img.shields.io/badge/GitHub-haiyangchenbj-black)](https://github.com/haiyangchenbj/cross-material-consistency-auditor-skill)

---

## 它做什么

针对同一主题或事件的多份材料，在发布前对比产品名、数字、事实表述、术语、来源标记、结构承诺和跨平台表达差异。只输出差异矩阵与统一口径建议，不自动修改原文。

## 何时使用

- 发布会 / 活动的 PR 通稿、媒体约稿、产品稿、演讲稿在数字或产品名上不一致。
- 同一篇文章的中英版本（微信、LinkedIn、Substack）在表达、数据来源标注或重点上存在差异。
- 系列文章在多篇间的事实、术语或判断出现漂移。
- PPT、白皮书、网页、展厅物料中同一组数字或同一产品用不同名称。

## 何时不使用

- 单篇文章事实核验 → `claim-to-source-auditor` 或 `content-compliance-reviewer`。
- 单篇格式 / 语法 / 客户脱敏检查。
- 选题评估 → `editorial-topic-portfolio`。
- 直接修改或重写任何原文。

## 关键硬规则

- 只审计不改写：绝不修改原文，交付后 hands-off。
- 权威源仲裁冲突；统一口径须引用既有来源。
- P0（数字/法律状态错误、同客户同产品异名、图文关键数据不符）阻断发布。
- 至少两份材料。

## 目录结构

```
cross-material-consistency-auditor/
├── SKILL.md
├── SKILL_zh.md
├── README.md
├── README_zh.md
├── _meta.json
├── references/   # 一致性清单、回放参考
├── scripts/      # 提取与差异脚本
└── templates/    # 审计报告、差异矩阵、统一口径
```

## 许可证

MIT
