## Description:

Neural web search, parsed page contents, find-similar, and agentic Q&A over the live web through the superagnt unified API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[superagnt](https://clawhub.ai/user/superagnt)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and AI agents use this integration to search the live web, retrieve page content, find similar URLs, and generate answers with citations through a connected Exa account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Queries and requested URLs pass through superagnt to Exa, and usage may incur charges on the connected account.

Mitigation: Keep the API key in the SUPERAGNT_API_KEY environment variable, review permissions before connecting through MCP, and check account billing and rate limits.

Risk: The documented shell examples contain encoded quotes and bearer-header quoting that may fail when run as written.

Mitigation: Correct the shell quoting in the examples before running them.

## Reference(s):

- [Exa Integration documentation](https://superagnt.com/r/ch-exa-search-docs)
- [MCP installation guide](https://www.superagnt.com/install)
- [Exa account connections](https://app.superagnt.com/dashboard/connections)
- [superagnt API keys](https://superagnt.com/r/ch-exa-search-key)

## Skill Output:

**Output Type(s):** [API responses, Text, JSON]

**Output Format:** [JSON search, content, similar-link, or cited-answer responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses may include page text, highlights, summaries, similar URLs, and citations.]

## Skill Version(s):

2.0.10 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
