## Description:

Provides agents with market-data and open-interest history references, plus exchange trading workflows for crypto, Taiwan stocks, and futures.

This skill is ready for commercial/non-commercial use.

## Publisher:

[blave-wei](https://clawhub.ai/user/blave-wei)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and traders use this skill to retrieve crypto and Taiwan market data, analyze open-interest history, and guide exchange trading with explicit confirmation for account-changing actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Downloaded marketplace strategies may execute unreviewed code with access to local files or trading credentials.

Mitigation: Review strategy code independently before running it, and sandbox execution away from credentials and local files.

Risk: Exchange access can create substantial trading losses or expose account privileges.

Mitigation: Use dedicated, least-privilege API keys without withdrawal permission and confirm each account-changing action before execution.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/blave-wei/skills/blave-quant-skill)
- [Blave website](https://blave.org)
- [Blave documentation](https://blave.org/docs/en)

## Skill Output:

**Output Type(s):** [Market analysis, Trading guidance, Code, Shell commands]

**Output Format:** [Markdown with data summaries and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Account-changing trading actions require explicit user confirmation.]

## Skill Version(s):

1.23.11 (source: ClawHub release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
