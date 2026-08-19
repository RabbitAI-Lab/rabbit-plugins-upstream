## Description:

招投标AI数据分析平台 helps agents use natural language to search, aggregate, and analyze bidding-market data for market reports, opportunity analysis, trend forecasting, and likely bidder assessment.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhiliaobiaoxun](https://clawhub.ai/user/zhiliaobiaoxun)

### License/Terms of Use:

MIT-0

## Use Case:

External analysts, sales teams, procurement researchers, and agents use this skill to turn open-ended bidding-market questions into structured searches, market summaries, company analysis, price trends, and potential bidder reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create and store service credentials after the user consents to automatic registration.

Mitigation: Prefer setting ZLBX_API_KEY yourself or creating ~/.zlbx/config.json manually to avoid the automatic registration path.

Risk: Automatic registration sends a MAC-derived device hash and stores the returned API key in ~/.zlbx/config.json.

Mitigation: Proceed only if comfortable with that device-hash flow; the artifact limits collection to platform, CPU architecture, and hashed MAC and requires consent before collection.

Risk: Auto-created accounts can generate an auto-login recharge link when free quota is exhausted.

Mitigation: Review the recharge link flow before use, and use a manually configured API key when automatic login is not desired.

Risk: Company shorthand matching can aggregate multiple related entities and may affect analysis conclusions.

Mitigation: Review aggregated company matches when analyzing shorthand or group company names.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhiliaobiaoxun/skills/ai-bidding-data-platform)
- [Account API reference](references/api-account.md)
- [Company analysis API reference](references/api-company.md)
- [Market analysis API reference](references/api-market.md)
- [Bid search API reference](references/api-search.md)
- [Automatic registration workflow](references/auto-register.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown responses with structured analysis, JSON request examples, and shell commands when credential setup is needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May call remote bidding analytics APIs and return summarized market data, company data, price trends, and source URLs.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
