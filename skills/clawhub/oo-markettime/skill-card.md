## Description:

MarketTime lets an agent search and read MarketTime catalog, manufacturer, and order data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents with an OOMOL-connected MarketTime account use this skill to read catalog items, manufacturers, and orders without handling raw MarketTime API credentials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill permits broad use of the oo CLI beyond the three documented read-only MarketTime actions.

Mitigation: Review proposed oo CLI commands before execution and limit use to schema inspection and the documented MarketTime read actions unless explicitly approved.

Risk: First-time setup includes remote installer commands for the oo CLI.

Mitigation: Verify the oo CLI installation through a trusted channel before running installer scripts, and avoid automatic installer execution.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-markettime)
- [MarketTime Homepage](https://www.markettime.com/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return JSON-formatted MarketTime connector results when actions are executed.]

## Skill Version(s):

1.0.3 (source: release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
