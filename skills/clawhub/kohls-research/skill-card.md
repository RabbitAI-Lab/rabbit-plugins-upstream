## Description:

Researches Kohl's catalog by browsing category taxonomy for products, prices, ratings, and facets; pulling product reviews by web_id; finding nearby Kohl's stores; and returning search-box typeahead suggestions via the Crawlora API as clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to research public Kohl's catalog categories, product reviews, store locations, and typeahead suggestions through the Crawlora API rather than scraping Kohls.com directly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The included helper can call broader Crawlora API paths and arbitrary request bodies beyond the documented Kohl's lookup endpoints.

Mitigation: Install only when this flexibility is acceptable, keep the Crawlora API key scoped and private, and prefer a version that restricts the helper to the four documented Kohl's GET endpoints with parameter validation.

## Reference(s):

- [kohls-research endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/kohls-research)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, json]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and returns public Kohl's catalog, review, store, and suggestion data from Crawlora endpoints.]

## Skill Version(s):

1.0.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
