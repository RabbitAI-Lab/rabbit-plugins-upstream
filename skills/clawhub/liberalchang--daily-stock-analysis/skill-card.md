## Description:

Analyzes stock codes through a configured daily_stock_analysis service and presents trends, action guidance, and price targets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[liberalchang](https://clawhub.ai/user/liberalchang)

### License/Terms of Use:

MIT-0

## Use Case:

Users and research assistants request stock-code-based analysis for supported markets through a configured DSA service, then review its summary, trend outlook, and suggested price levels.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A configured remote DSA service may receive stock codes, prompts, chat messages, session identifiers, and required cookies.

Mitigation: Confirm that DSA_BASE_URL points to a trusted service and avoid sending private financial details unless you control or trust the endpoint.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/liberalchang/skills/daily-stock-analysis)
- [daily_stock_analysis project (linked in skill documentation; not verified release provenance)](https://github.com/ZhuLinsen/daily_stock_analysis)
- [OpenClaw skill integration guide (linked in skill documentation)](https://github.com/ZhuLinsen/daily_stock_analysis/blob/main/docs/openclaw-skill-integration.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown analysis in conversation]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include an action recommendation, trend forecast, analysis summary, and buy, stop-loss, or take-profit levels when returned by the service.]

## Skill Version(s):

1.0.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
