## Description:

Search Google and get the full structured SERP as JSON: organic results, ads, knowledge graph, AI overview, related questions, and more.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to retrieve current Google search results and structured SERP features through Scavio when an answer requires up-to-date web information.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search queries are sent to Scavio's external service.

Mitigation: Do not send passwords, private internal text, customer data, or other sensitive material unless that use has been approved by the organization.

Risk: The skill requires a Scavio API key.

Mitigation: Store SCAVIO_API_KEY in an environment variable or approved secret store and keep it out of source control.

## Reference(s):

- [Scavio Search API documentation](https://scavio.dev/docs/search-api)
- [Scavio rate limits](https://scavio.dev/docs/rate-limits)
- [ClawHub skill listing](https://clawhub.ai/scavio-ai/skills/scavio-google)

## Skill Output:

**Output Type(s):** [JSON, Markdown, Guidance]

**Output Format:** [Structured SERP JSON from the Scavio Google API, usually summarized for the user in Markdown with cited source URLs.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY; supports localization, pagination, recency filters, SafeSearch, AI Overview resolution, and optional raw HTML.]

## Skill Version(s):

3.0.3 (source: server release evidence; artifact frontmatter lists 3.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
