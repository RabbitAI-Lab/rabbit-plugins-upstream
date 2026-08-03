# Claim-to-Source Auditor

> Audit, fact-check, verify, or cross-check an article, report, draft, or series. Extracts verifiable claims, traces them to L0 primary or L1 reliable secondary sources, marks each as pass / partial-support / missing-evidence / wrong / judgment, and produces a structured audit report with P0–P2 severity. Supports cross-platform comparison and regression gold-set re-runs.

[![ClawHub](https://img.shields.io/badge/ClawHub-claim--to--source--auditor--skill-blue)](https://clawhub.ai/haiyangchenbj/claim-to-source-auditor-skill)
[![GitHub](https://img.shields.io/badge/GitHub-haiyangchenbj-black)](https://github.com/haiyangchenbj/claim-to-source-auditor-skill)

---

## What it does

Extracts high-risk claims from a long-form article, report, or series; traces each to L0 primary or L1 reliable secondary sources; classifies each as 通过(pass) / 部分支持(partial-support) / 缺证(missing-evidence) / 错误(wrong) / 判断(judgment); and outputs a structured audit report with P0–P2 severity. Also supports cross-platform version comparison and a regression gold-set for future re-runs.

## When to use

- Fact-check a long-form article, report, or analysis before publication.
- Verify published claims still hold against current sources.
- Check fact consistency across multi-platform versions of the same article.
- Audit academic citations, regulatory claims, financial numbers, internal data, or direct quotes.
- Build a regression gold set for fact-regression checks on future revisions.

## When not to use

- Style / structure / argument-strength critique → this skill audits facts and sources only.
- Cross-material wording/number consistency → `cross-material-consistency-auditor`.
- Full pre-publish compliance of a marketing draft → a dedicated compliance-review skill if one is installed.

## Hard rules (key)

- Only L0 or L1 sources make a claim pass; L2 is supplementary only.
- Missing-verifiable-source defaults to 缺证 (missing-evidence), never 通过 (pass).
- Separate incident layers: only "agreed facts" can pass as verified; platform statements and author interpretation must not be compressed.
- Never invent evidence; report gaps.

## File structure

```
claim-to-source-auditor/
├── SKILL.md
├── SKILL_zh.md
├── README.md
├── README_zh.md
└── _meta.json
```

## License

MIT
