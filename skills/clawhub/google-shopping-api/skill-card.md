## Description:

Search Google Shopping for products, fetch full product pages, and page through store offers as structured JSON with price, seller, rating, and sale filters.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to search products, compare merchant offers, inspect product details, and build shopping or price-comparison workflows through Scavio's Google Shopping API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API calls send product-search queries to Scavio.

Mitigation: Disclose the third-party API use to the user before making calls and avoid sending sensitive search terms.

Risk: Scavio API calls require an API key.

Mitigation: Keep SCAVIO_API_KEY in an environment variable or secret store and never hard-code it in source files.

Risk: Pagination across many stores can spend paid Scavio credits.

Mitigation: Ask before large pagination runs and report that each endpoint call consumes credits.

## Reference(s):

- [Scavio Google Shopping API documentation](https://scavio.dev/docs/google-shopping?utm_source=agent-skills&utm_medium=skill&utm_campaign=google-shopping-api)
- [Scavio rate limits](https://scavio.dev/docs/rate-limits?utm_source=agent-skills&utm_medium=skill&utm_campaign=google-shopping-api)
- [ClawHub skill page](https://clawhub.ai/scavio-ai/skills/google-shopping-api)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, Python examples, API request details, and JSON response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides API calls that return structured JSON product, offer, seller, rating, and pagination data.]

## Skill Version(s):

1.0.3 (source: ClawHub release evidence; artifact frontmatter reports 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
