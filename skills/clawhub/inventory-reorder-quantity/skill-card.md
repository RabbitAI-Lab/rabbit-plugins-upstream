## Description:

Combines replenishment quantity selection with recording that quantity in an inventory planning ledger.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Operations, warehouse, purchasing, and fulfillment teams use this skill to choose replenishment quantities from inventory notes and record selected quantities in planning ledgers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Ledger recording can write business inventory-planning data.

Mitigation: Confirm the target ledger behavior in the OpenClaw environment and review quantities before enabling the recording operation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wxt-ai/skills/inventory-reorder-quantity)
- [ClawHub publisher profile](https://clawhub.ai/user/wxt-ai)

## Skill Output:

**Output Type(s):** [text, configuration, guidance]

**Output Format:** [Markdown or plain text describing replenishment quantities and ledger-recording results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs include a selected replenishment quantity and a recorded quantity value when ledger recording is requested.]

## Skill Version(s):

1.0.7 (source: SKILL.md frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
