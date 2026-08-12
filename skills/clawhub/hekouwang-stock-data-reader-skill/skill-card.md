## Description:

Reads public A-share stock data with akshare, calculates fixed indicators, and helps agents produce compliance-bounded recap reports and shareable finance graphics without investment advice.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huiyonghkw](https://clawhub.ai/user/huiyonghkw)

### License/Terms of Use:

MIT

## Use Case:

External content creators, finance writers, and developers use this skill to collect public A-share data, compute fund-flow, valuation, financial, and LHB-seat indicators, and draft neutral recap articles or image reports with compliance guardrails.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The screenshot helper uses relaxed local-file browser settings.

Mitigation: Run templates/screenshot.js only against a dedicated generated-output directory and review or remove relaxed Chrome flags before deployment.

Risk: The screenshot helper deletes matching HTML files after successful screenshots.

Mitigation: Keep source copies or disable deletion when preserving intermediate HTML is required.

Risk: Generated reports discuss individual stocks and could be mistaken for financial advice.

Mitigation: Retain the neutral recap posture, avoid buy/sell/target-price language, and include the fixed risk disclosure.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/huiyonghkw/skills/hekouwang-stock-data-reader-skill)
- [Skill homepage](https://github.com/huiyonghkw/hekouwang-stock-data-reader-skill)
- [akshare](https://github.com/akfamily/akshare)
- [daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis)
- [Compliance guardrails](references/compliance.md)
- [Report structure](references/report-structure.md)
- [LHB seat symmetry](references/lhb-symmetry.md)
- [Title checklist](references/title-checklist.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown, JSON analysis files, CSV data files, shell commands, and generated PNG report assets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses public akshare data; generated financial content is informational and must retain risk disclosures.]

## Skill Version(s):

1.2.1 (source: SKILL.md frontmatter and CHANGELOG, released 2026-08-12)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
