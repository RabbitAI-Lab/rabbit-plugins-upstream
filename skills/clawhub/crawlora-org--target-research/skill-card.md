## Description:

Researches Target catalog categories, products, filters, prices, questions, and reviews through the Crawlora API and returns normalized JSON instead of scraping target.com.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to answer Target product research requests, including product search, category browsing, price and availability checks, and review or Q&A summaries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Target lookup requests and Crawlora API keys are sent to Crawlora.

Mitigation: Keep CRAWLORA_API_KEY in the environment, do not hardcode or commit it, and review Crawlora's handling of request data before sending sensitive searches, store ids, or product interests.

Risk: Product listings, pricing, reviews, and availability can be paginated or store-specific.

Mitigation: Use the documented page, per_page, count, and store_id parameters when completeness or local availability matters.

## Reference(s):

- [Target endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses CRAWLORA_API_KEY from the environment and returns paginated public Target catalog data from documented Crawlora endpoints.]

## Skill Version(s):

1.0.15 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
