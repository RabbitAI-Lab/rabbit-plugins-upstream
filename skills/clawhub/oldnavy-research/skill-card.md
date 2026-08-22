## Description:

Researches Old Navy, Gap, Banana Republic, and Athleta catalog data with the Crawlora API, including categories, product details, colors and sizes, store pickup availability, nearby stores, and reviews.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to research Old Navy, Gap, Banana Republic, and Athleta products, categories, local pickup availability, nearby stores, and reviews through Crawlora instead of scraping storefront pages.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a Crawlora API key and sends product queries plus any store-location inputs to Crawlora.

Mitigation: Keep the key in CRAWLORA_API_KEY, do not hardcode or commit it, and prefer zip codes or store IDs instead of precise coordinates when checking local availability.

Risk: The included Crawlora helper can call unrelated API paths with arbitrary request data.

Mitigation: Use the helper only with the documented Old Navy, Gap, Banana Republic, and Athleta endpoints unless broader Crawlora access is intentional.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/oldnavy-research)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Guidance]

**Output Format:** [Markdown guidance with shell commands and API responses as JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY; may send product queries and store-location inputs to Crawlora.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
