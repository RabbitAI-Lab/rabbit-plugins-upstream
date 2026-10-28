## Description:

Connects to the LinkedIn Data API with one superagnt bearer token to retrieve company, job, profile, post, and professional network data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[superagnt](https://clawhub.ai/user/superagnt)

### License/Terms of Use:

MIT-0

## Use Case:

Sales, recruiting, and research agents use the skill to retrieve LinkedIn company, job, profile, and post data for enrichment and analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The optional MCP connection may expose workspace tools beyond LinkedIn lookups; the LinkedIn URL alone does not enforce a LinkedIn-only boundary.

Mitigation: Before approving the connection, inspect the enabled tools and workspace permissions and allow only the access needed.

Risk: Queries are processed by a third party and API requests can incur credit charges.

Mitigation: Protect the API key and account for third-party processing and credit use before making requests.

## Reference(s):

- [LinkedIn Data documentation](https://superagnt.com/r/ch-linkedin-data-docs)
- [LinkedIn Data API](https://api.superagnt.com/v1/data/linkedin)
- [LinkedIn Data ClawHub listing](https://clawhub.ai/superagnt/skills/linkedin-data)

## Skill Output:

**Output Type(s):** [JSON, Guidance, Shell commands]

**Output Format:** [API requests and structured JSON responses, with Markdown usage instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requests require a superagnt API key; usage consumes account credits.]

## Skill Version(s):

2.0.10 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
