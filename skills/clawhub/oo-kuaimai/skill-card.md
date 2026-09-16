## Description:

Kuaimai ERP lets an agent search and read Kuaimai ERP data through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers with OOMOL-connected Kuaimai ERP accounts use this skill to inspect products, SKUs, inventory, orders, stockouts, shops, warehouses, and session validity through the oo CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup guidance includes one-line remote installers for the oo CLI.

Mitigation: Verify the installer through OOMOL's install guide or another trusted channel before execution.

Risk: The refresh_session action extends Kuaimai Open Platform session validity.

Mitigation: Require explicit user approval before running refresh_session.

## Reference(s):

- [Kuaimai ERP on ClawHub](https://clawhub.ai/oomol/skills/oo-kuaimai)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Kuaimai ERP homepage](https://www.kuaimai.com/)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands may return JSON data from Kuaimai ERP through the oo CLI.]

## Skill Version(s):

1.0.2 (source: server evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
