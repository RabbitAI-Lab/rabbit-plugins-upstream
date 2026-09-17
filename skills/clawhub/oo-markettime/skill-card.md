## Description:

MarketTime lets agents search and read MarketTime catalog, manufacturer, and order data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers with an OOMOL-connected MarketTime account use this skill to inspect the live connector schema and run read-only MarketTime actions for catalog items, manufacturers, and orders.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands that run directly in a shell.

Mitigation: Review the setup path before installation; prefer an official package manager or a pinned release with checksum or signature verification, and do not let an agent run the remote installer automatically.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-markettime)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [MarketTime Homepage](https://www.markettime.com/)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Text, JSON]

**Output Format:** [Markdown guidance with shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill instructs the agent to inspect the connector schema before running an action and to return JSON output from the oo CLI.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
