## Description:

Search Google Hotels for a destination and dates, then fetch per-property vendor pricing and full details as structured JSON with price, rating, class, and amenity filters.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent builders use this skill to search lodging options, compare hotels or vacation rentals, and retrieve property details and vendor pricing through Scavio's Google Hotels API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Hotel searches and stay details are sent to Scavio using the configured SCAVIO_API_KEY.

Mitigation: Keep SCAVIO_API_KEY in an environment variable or secret store, and avoid committing it to source code.

Risk: Search and detail requests consume paid or free Scavio account credits.

Mitigation: Confirm query criteria before making API calls and monitor credit usage for the account tied to the API key.

Risk: Returned hotel names, prices, ratings, vendors, and availability can be misrepresented if the agent fabricates missing data or omits context.

Mitigation: Return only API-provided data and state the requested stay dates and currency when quoting prices.

## Reference(s):

- [Scavio Google Hotels API documentation](https://scavio.dev/docs/google-hotels?utm_source=agent-skills&utm_medium=skill&utm_campaign=google-hotels-api)
- [Scavio rate limits](https://scavio.dev/docs/rate-limits?utm_source=agent-skills&utm_medium=skill&utm_campaign=google-hotels-api)
- [ClawHub skill page](https://clawhub.ai/scavio-ai/skills/google-hotels-api)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration, JSON]

**Output Format:** [Markdown with inline bash and Python code blocks plus JSON response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY; API calls consume Scavio credits.]

## Skill Version(s):

1.0.3 (source: server release metadata; artifact frontmatter reports 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
