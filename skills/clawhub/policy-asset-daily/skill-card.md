## Description:

Generates bilingual single-file HTML daily reports that analyze links from policy and macro signals to energy, commodities, FX, and capital markets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[shrifill](https://clawhub.ai/user/shrifill)

### License/Terms of Use:

MIT-0

## Use Case:

Macro strategy analysts, market researchers, and business users use this skill to generate a current bilingual policy-to-market daily report with sourced news, key prices, linkage diagrams, and scenario observations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Opening generated reports may contact TradingView and run its embedded ticker widget script.

Mitigation: Use browser or network controls appropriate for the reader's privacy requirements when opening generated HTML reports.

Risk: The skill produces market and policy analysis from current web research, so stale or unverifiable source data can make conclusions misleading.

Mitigation: Review cited sources, publication times, and any pending or unverified data before relying on the report for decisions.

## Reference(s):

- [Policy-to-Asset Transmission Framework](artifact/references/linkage_framework.md)
- [Preferred News Sources by Domain](artifact/references/news_sources.md)
- [ClawHub skill page](https://clawhub.ai/shrifill/skills/policy-asset-daily)

## Skill Output:

**Output Type(s):** [text, code, guidance]

**Output Format:** [Single-file bilingual HTML report with inline CSS and JavaScript]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses current web research and may embed a TradingView ticker widget for real-time market data.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
