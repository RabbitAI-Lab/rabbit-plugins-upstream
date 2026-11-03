## Description:

Neural web search, parsed page contents, find-similar, and agentic Q&A over the live web through the superagnt unified API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[superagnt](https://clawhub.ai/user/superagnt)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers can use this skill to search the live web, retrieve and summarize page content, find related URLs, and generate answers grounded in cited sources through a connected Exa account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search queries and submitted URLs are handled through Superagnt using the connected Exa account, so account billing and rate limits apply.

Mitigation: Avoid submitting sensitive queries or URLs unless appropriate, and monitor usage on the connected Exa account.

Risk: The API key grants access to the connected service and could be exposed if shared in chat or logs.

Mitigation: Keep SUPERAGNT_API_KEY in the environment and out of conversation text and shared logs.

Risk: The optional MCP connection uses OAuth permissions, and its live implementation was outside this artifact review.

Mitigation: Review the requested OAuth permissions before approving the MCP connection.

## Reference(s):

- [Exa Integration documentation](https://superagnt.com/r/ch-exa-search-docs)
- [Superagnt API key setup](https://superagnt.com/r/ch-exa-search-key)
- [Connected accounts page](https://app.superagnt.com/dashboard/connections)
- [MCP installation instructions](https://www.superagnt.com/install)
- [Exa Integration on ClawHub](https://clawhub.ai/superagnt/skills/exa-search)

## Skill Output:

**Output Type(s):** [Text, JSON, Citations]

**Output Format:** [Text or JSON responses with search results, page content, summaries, similar URLs, or answers with source citations.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses may include URLs, excerpts, highlights, summaries, and source citations; available fields depend on the selected endpoint and options.]

## Skill Version(s):

2.0.12 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
