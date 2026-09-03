## Description:

Compare product or service prices across multiple sellers, marketplaces, or official pricing pages and produce normalized price findings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dataify-server](https://clawhub.ai/user/dataify-server)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to collect comparable current offers, normalize pricing evidence, and produce evidence-backed pricing reports for monitoring, offer comparison, channel pricing, and pricing-change decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The shipped shared module includes review, lead, and brand intelligence workflows beyond the advertised price-comparison purpose.

Mitigation: Review the installed files before routine use and remove, disable, or clearly disclose non-price workflows when only a narrow price-monitoring skill is intended.

Risk: Automated price findings can be misleading if variants, currencies, freshness, seller terms, stock, or shipping are not comparable.

Mitigation: Require human review for pricing decisions and preserve source, collection time, currency, variant, seller, stock, shipping, and billing-period evidence in reports.

## Reference(s):


## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Markdown and JSON reports with concise guidance and optional shell commands.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports retain raw responses, hashes, state, collection time, source URLs, seller details, currency, stock, shipping, and comparable-offer metrics when available.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
