## Description:

Analyze observed used-car listing price changes through Crawlora stored vehicle histories and selected live listings, preserving listing identity and crawl coverage.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Vehicle shoppers and researchers use this skill to compare dated asking-price changes and matched used-car listings while accounting for source coverage and observation gaps.

### Deployment Geography for Use:

United States

## Known Risks and Mitigations:

Risk: The Crawlora API key and vehicle-search parameters are sent to Crawlora, and searches may consume credits.

Mitigation: Keep the key private and set a credit and page budget before searching.

Risk: Observed listings and incomplete crawl coverage can be mistaken for completed sale prices or confirmed negotiation outcomes.

Mitigation: Present dated observations with coverage limits and verify the current listing and terms with the seller.

## Reference(s):

- [Crawlora endpoint reference](artifact/reference/endpoints.md)
- [ClawHub skill release](https://clawhub.ai/crawlora-org/skills/used-car-price-history-analysis)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Guidance]

**Output Format:** [Markdown price-event ledger, comparable-listing table, coverage notes, and seller-verification questions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Separates observed asking prices from sale prices and preserves source IDs, dates, and coverage caveats.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
