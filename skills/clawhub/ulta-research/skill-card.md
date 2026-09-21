## Description:

Researches Ulta Beauty's catalog, including categories, products, shades, questions, reviews, and nearby stores, through the Crawlora API and returns clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and shopping assistants use this skill to search or browse Ulta Beauty products, compare shades, review customer Q&A and reviews, and locate nearby Ulta stores without scraping Ulta pages.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Queries, product IDs, and store-location inputs are sent to Crawlora using the user's Crawlora API key.

Mitigation: Use the skill only when the user is comfortable sharing those inputs with Crawlora and avoid precise addresses or latitude/longitude unless nearby-store lookup is explicitly requested.

Risk: Product, review, Q&A, and store results may be incomplete, paginated, stale, or empty for unresolved inputs.

Mitigation: Follow pagination where needed, check product identifiers before relying on detail or review endpoints, and treat empty results as a signal to refine the query.

Risk: The helper requires a secret API key in the local environment.

Mitigation: Keep the key in CRAWLORA_API_KEY, do not hardcode or commit it, and use the provided helper so the key is not passed as a command-line argument.

## Reference(s):

- [Ulta Research Endpoint Reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [ClawHub Skill Page](https://clawhub.ai/crawlora-org/skills/ulta-research)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands that return JSON from the Crawlora API]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and uses scoped GET requests to documented Ulta endpoints.]

## Skill Version(s):

1.0.15 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
