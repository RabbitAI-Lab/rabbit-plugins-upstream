## Description:

Fetch LinkedIn company, job, people, post, and professional network data through the superagnt API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[superagnt](https://clawhub.ai/user/superagnt)

### License/Terms of Use:

MIT-0

## Use Case:

Sales, recruiting, and research agents use this skill to enrich company and professional profiles, search jobs and posts, and gather LinkedIn context for account research or candidate dossiers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Lookup parameters are sent to the third-party superagnt service, which uses the account's credits.

Mitigation: Keep lookups within the information you intend to send to the service and monitor credit usage.

Risk: The API key could be exposed if shared in chat or stored insecurely.

Mitigation: Keep SUPERAGNT_API_KEY in secure environment configuration and do not share it in chat.

Risk: Some packaged curl examples contain escaped characters that can prevent direct execution.

Mitigation: Review and correct the example command quoting before running it.

Risk: The optional MCP connection requires reviewing and approving its permissions.

Mitigation: Review the requested permissions before connecting the MCP server.

Risk: The packaged review does not cover the provider's live data handling.

Mitigation: Review the provider's current privacy and data-handling terms before sending lookup data.

## Reference(s):

- [LinkedIn Data documentation](https://superagnt.com/r/ch-linkedin-data-docs)
- [superagnt API key and credits](https://superagnt.com/r/ch-linkedin-data-key)
- [LinkedIn MCP setup](https://www.superagnt.com/install?facet=linkedin)
- [LinkedIn Data ClawHub listing](https://clawhub.ai/superagnt/skills/linkedin-data)

## Skill Output:

**Output Type(s):** [JSON data, Lookup results]

**Output Format:** [Structured JSON responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Response fields vary by lookup endpoint.]

## Skill Version(s):

2.0.12 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
