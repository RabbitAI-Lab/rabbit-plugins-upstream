## Description:

Researches Zappos footwear and apparel catalog data through the Crawlora API, including brands, search results, product details, pricing, images, ratings, fit feedback, and color variants.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agents use this skill to research public Zappos catalog data through Crawlora without scraping zappos.com directly. It supports brand lookup, product search, product detail retrieval, pricing and rating comparison, color variant review, and fit-feedback checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Crawlora receives the user's API key and Zappos search, brand, and product lookup parameters.

Mitigation: Keep CRAWLORA_API_KEY in the environment, do not commit it to files, and avoid sensitive personal data in lookup terms.

Risk: Zappos catalog responses can be paginated, empty, or limited to the documented product-detail fields.

Mitigation: Use pagination for brand and search workflows, treat empty responses as normal when documented, and verify decisions against returned pricing, rating, variant, and fit fields.

Risk: The skill accesses public Zappos catalog data through Crawlora and does not establish independent permission to use the underlying site data.

Mitigation: Use the data for the requested catalog research purpose and respect Zappos terms and any applicable usage restrictions.

## Reference(s):

- [zappos-research ClawHub page](https://clawhub.ai/crawlora-org/skills/zappos-research)
- [Endpoint reference](artifact/reference/endpoints.md)
- [Crawlora](https://crawlora.net)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY; brand, search, and brand-directory results are paginated.]

## Skill Version(s):

1.0.13 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
