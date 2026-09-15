## Description:

Checks Amazon listing mobile reading order, information density, and comprehension barriers using product details and review evidence; it requires an ARI API key and does not handle ads, inventory, or automatic publishing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, ecommerce operators, and developers use this skill to review an Amazon product listing's mobile reading flow and prioritize improvements grounded in product-detail and review evidence.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Confirmed ARI operations can spend credits or run outside the intended mobile-listing workflow.

Mitigation: Review the quoted operation before confirming, proceed only when it is the intended listing/mobile workflow, and stop if the workflow or focus differs.

Risk: The ARI API key is stored locally and may be exposed from shared or synced configuration directories.

Mitigation: Keep ~/.ari private, use a non-shared local profile, and rotate the key if exposure is suspected.

Risk: Findings can be incomplete when product details or review samples are missing.

Mitigation: State data gaps clearly, avoid unsupported claims about ads, inventory, orders, profit, or real-time store data, and collect reviews separately only after confirmation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/funewa/skills/mobile-listing)
- [Operation workflow](references/operation-workflow.md)
- [API reference](references/reference.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown report with concise findings, evidence notes, and CLI commands when needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key; paid ARI operations require a quote and explicit user confirmation.]

## Skill Version(s):

1.4.11 (source: server release metadata, _meta.json, CHANGELOG.md, scripts/ari.py)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
