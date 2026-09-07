## Description:

Researches Zara's catalog — category taxonomy, category listings, product detail, keyword search, search suggestions, and nearby physical stores — using the Crawlora API, returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and shopping assistants use this skill to browse Zara categories, search product listings, inspect product variants and availability, and find nearby stores through Crawlora instead of scraping Zara pages directly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper script can be used beyond the documented Zara endpoints and can send CRAWLORA_API_KEY to an overridden API base.

Mitigation: Restrict usage to the documented /zara endpoints and use a fixed or validated https://api.crawlora.net/api/v1 base before using a real API key.

Risk: The skill requires an API key for Crawlora requests.

Mitigation: Keep the key in CRAWLORA_API_KEY only; do not hardcode, place it in query parameters, or commit it.

## Reference(s):

- [Zara endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/zara-research)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY; API calls return normalized Zara catalog and store JSON.]

## Skill Version(s):

1.0.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
