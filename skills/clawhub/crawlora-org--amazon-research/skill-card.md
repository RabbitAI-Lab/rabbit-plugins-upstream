## Description:

Researches products, prices, availability, and search suggestions on Amazon (amazon.com) using the Crawlora API and returns clean JSON instead of scraping Amazon pages.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and commerce researchers use this skill to search Amazon listings, check product details by ASIN, compare price and availability, and gather Amazon search suggestions through Crawlora.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Amazon product keywords, ASINs, request parameters, and the Crawlora API key are sent to a third-party API.

Mitigation: Use the skill only when that data sharing is acceptable, avoid sensitive private queries, and keep the API key in the CRAWLORA_API_KEY environment variable.

Risk: Returned product, price, availability, and suggestion data may be incomplete or time-sensitive.

Mitigation: Review JSON results before using them for commercial decisions and re-run queries when current pricing or availability matters.

## Reference(s):

- [amazon-research endpoint reference](reference/endpoints.md)
- [Crawlora service](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)

## Skill Output:

**Output Type(s):** [guidance, shell commands, JSON]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and sends Amazon keywords, ASINs, request parameters, and the API key to Crawlora.]

## Skill Version(s):

1.0.16 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
