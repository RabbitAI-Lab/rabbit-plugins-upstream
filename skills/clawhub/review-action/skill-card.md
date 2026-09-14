## Description:

Turns Amazon review issues into evidence-based product, packaging, instruction, and supplier action tasks through the ARI service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, product teams, and operators use this skill to convert Amazon ASIN review evidence into product improvement tasks. It checks product data and pricing first, then runs the paid ARI action workflow only after explicit user confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires an ARI API key and stores local configuration under ~/.ari.

Mitigation: Keep ~/.ari private, avoid shared or synced config directories, and rotate the API key if local configuration is exposed.

Risk: Amazon ASIN, task, and review-related data is sent to https://ari.funewa.com.

Mitigation: Use the skill only when sending that product and review data to the ARI service is acceptable for the user's workflow.

Risk: Paid ARI credits may be spent when collection or analysis actions are confirmed.

Mitigation: Review the quoted cost and requestId before running confirmed actions; use status checks instead of rerunning interrupted confirmed tasks.

## Reference(s):

- [Amazon Review to Action API Reference](references/reference.md)
- [Amazon Review to Action Operations Workflow](references/operation-workflow.md)
- [ARI Service](https://ari.funewa.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown summaries with supporting CLI commands and JSON responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are scoped to product/action tasks using the ops_product template.]

## Skill Version(s):

1.4.11 (source: server release evidence, artifact _meta.json, CHANGELOG, and scripts/ari.py)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
