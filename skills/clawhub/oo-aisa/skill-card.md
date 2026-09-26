## Description:

AIsa (aisa.one) lets an agent search and read AIsa-connected account, usage, Kalshi, and Polymarket data through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to let an agent inspect AIsa schemas and run read-focused AIsa connector actions for account balances, usage buckets, prediction markets, executed trades, and wallet activity.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The fallback setup path runs a remotely fetched oo CLI installer script.

Mitigation: Review the installer source and prefer a verified installation method before allowing an agent to run setup commands.

Risk: Read-focused AIsa actions can expose account, usage, market, trade, and wallet activity from the connected OOMOL account.

Mitigation: Run connector actions only in the intended account context and avoid sharing outputs beyond the user's authorized workflow.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-aisa)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [AIsa Homepage](https://aisa.one)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Normal actions return JSON data from the oo CLI connector; setup guidance may include authentication and connection steps.]

## Skill Version(s):

1.0.1 (source: release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
