## Description:

Waffo Pancake lets an agent operate Waffo account workflows through the OOMOL oo CLI connector, including products, stores, checkout, subscriptions, payments, orders, and refunds.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Merchants, support operators, and developers use this skill to read and manage Waffo Pancake account data through an OOMOL-connected account. It supports store, product, checkout, subscription, order, payment, refund, and analytics workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can operate on real merchant, customer, payment, subscription, and refund data in the connected Waffo account.

Mitigation: Review the skill before installation when connected to production accounts and limit use to specific Waffo account tasks.

Risk: Write-capable actions can create or change products, stores, checkout sessions, subscriptions, product status, and refund workflows.

Mitigation: Require explicit user confirmation for every non-read operation and verify the exact payload and expected effect before execution.

Risk: Refund resubmission behavior may change refund state even though the action is not marked with a write tag in the artifact.

Mitigation: Treat refund resubmission as a non-read operation and require confirmation before running it.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-waffo)
- [Waffo Pancake homepage](https://www.waffo.ai)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs guide the agent to inspect live connector schemas, run oo CLI connector actions, and summarize JSON responses for the user.]

## Skill Version(s):

1.0.0 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
