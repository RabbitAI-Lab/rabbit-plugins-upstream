## Description:

Extracts verifiable Amazon product differentiation directions and open validation questions from main-product and authorized competitor product fields, images, and review evidence.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External marketplace operators and developers use this skill to turn Amazon product, image, and review evidence into focused differentiation directions for product discussion. It is not intended for market-size, sales, profit, inventory, advertising, order, or real-time store decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on a paid ARI service and may send ASIN, product, review, and request data to ari.funewa.com.

Mitigation: Install only if the publisher and ARI service are trusted, keep the ARI API key protected locally, and share only product data appropriate for that service.

Risk: Security evidence says the package exposes overrideable workflow and focus parameters for broader server-side operations.

Mitigation: Use it only for the documented page_compare/differentiation workflow unless the publisher documents and scopes broader operations.

Risk: Paid collection or analysis actions can consume account credits.

Mitigation: Keep paid actions behind the documented quote-and-explicit-confirm flow and reuse the quoted requestId when running the operation.

## Reference(s):

- [Amazon Product Differentiation Operation Workflow](references/operation-workflow.md)
- [Amazon Product Differentiation API Reference](references/reference.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with concise findings, evidence notes, validation gaps, and inline bash commands when setup or execution is needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key and quote-before-confirm flow for paid actions.]

## Skill Version(s):

1.4.13 (source: server evidence, CHANGELOG, _meta.json, scripts/ari.py)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
