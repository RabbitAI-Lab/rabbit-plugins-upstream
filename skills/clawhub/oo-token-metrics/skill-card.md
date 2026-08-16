## Description:

Token Metrics lets an agent query Token Metrics cryptocurrency market data and trading signals through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to fetch Token Metrics prices, token identifiers, OHLCV records, market-cap rankings, and trading signals from their OOMOL-connected Token Metrics account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can use the user's OOMOL-connected Token Metrics account to read market data.

Mitigation: Confirm the user wants this account used for Token Metrics reads before installing or invoking the skill.

Risk: First-time setup may require installing the external oo CLI or starting an OOMOL login flow.

Mitigation: Run installer or login commands only when needed after a command failure and after the user confirms they trust OOMOL.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-token-metrics)
- [Publisher profile](https://clawhub.ai/user/oomol)
- [Token Metrics homepage](https://www.tokenmetrics.com/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before execution and returns read-only market-data responses through the oo CLI.]

## Skill Version(s):

1.0.0 (source: server release metadata and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
