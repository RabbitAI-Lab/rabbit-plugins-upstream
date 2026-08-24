## Description:

Provides A-share and ETF historical-data collection, quantitative signal statistics, research-summary cross-checks, and optional DOCX/chart report generation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sunbinpy](https://clawhub.ai/user/sunbinpy)

### License/Terms of Use:

MIT-0

## Use Case:

External users and analysts use this skill to request A-share or ETF data lookups, historical signal matching, fund-flow summaries, research-report cross-checks, and optional DOCX report generation for a specified security. Outputs are informational and non-advisory.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Persistent API key handling

Mitigation: Install only if you trust the publisher, protect ~/.ghdata/ghdataapikey as a credential, and remove or rotate the key when it is no longer needed.

Risk: Remote analysis and payment-token data flow

Mitigation: Review the listed domains and network behavior before use, and avoid submitting confidential or regulated information through this skill.

Risk: Financial-analysis misuse

Mitigation: Keep outputs framed as historical statistics and informational summaries; do not treat them as investment advice, forecasts, or buy/sell/hold recommendations.

Risk: Local report and chart generation

Mitigation: Confirm the configured report directory before running report generation and review generated DOCX or chart files before sharing them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/sunbinpy/skills/gh-data)
- [股海罗盘 product homepage](https://www.oraskl.com/ghdata-admin)
- [股海罗盘 platform](https://www.oraskl.com/ghdata-admin/platform)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Files, Guidance]

**Output Format:** [Markdown/text responses with Python code snippets; optional DOCX reports and PNG charts.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May call external stock-data and analysis APIs; may create files under configured report directories and read/write ~/.ghdata/ghdataapikey.]

## Skill Version(s):

2.2.51 (source: server release evidence and artifact metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
