## Description:

ShipStation (shipstation.com). Use this skill for ShipStation requests, including reading purchase orders and inventory data and preparing state-changing connector operations through the OOMOL `oo` CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate ShipStation through an OOMOL-connected account, inspect live connector schemas, retrieve purchase orders, and list inventory levels, inventory properties, warehouses, and purchase orders.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance includes pipe-to-shell installer commands for the `oo` CLI.

Mitigation: Review the installer source and prefer a verified installation path before running installer commands.

Risk: At least one action is labeled inconsistently for read/write behavior.

Mitigation: Inspect the live action schema and confirm the exact payload and expected effect with the user before running any action tagged `[write]` or `[destructive]`.

Risk: The skill can operate a ShipStation account through OOMOL connector credentials.

Mitigation: Install and use it only when the publisher is trusted with ShipStation connector operations.

## Reference(s):

- [ClawHub ShipStation Skill](https://clawhub.ai/oomol/skills/oo-ship-station)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [ShipStation](https://www.shipstation.com/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce `oo connector schema` and `oo connector run` commands; connector responses are JSON when `--json` is used.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
