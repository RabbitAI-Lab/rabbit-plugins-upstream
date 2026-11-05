## Description:

Connects an Exa account through superagnt to search the live web, retrieve page content, find similar URLs, and generate answers with citations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[superagnt](https://clawhub.ai/user/superagnt)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this integration to find current web sources, retrieve and summarize page content, discover related URLs, and answer questions with citations through a connected Exa account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API credentials could be exposed if included in chat or command text.

Mitigation: Store the key in SUPERAGNT_API_KEY and avoid sharing it in chat.

Risk: Queries and URLs are sent to superagnt and Exa, and Exa usage may incur charges.

Mitigation: Send only information intended for those services and check expected usage costs.

Risk: The documented shell examples need quoting corrections, and enabling MCP exposes workspace tools and permissions.

Mitigation: Correct command quoting before execution; review the MCP tools and permissions before enabling the connection.

## Reference(s):

- [Exa Integration documentation](https://superagnt.com/r/ch-exa-search-docs)
- [MCP client setup](https://www.superagnt.com/install)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Search results, page content, highlights, summaries, and cited answers, with Markdown guidance and curl examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses may include citations and depend on the connected Exa account.]

## Skill Version(s):

2.0.13 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
