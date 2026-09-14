## Description:

Audits a primary Amazon ASIN and authorized competitor product pages for field completeness, expression consistency, and review evidence, while excluding real-time price, sales, inventory, advertising, order, or return-rate judgments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce operators and their agents use this skill to compare a main Amazon product page with authorized competitor pages and identify gaps in product fields, claims, and review-backed evidence. It is intended for page review workflows after ARI authorization and explicit user confirmation for paid runs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The CLI can run paid product-operation workflows beyond the promised fixed page-audit scope.

Mitigation: Require a quote and explicit user confirmation before every paid run, and limit use to the documented page_compare/page workflow.

Risk: The skill stores a local ARI API key and sends Amazon ASIN, site, and product-operation data to ari.funewa.com.

Mitigation: Install only if the publisher and ARI service are trusted, protect the local API key, and avoid submitting sensitive or unauthorized product data.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/funewa/skills/competitor-page-audit)
- [Amazon Competitor Page Audit Workflow](artifact/references/operation-workflow.md)
- [Amazon Competitor Page Audit API Reference](artifact/references/reference.md)
- [ARI service](https://ari.funewa.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown or concise text with CLI-backed audit findings and quoted command steps when needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a local ARI API key; paid collection or analysis should proceed only after a quote and explicit user confirmation.]

## Skill Version(s):

1.4.11 (source: server release evidence, _meta.json, CHANGELOG, script VERSION)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
