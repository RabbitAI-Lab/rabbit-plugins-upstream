## Description:

The official SentiSense CLI: quotes, sentiment, and market data in one npx command.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and market-data users use this skill to fetch US equity quotes, sentiment, news, institutional flows, options data, and related SentiSense read-only API outputs through the pinned CLI or documented REST API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can ask an agent to run npx, which downloads and executes the pinned sentisense npm package locally with access to SENTISENSE_API_KEY.

Mitigation: Ask before first CLI execution, review the npm package through the user's normal process, prefer the documented REST API when possible, and use a narrowly scoped API key.

Risk: Market data and sentiment outputs may be mistaken for investment advice.

Mitigation: Present outputs as informational data only and avoid personalized recommendations or solicitations to buy or sell securities.

## Reference(s):

- [SentiSense Website](https://sentisense.ai)
- [SentiSense API Reference](https://sentisense.ai/skill.md)
- [ClawHub Skill Page](https://clawhub.ai/thesentitrader/skills/sentisense-cli)
- [SentiSense API Key](https://app.sentisense.ai/get-api-key)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown guidance with inline shell commands and optional JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SENTISENSE_API_KEY for authenticated SentiSense API access.]

## Skill Version(s):

0.2.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
