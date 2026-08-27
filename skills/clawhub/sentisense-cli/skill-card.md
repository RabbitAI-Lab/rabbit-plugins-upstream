## Description:

The official SentiSense CLI: quotes, sentiment, and market data in one npx command.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and agents use this skill to fetch informational US stock market data, including quotes, sentiment, news, filings activity, flows, options positioning, and screens through the pinned SentiSense CLI. The skill is an educational data interface and is not investment advice or a personalized recommendation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a SentiSense API key and sends requests to the SentiSense service.

Mitigation: Confirm trust in the SentiSense npm package and service before use, and provide the key through SENTISENSE_API_KEY when temporary access is preferred.

Risk: The documented auth command can persist the API key locally.

Mitigation: Use local auth storage only when persistent key storage is acceptable; otherwise keep the key in the environment and remove stored auth with the documented removal command.

Risk: Market-data outputs could be mistaken for financial recommendations.

Mitigation: Treat outputs as informational data only and require users to make their own investment decisions.

## Reference(s):

- [SentiSense website](https://sentisense.ai)
- [SentiSense API reference](https://sentisense.ai/skill.md)
- [SentiSense API key setup](https://app.sentisense.ai/get-api-key)
- [ClawHub skill page](https://clawhub.ai/thesentitrader/skills/sentisense-cli)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Analysis, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline bash code blocks, plain text CLI output, and optional JSON CLI output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the SENTISENSE_API_KEY environment variable; CLI examples pin sentisense@0.47.1 and may store authentication locally when the documented auth command is used.]

## Skill Version(s):

0.1.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
