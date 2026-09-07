## Description:

Sorftime MCP helps agents search, inspect, and analyze marketplace product, keyword, category, and trend data through an OOMOL-connected Sorftime MCP account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and commerce analysts use this skill to query Sorftime MCP for product, keyword, category, and trend research across supported marketplaces.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generic tool execution can change or delete account data or consume credits.

Mitigation: Inspect the live schema and confirm the exact payload and effect before write-capable, destructive, favorites-changing, or billing-affecting actions.

Risk: Installer guidance includes streaming remote install scripts into a shell.

Mitigation: Prefer a verified or package-managed oo CLI installation, or review the installer before executing it.

Risk: Remote connector calls operate through a user-connected Sorftime MCP account.

Mitigation: Use the skill only when the user trusts OOMOL and Sorftime and is comfortable with connector calls from that account.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-sorftime-mcp)
- [Sorftime MCP Homepage](https://www.sorftime.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with oo CLI commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an installed oo CLI, an authenticated OOMOL account, and a connected Sorftime MCP account.]

## Skill Version(s):

1.0.0 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
