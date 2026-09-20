## Description:

Sorftime MCP lets agents use an OOMOL-connected Sorftime account to inspect marketplace products, categories, keywords, trends, and market reports across supported commerce platforms.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and commerce research teams use this skill to run Sorftime MCP actions through the oo CLI for product lookup, category browsing, keyword discovery, trend inspection, supplier sourcing, and market research.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path includes a remote oo CLI installer that may be run without enough user review.

Mitigation: Review the installer path first, prefer package-manager or separately downloaded installation with integrity checks, and do not let an agent install tooling unless the user intended it.

Risk: The skill can prompt connection or authentication to an OOMOL/Sorftime account.

Mitigation: Only authenticate or connect the account after explicit user intent, and avoid proactive login or connection steps unless a command fails for that reason.

Risk: The generic call_tool action may perform destructive Sorftime operations such as deletion or overwriting data.

Mitigation: Require the agent to show the exact target, payload, and expected effect, then obtain explicit approval before running destructive actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-sorftime-mcp)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Sorftime homepage](https://www.sorftime.com/)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include oo CLI connector commands, Sorftime action names, and JSON payload guidance based on the requested task.]

## Skill Version(s):

1.0.4 (source: skill metadata and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
