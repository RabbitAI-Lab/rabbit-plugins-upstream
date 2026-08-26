## Description:

Researches Old Navy's catalog and Gap Inc. sibling storefronts Gap, Banana Republic, and Athleta by using the Crawlora API to return clean JSON for categories, products, colors, sizes, in-store pickup availability, and reviews.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

External users and shopping research agents use this skill to search and browse Old Navy, Gap, Banana Republic, and Athleta product data, check local pickup availability, find nearby stores, and summarize product reviews without scraping storefront HTML.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper script is a broad Crawlora API client and can send requests outside the Old Navy-family lookup purpose.

Mitigation: Limit use to the documented Old Navy-family GET endpoints and avoid using the helper as a general-purpose Crawlora client.

Risk: The skill requires a Crawlora API key and allows external calls to Crawlora.

Mitigation: Install only when external Crawlora calls are acceptable, keep the API key in CRAWLORA_API_KEY, and do not hardcode or commit credentials.

Risk: Availability and store lookup endpoints can use zip codes or precise latitude and longitude.

Mitigation: Prefer store IDs, zip codes, or coarse location inputs when sufficient, and use precise coordinates only when needed.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)
- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/oldnavy-research)

## Skill Output:

**Output Type(s):** [JSON, API Calls, Shell commands, Guidance]

**Output Format:** [Markdown guidance with shell commands that return JSON from API calls]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a Crawlora API key in CRAWLORA_API_KEY; endpoint responses are normalized JSON.]

## Skill Version(s):

1.0.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
