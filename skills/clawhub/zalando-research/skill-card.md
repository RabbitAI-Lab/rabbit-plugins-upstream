## Description:

Researches products, prices, brands, and categories on Zalando (the European fashion marketplace) using the Crawlora API, returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and agents use this skill to research Zalando storefronts, product prices, SKU details, categories, brands, and search suggestions through Crawlora instead of scraping Zalando pages.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper script can use an environment-selected API base and may send the Crawlora API key and request data outside the stated endpoint.

Mitigation: Run the helper only in a controlled environment, leave CRAWLORA_API_BASE unset unless the target is trusted, and rotate the API key if it may have been used with an untrusted base URL.

Risk: Normal operation sends Zalando research queries to Crawlora using the user's API key.

Mitigation: Use a scoped Crawlora key from CRAWLORA_API_KEY, avoid hardcoding or committing the key, and review query data before sending it to the third-party API.

## Reference(s):

- [Zalando endpoint reference](reference/endpoints.md)
- [Crawlora API base](https://api.crawlora.net/api/v1)
- [Crawlora](https://crawlora.net)
- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/zalando-research)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, JSON]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a Crawlora API key in CRAWLORA_API_KEY; market is required for Zalando search, category, and product endpoints.]

## Skill Version(s):

1.0.7 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
