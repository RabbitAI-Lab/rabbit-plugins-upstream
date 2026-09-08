## Description:

Researches Wish marketplace categories, product search results, product details, related items, and reviews through the Crawlora API, returning normalized JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to research public Wish marketplace data, including category browsing, product search, product detail checks, related-item discovery, review summaries, and price or rating comparisons.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Wish queries and product IDs are sent to Crawlora.

Mitigation: Do not include secrets, personal data, or sensitive business information in queries, product IDs, or JSON bodies.

Risk: The helper can send the API key to a configurable API base.

Mitigation: Keep CRAWLORA_API_BASE unset unless the destination is fully trusted, and use the lowest-privilege Crawlora API key available.

Risk: The helper script is broader than the stated Wish-only purpose.

Mitigation: Restrict usage to the documented Wish endpoints before broad deployment.

## Reference(s):

- [Wish endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/wish-research)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY; API responses cover public Wish marketplace data and are subject to endpoint count and pagination limits.]

## Skill Version(s):

1.0.7 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
