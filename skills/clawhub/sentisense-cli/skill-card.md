## Description:

The official SentiSense CLI: quotes, sentiment, and market data in one npx command.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to fetch US stock quotes, sentiment, news, filings, flows, options data, screening results, and related market signals through the SentiSense CLI or REST API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill runs the sentisense npm CLI through npx and sends the SentiSense API key to the SentiSense service.

Mitigation: Confirm trust in the CLI and service before use, prefer the SENTISENSE_API_KEY environment variable when local key persistence is not desired, and use documented auth storage only when acceptable.

Risk: Market data and generated signals may be mistaken for investment advice or personalized recommendations.

Mitigation: Treat outputs as informational data only and require users to make their own investment decisions.

## Reference(s):

- [SentiSense Website](https://sentisense.ai)
- [SentiSense API Reference](https://sentisense.ai/skill.md)
- [SentiSense API Key](https://app.sentisense.ai/get-api-key)
- [ClawHub Skill Page](https://clawhub.ai/thesentitrader/skills/sentisense-cli)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, Text, JSON]

**Output Format:** [Markdown with inline bash code blocks, plain text CLI output, and optional JSON responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SENTISENSE_API_KEY for authenticated SentiSense API access.]

## Skill Version(s):

0.1.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
