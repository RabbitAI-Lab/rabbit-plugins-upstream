## Description:

Compares a primary Amazon ASIN with authorized competitor product-page fields, images, and review evidence to identify listing-expression gaps and verifiable improvements.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers and ecommerce operators use this skill to compare Amazon listing content against authorized competitors, then produce evidence-backed listing gap findings and improvement guidance. It is scoped to collected product-page and review evidence, not real-time price, sales, inventory, advertising, order, or true return-rate judgments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The packaged CLI exposes broader paid product-operation controls than the fixed listing-gap purpose promises.

Mitigation: Review the packaged command surface before deployment and use only the documented fixed listing-gap workflow; prefer a revision that hard-enforces the fixed workflow and focus in the CLI.

Risk: The ARI service receives product identifiers, review-analysis requests, account API keys, and may deduct credits for confirmed paid runs.

Mitigation: Install only when the ARI service is trusted for those inputs, inspect quote results first, and confirm paid runs deliberately.

Risk: Outputs can be misleading if treated as real-time price, sales, inventory, advertising, order, or return-rate evidence.

Mitigation: Use the skill only for collected product-page and review comparisons, and preserve evidence gaps instead of converting missing data into conclusions.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/funewa/skills/competitor-listing-gap)
- [ARI service](https://ari.funewa.com)
- [Operation workflow](references/operation-workflow.md)
- [API reference](references/reference.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and ARI service responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key and quote-before-confirm flow for paid runs.]

## Skill Version(s):

1.4.11 (source: server release metadata, artifact _meta.json, CHANGELOG, and script VERSION)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
