## Description:

Search Google Shopping for products, fetch a full product page, and page through every store selling a product as structured JSON with price, seller, rating, and price or sale filters.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external agents use this skill to search Google Shopping through Scavio, compare product offers across retailers, and retrieve product details or store listings for shopping research workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Shopping queries and lookup parameters are sent to Scavio using SCAVIO_API_KEY.

Mitigation: Use the skill only for queries appropriate to send to Scavio, keep the API key in environment or secret storage, and avoid placing the key in source files or chat output.

Risk: Paging through many store listings can consume credits quickly.

Mitigation: Have the agent state expected pagination before continuing and monitor credit usage or account balance during broad store lookups.

Risk: Product titles, prices, sellers, and ratings may be stale or unavailable if the API response is incomplete or empty.

Mitigation: Return only facts present in Scavio API responses and loosen filters or broaden the query when searches return no results.

## Reference(s):

- [Scavio Google Shopping documentation](https://scavio.dev/docs/google-shopping?utm_source=agent-skills&utm_medium=skill&utm_campaign=google-shopping-api)
- [Scavio rate limits](https://scavio.dev/docs/rate-limits?utm_source=agent-skills&utm_medium=skill&utm_campaign=google-shopping-api)
- [ClawHub skill listing](https://clawhub.ai/scavio-ai/skills/google-shopping-api)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with bash and Python examples; API responses are JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY. Each documented endpoint call consumes 1 credit, and agents should return product facts only from API responses.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
