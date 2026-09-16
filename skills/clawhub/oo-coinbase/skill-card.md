## Description:

Reads Coinbase Advanced Trade brokerage account details through the OOMOL oo CLI and connected account credentials.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to list Coinbase brokerage accounts or retrieve one account by UUID through an OOMOL-connected Coinbase account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance includes remote script execution commands for installing the OOMOL CLI.

Mitigation: Review and independently verify the installer source before running curl|bash or irm|iex commands.

Risk: The routing language is broader than the listed read actions.

Mitigation: Use the skill only for list_accounts and get_account unless a separate workflow clearly scopes additional Coinbase actions.

Risk: The skill accesses Coinbase account data through connected credentials.

Mitigation: Confirm the OOMOL account connection and requested account UUID before retrieving account data, and avoid trading, transfers, or account changes.

## Reference(s):

- [ClawHub Coinbase Skill](https://clawhub.ai/oomol/skills/oo-coinbase)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Coinbase](https://www.coinbase.com)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are JSON when the generated oo CLI command is run with --json.]

## Skill Version(s):

1.0.3 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
