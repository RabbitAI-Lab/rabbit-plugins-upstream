## Description:

Researches products, prices, availability, and search suggestions on Amazon (amazon.com) using the Crawlora API, returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to research Amazon.com products, compare prices and availability, inspect ASIN details, and gather Amazon search suggestions through the Crawlora API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled helper makes external Crawlora API calls and can send the API key to an overridden API base.

Mitigation: Keep CRAWLORA_API_BASE unset or pinned to https://api.crawlora.net/api/v1 before use.

Risk: Queries or request bodies sent through the helper may contain sensitive product or business research.

Mitigation: Avoid sending confidential text, credentials, customer data, or private research terms to the API.

Risk: The helper can call broader Crawlora paths even though the skill documents Amazon endpoints.

Mitigation: Restrict normal use to /amazon/product, /amazon/search, and /amazon/suggest unless broader Crawlora access is separately reviewed.

## Reference(s):

- [Amazon Research endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)
- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/amazon-research)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a Crawlora API key in CRAWLORA_API_KEY and returns normalized Amazon product, search, and suggestion data.]

## Skill Version(s):

1.0.8 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
