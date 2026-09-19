## Description:

Compares a primary Amazon ASIN with authorized competitor product-page fields, images, and review evidence to identify listing-message gaps and verifiable improvement opportunities.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External marketplace operators and agents use this skill to compare an Amazon listing against competitor listings and produce evidence-grounded listing gap findings. It is scoped to product-page comparison and does not support real-time price, sales, inventory, advertising, order, or true return-rate judgments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires an ARI API key and can initiate paid ARI operations.

Mitigation: Install only when ARI account access is appropriate, review quotes before execution, and require explicit confirmation for paid runs.

Risk: The security summary notes that the CLI can run paid operation workflows beyond the advertised listing-gap task.

Mitigation: Before approving a run, verify that the quoted workflow and focus match page_compare/listing_gap and avoid custom workflow or focus values unless a broader ARI operation is intended.

Risk: The skill may produce misleading conclusions if asked for unavailable marketplace signals.

Mitigation: Use outputs only for product-page listing comparison and treat real-time price, sales, inventory, advertising, order, and true return-rate claims as out of scope.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/funewa/skills/competitor-listing-gap)
- [Operation workflow](artifact/references/operation-workflow.md)
- [API reference](artifact/references/reference.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown with concise evidence-based findings and inline shell commands for ARI setup, quoting, execution, and status checks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key and explicit user confirmation before paid ARI operations.]

## Skill Version(s):

1.4.13 (source: server release metadata, artifact _meta.json, script VERSION, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
