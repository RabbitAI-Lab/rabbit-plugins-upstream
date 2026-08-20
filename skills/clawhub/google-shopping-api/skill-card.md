## Description:

Search Google Shopping for products, compare merchant offers and prices, inspect product details, and page through stores using Scavio's structured JSON API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and shopping-research agents use this skill to search products across retailers, compare prices and seller offers, and retrieve product details, specs, ratings, variants, and store listings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product searches and lookup parameters are sent to Scavio using SCAVIO_API_KEY.

Mitigation: Keep SCAVIO_API_KEY in an environment variable or secret store, avoid committing it to source control, and disclose external API use where required.

Risk: Repeated searches, product lookups, and store pagination consume Scavio credits.

Mitigation: Inform the user before broad pagination, apply filters early, and limit calls to the results needed for the task.

## Reference(s):

- [Scavio Google Shopping API documentation](https://scavio.dev/docs/google-shopping?utm_source=clawhub&utm_medium=skill&utm_campaign=google-shopping-api)
- [Scavio rate limits](https://scavio.dev/docs/rate-limits?utm_source=clawhub&utm_medium=skill&utm_campaign=google-shopping-api)
- [ClawHub skill page](https://clawhub.ai/scavio-ai/skills/google-shopping-api)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown guidance with JSON API payloads and code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [API responses include product, merchant, price, rating, review, pagination, credit, timing, and cache fields when returned by Scavio.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
