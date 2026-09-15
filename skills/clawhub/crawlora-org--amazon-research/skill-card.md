## Description:

Researches Amazon product listings, prices, availability, product details, and search suggestions through the Crawlora API and returns normalized JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to search Amazon, look up ASIN details, compare pricing and availability, and collect Amazon keyword suggestions without scraping Amazon pages.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Amazon search terms, ASINs, and the Crawlora API key are sent to Crawlora.

Mitigation: Keep the API key in CRAWLORA_API_KEY, avoid private information in product queries, and review Crawlora terms and billing limits before use.

Risk: Returned Amazon data is limited to public amazon.com product, search, and suggestion endpoints and may require pagination for complete result sets.

Mitigation: Use page parameters for broader searches and verify important pricing or availability before relying on the results.

## Reference(s):

- [Amazon Research Endpoint Reference](artifact/reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [ClawHub Skill Page](https://clawhub.ai/crawlora-org/skills/amazon-research)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses CRAWLORA_API_KEY from the environment and returns data from amazon.com endpoints.]

## Skill Version(s):

1.0.15 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
