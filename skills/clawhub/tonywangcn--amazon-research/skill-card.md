## Description:

Researches products, prices, availability, and search suggestions on Amazon (amazon.com) using the Crawlora API, returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and researchers use this skill to search Amazon listings, look up product details by ASIN, check prices and availability, and collect Amazon search suggestions through Crawlora instead of scraping pages directly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled Crawlora helper can call broader Crawlora paths than the Amazon-only purpose documented for this skill.

Mitigation: Constrain use to the documented GET endpoints /amazon/search, /amazon/product/{asin}, and /amazon/suggest/{keyword} before deployment in sensitive environments.

Risk: The skill sends requests to Crawlora and requires a Crawlora API key.

Mitigation: Store the key only in CRAWLORA_API_KEY, avoid committing it, and review outbound API use before installing in restricted environments.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora API base](https://api.crawlora.net/api/v1)
- [Crawlora](https://crawlora.net)
- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/amazon-research)

## Skill Output:

**Output Type(s):** [API Calls, Shell commands, Configuration, JSON, Guidance]

**Output Format:** [Markdown guidance with shell commands that return JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY; Amazon search results are paginated and all documented Amazon endpoints target amazon.com.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
