## Description:

Search Google Shopping for products, fetch full product pages, and page through merchant offers as structured JSON with price, seller, rating, and sale filters.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and shopping-research agents use this skill to search Google Shopping, compare merchant offers and prices, and retrieve product details as structured JSON.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Shopping queries and request parameters are sent to Scavio's API.

Mitigation: Disclose external API use to users and avoid sending sensitive shopping intent or private data unless appropriate for the deployment.

Risk: The skill requires SCAVIO_API_KEY for authenticated requests.

Mitigation: Store SCAVIO_API_KEY in an environment variable or secret store and keep it out of source code and logs.

Risk: Requests and pagination consume Scavio account credits.

Mitigation: Inform the user before paging through many stores and monitor remaining credits or billing limits.

Risk: Product titles, prices, sellers, ratings, or availability may be missing, stale, or affected by upstream API errors.

Mitigation: Return only API-provided data, avoid fabricating missing values, and retry or broaden queries only when failure handling guidance supports it.

## Reference(s):

- [Scavio Google Shopping documentation](https://scavio.dev/docs/google-shopping)
- [Scavio rate limits](https://scavio.dev/docs/rate-limits)
- [ClawHub skill listing](https://clawhub.ai/scavio-ai/skills/google-shopping-api)

## Skill Output:

**Output Type(s):** [API Calls, JSON, Shell commands, Configuration guidance]

**Output Format:** [Markdown guidance with REST API examples and JSON response structures]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY; each documented endpoint consumes 1 account credit.]

## Skill Version(s):

1.0.1 (source: server release evidence; artifact frontmatter: 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
