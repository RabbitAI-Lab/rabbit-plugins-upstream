## Description:

Checks readiness and relaunch risk for an existing Amazon ASIN using product detail and review evidence.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

Amazon sellers and marketplace operators use this skill to assess whether an existing ASIN is ready for a listing revision or relaunch. It is intended for products with an ASIN and review history, not for predicting new-product performance, ad budgets, inventory, or supply-chain actions.

### Deployment Geography for Use:

Global; marketplace coverage is limited to the Amazon sites supported by ARI.

## Known Risks and Mitigations:

Risk: The security review reports that the CLI can permit broader paid product-operation workflows than the fixed launch-readiness scope described in the documentation.

Mitigation: Use the packaged launch-readiness flow only, keep workflow and focus values aligned to audit/launch, and do not manually supply alternate operations values unless broader ARI behavior is intended.

Risk: The skill requires an ARI API key and can submit paid analysis or review-collection requests after confirmation.

Mitigation: Install only when the user is comfortable authorizing the ARI service, review quotes before confirming paid runs, and avoid implicit reruns after interruptions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/funewa/skills/launch-readiness)
- [README](README.md)
- [Operation workflow](references/operation-workflow.md)
- [API reference](references/reference.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with concise findings and inline shell commands when setup or execution details are needed.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key and explicit user confirmation before paid analysis or review-collection requests.]

## Skill Version(s):

1.4.13 (source: server evidence, _meta.json, CHANGELOG, and scripts/ari.py)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
