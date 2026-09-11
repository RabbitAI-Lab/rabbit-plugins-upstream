## Description:

Compare used-car asking prices with matched local listings through Crawlora. Use for a vehicle shortlist, a comparable-listing price range, or explaining a listing's premium or discount by trim, mileage, condition, and location.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External buyers, sellers, and agents use this skill to gather matched used-car listings, compare advertised asking prices, and explain apparent premiums or discounts with clear sample limits.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends vehicle search criteria, listing IDs, ZIP codes, and the user's Crawlora API key to Crawlora.

Mitigation: Use the skill only when that data sharing is acceptable, keep the API key secret, and keep requests within the user's stated car-comparison scope.

Risk: Advertised listing samples can be incomplete, stale, or mismatched and do not prove transaction value, sale speed, mechanical condition, or an out-the-door quote.

Mitigation: Report retrieval dates, source URLs, match criteria, exclusions, sample size, fee and history gaps, and describe weak samples as ranges rather than precise valuations.

Risk: Unbounded searches can consume Crawlora credits or hit rate limits.

Mitigation: Use bounded pages and search criteria, monitor Crawlora credit use, back off on 429 responses, and treat failed fetches as unavailable evidence.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)
- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/used-car-market-comparison)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with comparable-listing tables, price summaries, source URLs, retrieval dates, and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses Crawlora listing data and should preserve match criteria, coverage limits, exclusions, uncertain matches, and fee or history gaps.]

## Skill Version(s):

1.0.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
