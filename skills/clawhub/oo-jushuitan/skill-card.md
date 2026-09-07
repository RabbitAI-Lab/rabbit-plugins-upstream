## Description:

Jushuitan ERP enables agents to read, create, and update Jushuitan ERP data through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and operators use this skill to operate a connected Jushuitan merchant account through the oo CLI, including order, shipment, inventory, product, supplier, warehouse, finance, and WMS workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup may execute remote OOMOL CLI installer scripts directly.

Mitigation: Review the OOMOL CLI installation path before use; prefer a pinned package, a downloaded installer with a published checksum or signature, or manual inspection before execution.

Risk: Write actions can change Jushuitan ERP business state, including orders, inventory, shipments, suppliers, and warehouse workflows.

Mitigation: Inspect the live action schema and approve state-changing payloads only after checking the exact Jushuitan payload and expected business effect.

Risk: Shipment records do not provide parcel tracking events, pickup status, or current transit milestones.

Mitigation: Use Jushuitan shipment data only for shipment records and use a separate connected carrier tracking source when pickup or transit status is required.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-jushuitan)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Jushuitan ERP Homepage](https://www.jushuitan.com/)
- [Jushuitan OpenWeb Shipment Tracking FAQ](https://openweb.jushuitan.com/qaCenter?groupId=12&postId=39)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May emit oo CLI commands, connector schema inspection steps, JSON request payload guidance, and cautions for write actions.]

## Skill Version(s):

1.0.2 (source: release evidence and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
