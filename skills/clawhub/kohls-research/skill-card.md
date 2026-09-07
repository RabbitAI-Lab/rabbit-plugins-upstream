## Description:

Researches Kohl's catalog by browsing category taxonomy for products, prices, ratings, and facets; pulls product reviews by web_id; finds nearby Kohl's stores; and returns search-box typeahead suggestions through the Crawlora API as clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to research public Kohl's catalog categories, reviews, typeahead suggestions, and nearby store information through Crawlora API calls rather than direct page scraping.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The included shell helper is broader than the Kohl's-only purpose and can call non-Kohl's Crawlora paths.

Mitigation: Restrict routine use to the four documented Kohl's GET endpoints before deployment.

Risk: CRAWLORA_API_BASE can redirect requests and expose the API key to an environment-controlled API base.

Mitigation: Use a dedicated Crawlora API key and set CRAWLORA_API_BASE only in trusted test environments.

Risk: Store searches can include precise user addresses.

Mitigation: Prefer ZIP code or city-level searches unless a full address is necessary.

## Reference(s):

- [Kohl's endpoint reference](artifact/reference/endpoints.md)
- [Crawlora](https://crawlora.net)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses CRAWLORA_API_KEY for authenticated Crawlora requests; API responses depend on the queried public Kohl's endpoint.]

## Skill Version(s):

1.0.6 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
