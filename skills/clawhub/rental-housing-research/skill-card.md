## Description:

Research public rental communities and NYC housing listings or market series through Crawlora StreetEasy and Greystar to build shortlists and compare advertised offers in context.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Renters and housing researchers use this skill to compare public rental listings, build sourced shortlists, and place NYC asking prices in dated market context. StreetEasy covers NYC-area listings and market series; Greystar covers its published communities in discovered markets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Rental search locations, budgets, and listing queries are sent to Crawlora with an API key.

Mitigation: Use a protected Crawlora API key and limit queries to the requested housing research.

Risk: Advertised rents or listing snapshots may omit fees, change, or no longer reflect availability.

Mitigation: Retain source URLs and collection times, distinguish prices and fees, and verify listing details before taking action.

## Reference(s):

- [Rental housing research endpoint reference](reference/endpoints.md)
- [ClawHub rental-housing-research release](https://clawhub.ai/crawlora-org/skills/rental-housing-research)

## Skill Output:

**Output Type(s):** [Markdown, Analysis, Guidance]

**Output Format:** [Markdown shortlist with listing and market comparisons]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes listing identities, price basis, source URLs, observation dates, and unresolved costs or availability.]

## Skill Version(s):

1.0.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
