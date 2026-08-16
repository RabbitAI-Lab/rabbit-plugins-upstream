## Description:

Researches Wish's marketplace — categories, product search, product detail, related items, and reviews — using the Crawlora API, returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to research Wish categories, products, related items, and reviews through Crawlora. It supports product discovery and comparison using price, rating, review count, merchant, and review data without scraping Wish directly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled helper can call arbitrary Crawlora API paths, not only the documented Wish endpoints.

Mitigation: Use only the documented /wish endpoints and review requested API paths before execution.

Risk: Marketplace queries or product review prompts may contain confidential or sensitive user text.

Mitigation: Avoid placing confidential text in marketplace queries and review outgoing requests before sending them to Crawlora.

Risk: A Crawlora API key could be exposed if it is hardcoded or committed.

Mitigation: Keep the API key in the CRAWLORA_API_KEY environment variable and do not include it in code, query parameters, or repository files.

## Reference(s):

- [ClawHub skill page: wish-research](https://clawhub.ai/tonywangcn/skills/wish-research)
- [Wish endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY; results are based on public Wish marketplace data returned by Crawlora.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
