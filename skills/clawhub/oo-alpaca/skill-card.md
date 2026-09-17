## Description:

Alpaca (alpaca.markets). Use this skill for ANY Alpaca request - reading, creating, and updating data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate an Alpaca account through OOMOL-connected agent actions, including account inspection, positions, orders, assets, watchlists, portfolio history, and market data retrieval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill instructs an agent to run remote installer commands for the oo CLI if the command is missing.

Mitigation: Review and independently verify the installer source before allowing an agent to execute curl-to-bash or PowerShell-to-iex commands.

Risk: The skill can access sensitive Alpaca account information through OOMOL once the account is connected.

Mitigation: Use only trusted agent sessions, confirm state-changing requests before execution, and limit access to accounts appropriate for the task.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-alpaca)
- [Alpaca Homepage](https://alpaca.markets/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May trigger OOMOL-connected Alpaca actions that return JSON data from the connected account.]

## Skill Version(s):

1.0.2 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
