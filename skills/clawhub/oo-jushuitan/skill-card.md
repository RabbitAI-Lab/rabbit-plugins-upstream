## Description:

Jushuitan ERP helps an agent read, create, update, and delete Jushuitan ERP data through the OOMOL oo connector instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers who operate Jushuitan ERP through an OOMOL-connected account use this skill to inspect live action schemas and run ERP actions for orders, shipments, inventory, warehouses, purchases, after-sales, finance, WMS, products, suppliers, and cross-border workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup instructions can run remote installer scripts on the user's machine.

Mitigation: Review the installer source and prefer an official signed or package-manager install path before authorizing installation.

Risk: Write and destructive Jushuitan ERP actions can change, overwrite, or remove business records.

Mitigation: Confirm the exact payload, target records, and expected business effect with the user before running state-changing actions.

Risk: Shipment records do not include carrier tracking events or pickup status.

Mitigation: Use a separate connected tracking source for pickup, transit, stale-tracking, or delivery status decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-jushuitan)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [Jushuitan ERP homepage](https://www.jushuitan.com/)
- [Jushuitan OpenWeb shipment tracking FAQ](https://openweb.jushuitan.com/qaCenter?groupId=12&postId=39)
- [OOMOL oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce oo CLI commands, schema-first execution guidance, JSON payload guidance, and interpretation of JSON ERP results.]

## Skill Version(s):

1.0.5 (source: server release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
