## Description:

Compare GTM data APIs using a downloadable catalog of provider plans, pricing, scores, rate limits, returned fields, and documentation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[waynehamadi](https://clawhub.ai/user/waynehamadi)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and GTM teams can compare or price data APIs by reviewing provider plans, costs, scores, rate limits, returned fields, and documentation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Downloading the catalog replaces an existing datacircle.json in the working directory.

Mitigation: Download into a dedicated directory or back up any existing file first.

Risk: Catalog pricing may be outdated or differ from a provider's current offer.

Mitigation: Confirm prices and plan terms with the provider before purchasing.

## Reference(s):

- [Datacircle JSON catalog](https://datacircle.dev/datacircle.json)
- [Datacircle CSV catalog](https://datacircle.dev/datacircle.csv)
- [Datacircle field definitions](https://datacircle.dev/fields)
- [Datacircle documentation](https://datacircle.dev/docs)

## Skill Output:

**Output Type(s):** [JSON, CSV, SQL queries, Shell commands, Pricing-comparison guidance]

**Output Format:** [JSON or CSV catalog with tabular query results or concise comparison guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Catalog rows describe API providers and plans, including pricing and plan details.]

## Skill Version(s):

1.0.3 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
