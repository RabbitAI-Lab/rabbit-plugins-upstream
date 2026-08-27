## Description:

Researches products, prices, availability, and search suggestions on Amazon using the Crawlora API and returns clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to search Amazon listings, look up ASIN details, check prices and availability, and retrieve Amazon keyword suggestions without scraping pages.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper script can call broader Crawlora API endpoints than the Amazon-only skill description indicates.

Mitigation: Review or restrict scripts/crawlora.sh before use so agents cannot use the same API key for non-Amazon endpoints or arbitrary POST requests.

Risk: Product searches and ASINs are sent to Crawlora.

Mitigation: Install only when that data sharing is acceptable for the intended workflow.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)
- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/amazon-research)

## Skill Output:

**Output Type(s):** [API Calls, JSON, Shell commands, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY; search results are paginated.]

## Skill Version(s):

1.0.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
