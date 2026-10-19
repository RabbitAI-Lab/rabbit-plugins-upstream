## Description:

Provides agents with Blave market-data guidance and exchange-trading references for crypto, futures, and Taiwan stocks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[blave-wei](https://clawhub.ai/user/blave-wei)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and traders use this skill to query market data, analyze crypto and Taiwan stock markets, and prepare or execute exchange trading actions with user confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Downloaded marketplace strategies may access unrelated files or trading credentials when run locally.

Mitigation: Review strategy code before execution and run it in a restricted sandbox without unrelated files, inherited secrets, or broad network access.

Risk: Live exchange actions can move funds or place unintended trades using API keys.

Mitigation: Use least-privilege, IP-restricted keys; prefer read-only access unless trading is necessary, and require a fresh user CONFIRM for each write action.

## Reference(s):

- [Blave Quant release](https://clawhub.ai/blave-wei/skills/blave-quant-skill)
- [Blave homepage](https://blave.org)
- [Blave API reference](references/blave-api.md)
- [Blave indicator guide](references/blave-indicator-guide.md)
- [Strategy marketplace reference](references/marketplace.md)

## Skill Output:

**Output Type(s):** [Text, Code, Shell commands, Configuration instructions]

**Output Format:** [Markdown with API request and command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Market-data responses and trading guidance depend on configured API credentials and exchange access.]

## Skill Version(s):

1.23.28 (source: release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
