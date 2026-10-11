## Description:

Helps agents retrieve and explain Chinese financial-market and investment-research data for stocks, funds, indices, company financials, reports, and macroeconomics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kenneth-bro](https://clawhub.ai/user/kenneth-bro)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, analysts, and developers use this skill to look up and compare Chinese market prices, fund performance, financial statements, announcements, research, and macroeconomic data. It supports data gathering and interpretation, not trade execution or direct buy/sell advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing the external API package or enabling automatic updates may introduce untrusted code.

Mitigation: Review the package and its update channel before installing or enabling updates.

Risk: Putting an API key directly in a command may expose it in shell history or process details.

Mitigation: Use safer credential handling instead of the documented inline --api-key example.

Risk: Skipping verification weakens installation trust checks.

Mitigation: Avoid --skip-verify unless its security tradeoff has been reviewed.

Risk: Sending private text to entity-recognition services can disclose sensitive information.

Mitigation: Do not submit sensitive private text for entity recognition.

Risk: Some reference examples appear inconsistent or contaminated, so financial outputs may mislead.

Mitigation: Independently verify important financial data and conclusions before relying on them.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/kenneth-bro/skills/investoday-finance-data)
- [Financial data API reference index](artifact/docs/references-index.md)
- [Financial data API reference index (English)](artifact/docs/references-index.en.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Structured financial data]

**Output Format:** [Markdown summaries, tables, and CLI examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Financial data availability depends on network access, credentials, service permissions, and query scope.]

## Skill Version(s):

1.8.94 (source: skill frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
