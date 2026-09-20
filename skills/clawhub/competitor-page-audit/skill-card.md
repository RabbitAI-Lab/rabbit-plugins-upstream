## Description:

Audits field completeness, expression consistency, and review evidence between a primary Amazon ASIN and authorized competitor product pages; it does not assess real-time price, sales, inventory, advertising, orders, or actual return rates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers, operators, and analysts use this skill to compare a main ASIN with authorized competitor ASINs, check listing field completeness and review-backed consistency, and receive a concise issue list after quote and explicit confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires an ARI API key and sends product identifiers and related data to ari.funewa.com; paid operations can spend ARI credits after confirmation.

Mitigation: Install only when this data sharing and credit usage are acceptable, review the quote, and run paid operations only after explicit user confirmation.

Risk: Security evidence notes that the CLI can override the documented fixed page-audit workflow and run other server-supported paid operations after confirmation.

Mitigation: Use the documented page_compare/page workflow and avoid workflow or focus overrides unless the publisher narrows enforcement or clearly documents the broader scope.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/funewa/skills/competitor-page-audit)
- [Amazon Competitor Page Audit operational workflow](artifact/references/operation-workflow.md)
- [Amazon Competitor Page Audit API reference](artifact/references/reference.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown guidance with JSON command output from the ARI CLI]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key, product identifiers, and explicit user confirmation before paid operations.]

## Skill Version(s):

1.4.13 (source: server release evidence, artifact _meta.json, CLI VERSION, and CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
