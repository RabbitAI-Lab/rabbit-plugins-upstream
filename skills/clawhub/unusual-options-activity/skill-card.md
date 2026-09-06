## Description:

Unusual Options Activity helps agents retrieve read-only, end-of-day SentiSense options analytics for US stocks and ETFs, including IV rank, options sentiment, put/call percentiles, skew, open-interest walls, max pain, and unusually active contracts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and external users use this skill to ask an agent for concise read-only summaries of unusual options activity, volatility positioning, put/call context, skew, open-interest walls, max pain, and related ticker history for covered US stocks and ETFs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The optional npx CLI path expands a data lookup workflow into local third-party code execution.

Mitigation: Prefer the curl or Python REST examples; if the CLI is used, run it in a constrained environment with no unrelated credentials exposed.

Risk: The required SENTISENSE_API_KEY could be exposed through logs, shell history, or user-facing output.

Mitigation: Keep the key in the environment, never put it in query strings, logs, or generated answers, and avoid exposing unrelated credentials when running commands.

Risk: End-of-day options analytics can be mistaken for real-time order flow, forecasts, or personalized investment advice.

Mitigation: Frame results as informational, educational, read-only context; state that readings are end-of-day and avoid buy, sell, hedge, or prediction language.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thesentitrader/skills/unusual-options-activity)
- [SentiSense homepage](https://sentisense.ai)
- [SentiSense API](https://app.sentisense.ai)
- [SentiSense API key](https://app.sentisense.ai/get-api-key)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown answers with JSON API summaries and optional curl, Python, or npx examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SENTISENSE_API_KEY; uses read-only GET requests; returns end-of-day financial analytics, not trading instructions.]

## Skill Version(s):

1.3.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
