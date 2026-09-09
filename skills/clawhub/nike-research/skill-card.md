## Description:

Researches Nike's catalog - categories, search, product detail, colorways, reviews, and nearby stores - using the Crawlora API, returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to search or browse Nike product data, compare prices and colorways, review product details and customer reviews, and locate nearby Nike stores through Crawlora's Nike endpoints.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The shell helper can send the Crawlora API key to an overridden API host.

Mitigation: Use the skill only in a trusted shell environment and unset or pin CRAWLORA_API_BASE to https://api.crawlora.net/api/v1 before using a real API key.

Risk: The helper script is broader than the Nike-focused skill description.

Mitigation: Prefer a Nike-only wrapper or review commands so they call only the documented /nike GET endpoints.

## Reference(s):

- [Nike endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)
- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/nike-research)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, JSON]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY; API responses are paginated for search and reviews.]

## Skill Version(s):

1.0.7 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
