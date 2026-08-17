## Description:

This skill helps agents fetch public A-share stock data with akshare, compute fixed recap indicators, and produce compliance-guarded neutral recap charts and article drafts without investment advice.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huiyonghkw](https://clawhub.ai/user/huiyonghkw)

### License/Terms of Use:

MIT

## Use Case:

External content creators and finance-reporting teams use this skill to turn a requested A-share ticker into a neutral, public-data recap with charts, article structure, and platform-specific compliance guardrails. The workflow supports stock-code data fetching, indicator analysis, report draft generation, and screenshot-ready visual output.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill queries third-party public market-data services for requested stock codes.

Mitigation: Use it only when those lookups are acceptable for the workflow and avoid entering sensitive or confidential watchlists as requests.

Risk: Generated financial recaps could be misleading or non-compliant if published without review.

Mitigation: Review the generated text against the included compliance guardrails and keep the content neutral: no investment advice, price predictions, ratings, or buy/sell points.

Risk: Generated HTML is removed after screenshots, which can reduce auditability.

Mitigation: Keep copies of intermediate HTML or generated output files when an audit trail is required.

Risk: The workflow installs Python dependencies and runs local scripts.

Mitigation: Install dependencies in an isolated environment and review the scripts before deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/huiyonghkw/skills/hekouwang-stock-data-reader-skill)
- [Publisher profile](https://clawhub.ai/user/huiyonghkw)
- [Homepage](https://github.com/huiyonghkw/hekouwang-stock-data-reader-skill)
- [akshare](https://github.com/akfamily/akshare)
- [daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis)
- [Compliance guardrails](references/compliance.md)
- [Report structure](references/report-structure.md)
- [LHB seat symmetry guide](references/lhb-symmetry.md)
- [Title and cover checklist](references/title-checklist.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, generated report text, structured analysis files, and screenshot-ready chart assets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses public market data requested by ticker and includes financial compliance guardrails; users should review generated financial text before publishing.]

## Skill Version(s):

1.2.2 (source: frontmatter, changelog released 2026-08-12, ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
