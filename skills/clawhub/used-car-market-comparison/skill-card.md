## Description:

Compare used-car asking prices with matched local listings through Crawlora. Use for a vehicle shortlist, a comparable-listing price range, or explaining a listing's premium or discount by trim, mileage, condition, and location.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and vehicle-shopping assistants use this skill to collect comparable advertised listings from Crawlora, compare asking prices across matched cohorts, and explain premiums or discounts without treating listings as verified appraisals.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends scoped vehicle-search queries to Crawlora, a third-party service.

Mitigation: Install and use it only when third-party Crawlora processing is acceptable for the user's vehicle-shopping task.

Risk: The Crawlora API key is sensitive.

Mitigation: Keep CRAWLORA_API_KEY out of transcripts and command lines; use the bundled helper's credential-safe curl behavior.

Risk: Advertised listing prices can be mistaken for verified value, condition, or purchase cost.

Mitigation: Present results as listing evidence only, separate fees and history gaps, and avoid appraisals, out-the-door quotes, or mechanical-condition claims.

## Reference(s):

- [Crawlora](https://crawlora.net)
- [used-car-market-comparison endpoint reference](reference/endpoints.md)
- [Crawlora API base](https://api.crawlora.net/api/v1)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, API Calls, Guidance]

**Output Format:** [Markdown with comparable-listing tables, price summaries, source URLs, retrieval dates, exclusions, uncertainties, and optional shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses Crawlora API results as evidence; advertised listing prices are not verified market value, out-the-door quotes, transaction history, or mechanical-condition assessments.]

## Skill Version(s):

1.0.8 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
