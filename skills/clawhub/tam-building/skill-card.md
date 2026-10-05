## Description:

Guides teams through defining an ideal customer profile, estimating sourcing costs, and deploying a Cargo model of matching companies.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

RevOps, GTM engineering, and sales leadership teams use this skill to turn an approved ideal customer profile into a sourced account universe in Cargo, with company counts and spend reviewed before sourcing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Company, customer-domain, and ICP details may be shared with external enrichment or search providers.

Mitigation: Review the providers and data sent to them before connecting or sourcing.

Risk: Company sourcing can incur per-record charges.

Mitigation: Confirm live prices, candidate counts, the record limit, and maximum spend before a paid sync.

Risk: Unpinned installation dependencies may change between runs.

Mitigation: Review and pin the CLI dependency and cargo-cdk installation source when reproducibility matters.

Risk: The example ideal customer profile may not match the deploying organization.

Mitigation: Replace or verify the example profile and approve industries, company size, and countries before deployment.

## Reference(s):

- [Cargo GTM skills homepage](https://github.com/getcargohq/gtm-skills)
- [Configure the account universe](references/configure.md)
- [Sourcing and reporting](references/run.md)
- [Available data sources](references/sources.md)

## Skill Output:

**Output Type(s):** [Code, Configuration, Guidance, Markdown]

**Output Format:** [Cargo CDK model configuration and Markdown report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [A deployed company model and a report of sourced records, market breakdowns, and estimated versus actual spend.]

## Skill Version(s):

0.5.0 (source: skill frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
