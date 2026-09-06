## Description:

Compares recorded Amazon product-page price snapshots for a primary ASIN and authorized competitors, showing relative price position, timestamp, and evidence gaps without claiming real-time pricing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers and operators use this skill to compare a product's captured price position against authorized competitors and identify gaps in the evidence behind that comparison. It is intended for snapshot-based operational review, not automated repricing or sales, inventory, profit, order, or ad-budget decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The released artifact exposes broader ARI workflows than the narrow competitor price-positioning summary suggests, including review export, monitoring, and paid AI or data operations.

Mitigation: Review the full capability scope before installation, keep use focused on the fixed page_compare/price workflow, and require explicit approval before export, monitoring, or paid operations.

Risk: The skill requires an ARI API key and may access account-specific Amazon product and review data.

Mitigation: Use the documented setup or local configuration flow, never place the API key in reports or command examples, and revoke or recreate the key if it may have been exposed.

Risk: Server-side autoconfirm can allow some paid workflows to run without a fresh prompt when the configured policy permits it.

Mitigation: Check and adjust the autoconfirm setting for the deployment context, report credits used after execution, and disable or lower thresholds where explicit per-run approval is required.

Risk: Price comparisons are based on recorded snapshots and can be stale or incomplete.

Mitigation: Show the snapshot timing and evidence gaps, avoid representing results as real-time prices, and do not use the output for automated repricing or sales, profit, inventory, order, or ad-budget decisions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/funewa/skills/competitor-price)
- [Operation Workflow](artifact/references/operation-workflow.md)
- [ARI CLI and API Reference](artifact/references/reference.md)
- [User Guide](artifact/使用说明.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown and structured CLI output with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include ASIN, site, sample size, snapshot timing, report URL, credits used, current balance, and explicit evidence-gap notes when returned by ARI.]

## Skill Version(s):

1.4.5 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
