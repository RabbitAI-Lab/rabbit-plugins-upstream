## Description:

天机我要查 (免费版)（TianJi-Open） is a free, open-source assistant for aggregating public company information into source-linked due diligence and business risk reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chesaram](https://clawhub.ai/user/chesaram)

### License/Terms of Use:

MIT-0

## Use Case:

External users, employees, and business analysts use this skill to research companies before investment, partnership, procurement, competitor analysis, or other business review workflows. It helps collect public business registration, ownership, risk, financing, news, bidding, qualification, and intellectual property signals into a structured report for follow-up verification.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill performs web searches about companies and may surface incomplete or outdated public records.

Mitigation: Treat results as leads, confirm ambiguous company names, record collection dates, and verify important conclusions with official sources.

Risk: Business risk findings could be mistaken for professional legal, financial, or regulatory due diligence.

Mitigation: Use the report as preliminary research only and require qualified professional review for high-impact decisions.

Risk: The optional local baidu-search helper can run if the user has configured it.

Mitigation: Run optional helpers only in a trusted local environment and fall back to built-in web search when the helper is unavailable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chesaram/skills/tianji-open-1-0-0)
- [Search tips](references/search-tips.md)
- [Business information sources](references/sources.md)
- [Industry and bidding templates](references/industry-bidding-templates.md)
- [Demo report](references/demo-report.md)

## Skill Output:

**Output Type(s):** [Markdown, Guidance, Shell commands]

**Output Format:** [Markdown reports with sourced findings, verification guidance, and optional shell command suggestions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports should mark collection time, event dates, source confidence, missing evidence, and official verification needs.]

## Skill Version(s):

1.0.0 (source: server release evidence and manifest.yaml)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
