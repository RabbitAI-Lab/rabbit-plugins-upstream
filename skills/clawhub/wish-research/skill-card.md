## Description:

Researches Wish marketplace categories, product search, product details, related items, and reviews through the Crawlora API and returns clean JSON for comparison or summarization.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to browse Wish categories, search products, inspect product details, find related items, and summarize reviews without scraping Wish HTML directly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper script can send the Crawlora API key through broader, configurable API requests than the Wish-only skill purpose requires.

Mitigation: Review before installing, keep CRAWLORA_API_BASE unset unless the destination is fully trusted, and prefer a Wish-specific wrapper that only permits the documented GET endpoints before exposing a real Crawlora key.

## Reference(s):

- [wish-research endpoint reference](artifact/reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)
- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/wish-research)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses Crawlora API responses for Wish marketplace data; callers should keep API keys in environment variables.]

## Skill Version(s):

1.0.6 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
