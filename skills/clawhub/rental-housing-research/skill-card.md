## Description:

Research public rental communities and NYC housing listings or market series through Crawlora StreetEasy and Greystar.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Renters and housing researchers use this skill to compare public rental listings and communities, build sourced shortlists, and place NYC asking prices in dated market context. It distinguishes community starting rents from unit offers and flags unknown availability or costs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The Crawlora API key or housing search criteria could be exposed.

Mitigation: Keep CRAWLORA_API_KEY in a secure environment variable, avoid logging it, and share only search criteria intended for Crawlora.

Risk: Listings may be stale, and advertised prices or availability may not reflect final housing terms.

Mitigation: Check original source URLs and collection times; verify availability, fees, concessions, and lease terms before making housing decisions.

## Reference(s):

- [Rental housing research endpoint reference](artifact/reference/endpoints.md)
- [ClawHub skill listing](https://clawhub.ai/crawlora-org/skills/rental-housing-research)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown rental shortlist and dated market comparisons]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes source URLs, collection times, price basis, and explicit unknowns.]

## Skill Version(s):

1.0.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
