## Description:

Sorftime MCP helps agents search, browse, and inspect ecommerce market data through the OOMOL-connected Sorftime MCP connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to query Sorftime MCP for product lookup, category browsing, keyword discovery, market reports, and trend inspection across supported ecommerce marketplaces.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A deletion-capable tool path may not be clearly labeled before use.

Mitigation: Inspect the selected tool schema and require explicit confirmation before any favorite change, deletion, overwrite, or other account-state change.

Risk: Remote installer commands fetch and execute scripts from the network.

Mitigation: Review the installer source first and prefer a pinned or signed installation method where available.

Risk: Some Sorftime actions may consume account credits.

Mitigation: Confirm credit-consuming actions before execution and stop for billing errors such as HTTP 402 or OOMOL_INSUFFICIENT_CREDIT.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-sorftime-mcp)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Sorftime MCP Homepage](https://www.sorftime.com/)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown guidance with shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Actions should inspect the live connector schema before execution; some actions may consume Sorftime credits or change account state.]

## Skill Version(s):

1.0.1 (source: release evidence and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
