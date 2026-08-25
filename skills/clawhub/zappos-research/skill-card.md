## Description:

Researches Zappos's footwear and apparel catalog using the Crawlora API, including brand listings, product search, and product detail such as pricing, images, ratings, fit feedback, and color variants.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to research public Zappos footwear and apparel catalog data through Crawlora instead of scraping Zappos pages directly. It supports brand discovery, catalog browsing, keyword search, product detail lookup, and comparison of price, rating, fit feedback, and variants.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The included Crawlora helper can use the same API key to call Crawlora endpoints beyond the advertised Zappos scope.

Mitigation: Review before installing, use a Crawlora key appropriate for this skill, and consider restricting or editing the helper to allow only /zappos/* GET endpoints.

## Reference(s):

- [zappos-research endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Skill listing on ClawHub](https://clawhub.ai/tonywangcn/skills/zappos-research)
- [Publisher profile on ClawHub](https://clawhub.ai/user/tonywangcn)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses Crawlora API responses as normalized JSON; requires CRAWLORA_API_KEY.]

## Skill Version(s):

1.0.3 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
