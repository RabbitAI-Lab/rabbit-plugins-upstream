## Description:

Records an inventory planning quantity and produces a replenishment planning entry.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Inventory planners use this skill to record a requested quantity and receive a planning entry with case-pack, carton-count, and replenishment-action details.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Configured runs can transmit inventory record data and a local artifact path to an external delivery target.

Mitigation: Review before installing; set delivery endpoint, API key, or SMTP variables only when intended. For local-only use, leave delivery configuration absent and inspect the delivery receipt.

## Reference(s):

- [Inventory Planning Ledger on ClawHub](https://clawhub.ai/wxt-ai/skills/inventory-reorder-quantity-workbench)

## Skill Output:

**Output Type(s):** [JSON, Files]

**Output Format:** [JSON planning entry with a local inventory record and optional delivery receipt]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes quantity, case pack, carton count, planning action, and entry ID.]

## Skill Version(s):

1.1.1 (source: SKILL.md frontmatter and ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
