## Description:

Researches Costco products, categories, warehouse stock/availability, and reviews using the Crawlora API, returning clean JSON. Use when the user asks to find a Costco product, check delivery/warehouse availability, browse Costco categories, or pull Costco product reviews \u2014 instead of scraping Costco.com.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and shopping assistants use this skill to research public Costco products, compare categories, check US delivery availability, find nearby warehouses, and retrieve product reviews through Crawlora rather than scraping Costco.com.

### Deployment Geography for Use:

Global, with US-only delivery availability lookup

## Known Risks and Mitigations:

Risk: The skill sends Costco search terms, ZIP/state values, and coordinates supplied by the user to the Crawlora API.

Mitigation: Avoid precise coordinates unless warehouse lookup is needed, and disclose the third-party API use when handling location-sensitive requests.

Risk: The helper requires a Crawlora API key.

Mitigation: Keep CRAWLORA_API_KEY in the environment only and out of committed files or chat transcripts.

Risk: Availability lookups are limited to US delivery destinations.

Mitigation: Use the availability endpoint only with a US ZIP code and two-letter state, and avoid presenting it as a non-US delivery check.

## Reference(s):

- [Endpoint reference](artifact/reference/endpoints.md)
- [Crawlora API base](https://api.crawlora.net/api/v1)
- [Crawlora](https://crawlora.net)
- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/costco-research)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Configuration, Guidance]

**Output Format:** [JSON API responses with concise Markdown guidance and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY; Costco delivery availability requires US postal_code and state; warehouse lookup requires latitude and longitude.]

## Skill Version(s):

1.0.15 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
