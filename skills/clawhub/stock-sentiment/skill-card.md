## Description:

Sentiment and smart-money positioning for US stocks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and market-research agents use this skill to retrieve SentiSense sentiment, market mood, smart-money positioning, analyst activity, AI insights, and news context for US equities. It supports educational synthesis and signal comparison, not order entry, portfolio management, or personalized investment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires network access to SentiSense and use of a SENTISENSE_API_KEY.

Mitigation: Limit network access to app.sentisense.ai, keep the API key in environment variables, and avoid exposing the key in prompts, logs, or user-facing output.

Risk: Financial sentiment and positioning summaries could be mistaken for personalized investment advice.

Mitigation: Frame outputs as informational market context only, avoid buy/sell recommendations, and preserve the skill's read-only posture.

## Reference(s):

- [SentiSense](https://sentisense.ai)
- [SentiSense API Skill Documentation](https://sentisense.ai/skill.md)
- [ClawHub Skill Page](https://clawhub.ai/thesentitrader/skills/stock-sentiment)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, guidance]

**Output Format:** [Concise Markdown or text synthesis with optional JSON snippets, curl examples, and Python helper commands.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are informational financial context; API-derived values should be sourced from current read-only SentiSense GET responses and labeled for freshness when batch or delayed.]

## Skill Version(s):

0.4.4 (source: server release evidence, released 2026-09-08)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
