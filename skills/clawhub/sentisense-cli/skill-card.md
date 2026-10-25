## Description:

Helps agents retrieve US stock quotes, sentiment, market activity, analyst data, and screening results through the read-only SentiSense CLI or REST API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other agents use this skill to look up US equity market data and summarize quotes, sentiment, disclosures, institutional flows, options positioning, and screen results without placing trades.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Running the CLI downloads and executes an npm package with the user's environment permissions.

Mitigation: Prefer REST unless shell commands are requested; obtain consent before first CLI use, pin examples, and review the package through normal dependency processes.

Risk: API keys could be exposed in command arguments or sent to an unintended endpoint.

Mitigation: Pass the key through SENTISENSE_API_KEY, not command arguments, and keep requests directed to https://app.sentisense.ai.

Risk: Market data and sentiment may be mistaken for personalized investment advice.

Mitigation: Present results as informational data, not recommendations or instructions to trade.

## Reference(s):

- [SentiSense API reference](https://sentisense.ai/skill.md)
- [SentiSense API key](https://app.sentisense.ai/get-api-key)
- [ClawHub skill listing](https://clawhub.ai/thesentitrader/skills/sentisense-cli)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Plain text or JSON market data; Markdown with bash examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only data access; CLI commands provide stable exit codes.]

## Skill Version(s):

0.3.2 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
