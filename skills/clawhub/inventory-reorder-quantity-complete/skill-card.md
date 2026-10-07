## Description:

Calculates an inventory replenishment quantity, records a local planning entry, and optionally delivers the record when configured.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Inventory planners use this skill to calculate reorder quantities from stock notes and create local planning records. Configured deployments can also submit the records to a delivery destination.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Configured delivery can automatically submit the inventory record and its local file path to an external endpoint using ambient credentials.

Mitigation: Use local-only mode unless external delivery is intended; scope delivery endpoints, API keys, and SMTP settings specifically to this skill and review the destination before running.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/wxt-ai/skills/inventory-reorder-quantity-complete)
- [Usage and delivery instructions](artifact/README.md)

## Skill Output:

**Output Type(s):** [JSON data, CSV file, Delivery receipt]

**Output Format:** [JSON result and local CSV planning record]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Delivery receipt reports sent, delivered, failed, or unconfigured; external delivery requires configuration.]

## Skill Version(s):

1.2.0 (source: SKILL.md frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
