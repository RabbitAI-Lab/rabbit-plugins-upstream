## Description:

Analyzes observed used-car asking-price changes using Crawlora listing histories and selected live listings, with dated events, matched comparables, and coverage caveats.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Car shoppers and researchers use this skill to compare observed asking-price changes for US used-car listings and matched vehicles, while distinguishing recorded events from unobserved price history.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Vehicle searches send query details and a Crawlora API key to Crawlora.

Mitigation: Use a trusted key, keep it out of logs and shared outputs, and send only the vehicle details needed for the search.

Risk: Broad searches may consume more Crawlora credits than intended.

Mitigation: Set a vehicle scope, page limit, and credit budget before querying.

Risk: Incomplete crawl coverage or a single observed price can make price changes appear more certain than they are.

Mitigation: Show source and crawl dates, distinguish first observation from original price, and flag gaps and unverified seller claims.

## Reference(s):

- [Crawlora vehicle-listing endpoint reference](reference/endpoints.md)
- [ClawHub skill listing](https://clawhub.ai/crawlora-org/skills/used-car-price-history-analysis)

## Skill Output:

**Output Type(s):** [Analysis, Text, Guidance]

**Output Format:** [Markdown with price-event and comparable tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes observed dates, listing identities, sample sizes, coverage and freshness notes, discrepancies, and seller-verification questions.]

## Skill Version(s):

1.0.1 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
