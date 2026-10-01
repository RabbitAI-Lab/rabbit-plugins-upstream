## Description:

Selects a replenishment quantity from an inventory note and records a local inventory planning entry when requested.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Inventory planners and their agents use this skill to calculate a replenishment quantity from stock levels and, when requested, record that quantity in a local planning ledger.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Running the downstream operation creates local receipt folders and an inventory-plan.csv file.

Mitigation: Choose a dedicated, writable output directory and review the local files before relying on them.

Risk: A local inventory planning record may be mistaken for a completed external business action.

Mitigation: Treat the ledger as a local plan, not confirmation of an external order or inventory update.

## Reference(s):

- [Inventory Replenishment Ledger on ClawHub](https://clawhub.ai/wxt-ai/skills/inventory-replenishment-ledger)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, JSON]

**Output Format:** [Text instructions and shell commands; operation results in JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The downstream operation writes a local CSV ledger and receipt files in the specified output directory.]

## Skill Version(s):

3.0.0 (source: SKILL.md frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
