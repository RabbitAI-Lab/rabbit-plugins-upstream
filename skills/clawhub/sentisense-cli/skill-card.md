## Description:

The official SentiSense CLI: quotes, sentiment, and market data in one npx command.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to fetch read-only US stock market quotes, sentiment, news, options, insider, congressional, analyst, and institutional flow data through SentiSense CLI commands.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends an API key to the SentiSense service and may store credentials locally if the auth command is used.

Mitigation: Confirm trust in the SentiSense npm package and service before running commands, keep the API key private, and avoid persisted auth on shared machines.

Risk: Market data and sentiment outputs may be mistaken for investment advice.

Mitigation: Treat outputs as informational market data only and require independent review before trading or investment decisions.

## Reference(s):

- [SentiSense Website](https://sentisense.ai)
- [SentiSense API Reference](https://sentisense.ai/skill.md)
- [SentiSense API Key](https://app.sentisense.ai/get-api-key)
- [ClawHub Skill Page](https://clawhub.ai/thesentitrader/skills/sentisense-cli)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, guidance]

**Output Format:** [Plain text or JSON from CLI commands, with Markdown guidance for agents]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SENTISENSE_API_KEY for authenticated SentiSense API access.]

## Skill Version(s):

0.2.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
