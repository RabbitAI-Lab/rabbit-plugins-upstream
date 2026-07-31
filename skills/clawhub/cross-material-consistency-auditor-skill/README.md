# Cross-Material Consistency Auditor

> Compare two or more materials on the same topic or event for cross-material consistency before publication — mismatched numbers, product names, fact wording, terminology, source attributions, structural promises, and cross-platform expression drift. Outputs a diff matrix with severity ratings and recommended unified wording; never modifies originals.

[![ClawHub](https://img.shields.io/badge/ClawHub-cross--material--consistency--auditor--skill-blue)](https://clawhub.ai/haiyangchenbj/cross-material-consistency-auditor-skill)
[![GitHub](https://img.shields.io/badge/GitHub-haiyangchenbj-black)](https://github.com/haiyangchenbj/cross-material-consistency-auditor-skill)

---

## What it does

For multiple materials on the same topic or event, compare product names, numbers, fact wording, terminology, source attributions, structural promises, and cross-platform expression drift before publication. Output only a diff matrix and unified-wording recommendations — never auto-modify the originals.

## When to use

- A launch/event's PR release, journalist pitch, product copy, and speech script disagree on numbers or product names.
- A Chinese and English version of the same article differ in expression, data-source attribution, or emphasis.
- A series of articles drifts on facts, terminology, or judgments across installments.
- The same numbers or product use different names across PPT, white paper, web page, and booth materials.

## When not to use

- Fact-checking a single article → `claim-to-source-auditor` or `content-compliance-reviewer`.
- Format / grammar / customer-redaction on a single article.
- Topic evaluation → `editorial-topic-portfolio`.
- Directly modifying or rewriting any original.

## Hard rules (key)

- Audit-only: never modify originals; hands-off after delivery.
- Authoritative source arbitrates conflicts; unified wording must cite an existing source.
- P0 (wrong number / legal status, same customer/product under different names, figure-vs-body mismatch) blocks publication.
- At least two materials required.

## File structure

```
cross-material-consistency-auditor/
├── SKILL.md
├── SKILL_zh.md
├── README.md
├── README_zh.md
├── _meta.json
├── references/
│   ├── consistency-checklist.md
│   └── replay-references.md
├── scripts/
│   └── extract_and_diff.py
└── templates/
    ├── audit-report.template.md
    ├── diff-matrix.template.md
    └── unified-wording.template.json
```

## License

MIT
