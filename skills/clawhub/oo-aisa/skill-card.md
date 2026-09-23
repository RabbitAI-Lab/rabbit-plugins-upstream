## Description:

AIsa helps agents search and read AIsa-connected account balances, usage metrics, Kalshi market and trade data, and Polymarket event, market, and wallet activity through OOMOL's oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to query AIsa account, usage, and prediction-market data after the oo CLI is installed, signed in, and connected to AIsa.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions can execute remote installer scripts directly.

Mitigation: Review the oo CLI installation path and prefer installing from a trusted, verified source before enabling the skill.

Risk: The skill can read AIsa-connected account, usage, market, trade, and wallet activity data through OOMOL-managed credentials.

Mitigation: Connect only the intended AIsa account and review returned data before sharing it outside the current task.

Risk: Live connector schemas may change over time.

Mitigation: Inspect the action schema before constructing a payload and only run actions that match the current schema.

## Reference(s):

- [AIsa homepage](https://aisa.one)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-aisa)
- [Publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reads account, usage, market, trade, event, and wallet activity data through OOMOL-managed credentials.]

## Skill Version(s):

1.0.0 (source: server evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
