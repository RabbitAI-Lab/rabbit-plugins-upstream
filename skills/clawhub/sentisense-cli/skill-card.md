## Description:

Fetch read-only US stock market quotes, sentiment, news, analyst ratings, earnings, company KPIs, ownership activity, options positioning, and screening results through the SentiSense CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and market researchers use this skill to retrieve US equity data for analysis, monitoring, and shell workflows. Its results are informational and are not investment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first CLI run downloads and executes the sentisense npm package with the process's permissions and environment; the external CLI implementation was not independently verified.

Mitigation: Ask before first CLI execution. Keep the documented sentisense@0.73.0 pin and explicit https://app.sentisense.ai base URL, pass credentials through SENTISENSE_API_KEY, or use the documented HTTPS API instead.

## Reference(s):

- [SentiSense API reference](https://sentisense.ai/skill.md)
- [SentiSense API key setup](https://app.sentisense.ai/get-api-key)
- [ClawHub skill listing](https://clawhub.ai/thesentitrader/skills/sentisense-cli)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Guidance]

**Output Format:** [Plain-text or JSON market data, with Markdown usage guidance and shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only market data; stable CLI exit codes]

## Skill Version(s):

0.4.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
