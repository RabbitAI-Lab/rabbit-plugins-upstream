## Description:

Connects an Exa account through the superagnt unified API for neural and keyword web search, page content, similar links, and cited agentic Q&A.

This skill is ready for commercial/non-commercial use.

## Publisher:

[superagnt](https://clawhub.ai/user/superagnt)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and AI agents use the skill to search the live web, retrieve and summarize page content, find similar sources, and answer questions with citations. It also provides setup guidance for connecting an Exa account through superagnt.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The documented install check queries account credits, which the security summary flags as outside the stated web-research purpose; the skill also makes external API calls.

Mitigation: Review the credit lookup and API destination if this behavior matters, and use only the endpoints needed for the user's request.

## Reference(s):

- [Exa Integration documentation](https://superagnt.com/r/ch-exa-search-docs)
- [superagnt MCP installation guide](https://www.superagnt.com/install)
- [Connect an Exa account](https://app.superagnt.com/dashboard/connections)
- [superagnt API key setup](https://superagnt.com/r/ch-exa-search-key)

## Skill Output:

**Output Type(s):** [Text, API Calls, Shell commands, Configuration instructions]

**Output Format:** [Markdown guidance, inline shell commands, and text or structured results from web APIs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Search answers can include citations; results depend on the connected Exa account and the requested endpoint.]

## Skill Version(s):

2.0.17 (source: frontmatter, server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
