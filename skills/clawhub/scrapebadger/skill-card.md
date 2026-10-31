## Description:

ScrapeBadger provides APIs for web scraping, ecommerce and marketplace data, social media, search, real-estate listings, and cited AI answers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[0xghostcasper](https://clawhub.ai/user/0xghostcasper)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and researchers use the skill to retrieve web, marketplace, social, search, real-estate, and AI answer data through ScrapeBadger APIs. Requests require a ScrapeBadger API key and may incur service usage costs.

### Deployment Geography for Use:

Global, subject to the market coverage of each API.

## Known Risks and Mitigations:

Risk: Queries, URLs, images, and prompts are sent to ScrapeBadger; AI prompts may also reach named upstream services.

Mitigation: Avoid confidential inputs and URLs containing access tokens. Use supported POST requests for prompts where possible to reduce exposure in URL logs.

Risk: The API key could be exposed, and paid requests can incur usage costs.

Mitigation: Protect SCRAPEBADGER_API_KEY and set a spending limit.

## Reference(s):

- [ScrapeBadger API documentation](https://docs.scrapebadger.com)
- [ScrapeBadger service](https://scrapebadger.com)

## Skill Output:

**Output Type(s):** [JSON, Text, Cited sources]

**Output Format:** [Structured API results, primarily JSON, with text summaries or cited sources when requested.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Coverage varies by API and market; requires SCRAPEBADGER_API_KEY.]

## Skill Version(s):

1.9.0 (source: frontmatter, server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
