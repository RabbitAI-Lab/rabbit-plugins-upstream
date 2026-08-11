## Description:

Queries Google Trends keyword search-interest data through LinkFox and helps agents summarize normalized keyword trends by region and date range.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, market researchers, and commerce operators use this skill to retrieve normalized Google Trends keyword interest data and analyze trend direction, seasonality, peaks, and regional search-interest patterns.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses LinkFox as a paid external service and each trend query consumes credits.

Mitigation: Tell users when a call will spend credits, avoid repeated exploratory calls for the same task, and get explicit approval before initiating payment or order flows.

Risk: Keyword queries, account details, and feedback content may be sent to LinkFox services.

Mitigation: Avoid sending sensitive user content through trend queries or feedback, and review endpoint environment variables before use.

Risk: The scripts can persist API responses, setup metadata, and payment QR output under a local linkfox directory.

Mitigation: Run the skill only in an expected workspace, protect API keys in environment variables, and remove local response or setup files when retention is not needed.

Risk: Onboarding helpers can perform phone signup, API key generation, plan listing, and payment order creation.

Mitigation: Require explicit user approval before phone signup, API key generation, plan selection, or payment order steps.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-google-trend-get-trend-by-keys)
- [Publisher profile](https://clawhub.ai/user/linkfox-ai)
- [Google Trends keyword API reference](references/api.md)
- [Authentication and billing onboarding](references/onboarding.md)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, configuration, guidance]

**Output Format:** [Markdown trend summaries, JSON API responses, and shell commands or configuration snippets for setup and billing flows]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Trend results use a normalized 0-100 scale, full responses are saved locally, repeated identical calls may use a 24-hour cache, and each trend query consumes 6 credits.]

## Skill Version(s):

1.0.5 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
