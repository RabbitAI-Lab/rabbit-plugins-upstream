## Description:

Enables agents to search the live web, retrieve parsed page content, find similar URLs, and generate cited answers through Exa.

This skill is ready for commercial/non-commercial use.

## Publisher:

[superagnt](https://clawhub.ai/user/superagnt)

### License/Terms of Use:

MIT-0

## Use Case:

Developers building agent workflows can use this integration to search current web sources, retrieve page text and summaries, find similar pages, and answer questions with citations through their connected Exa account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Requests and URLs are processed through Superagnt and the connected Exa account, which may incur Exa billing.

Mitigation: Use the integration only if you accept that processing and billing, and keep SUPERAGNT_API_KEY in the environment rather than sharing it in chat.

Risk: Some command examples contain escaped characters and authorization-header quoting that need correction before execution.

Mitigation: Correct the escaped characters and quote the Authorization header before running the examples.

## Reference(s):

- [Exa Integration Documentation](https://superagnt.com/r/ch-exa-search-docs)
- [MCP Server](https://mcp.superagnt.com/mcp)
- [MCP Installation Instructions](https://www.superagnt.com/install)
- [API Key Setup](https://superagnt.com/r/ch-exa-search-key)
- [Exa Account Connections](https://app.superagnt.com/dashboard/connections)

## Skill Output:

**Output Type(s):** [Text, API calls, Shell commands, Configuration guidance]

**Output Format:** [Markdown with curl examples and JSON API payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Web search and page results can include citations; use requires a connected Exa account and SUPERAGNT_API_KEY.]

## Skill Version(s):

2.0.11 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
