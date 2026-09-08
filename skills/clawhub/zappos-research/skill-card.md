## Description:

Researches Zappos's footwear and apparel catalog, including brands, product search, pricing, images, ratings, fit feedback, and color variants, through the Crawlora API and returns clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to research public Zappos footwear and apparel listings without scraping zappos.com directly. It supports brand discovery, catalog browsing, product search, and product-detail comparison using Crawlora API responses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled helper can send authenticated requests to arbitrary Crawlora paths and can use an environment-selected API host, which is broader than narrow Zappos lookup.

Mitigation: Review before installation, keep CRAWLORA_API_KEY scoped and private, prefer the documented /zappos endpoints, and avoid setting CRAWLORA_API_BASE unless the target host is explicitly trusted.

## Reference(s):

- [Zappos endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY; results are paginated and limited to public Zappos catalog data exposed by the Crawlora endpoints.]

## Skill Version(s):

1.0.7 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
