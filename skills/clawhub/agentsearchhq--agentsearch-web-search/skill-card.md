## Description:

Live web search, URL-to-markdown extract and JavaScript page render for agents via AgentSearch. Free tier with no API key or account (25 free searches per IP in total, small daily extract/render trials), then pay per call over x402 with USDC on Base (search $0.003). Use when a task needs current web results or the readable text of a URL.

This skill is ready for commercial/non-commercial use.

## Publisher:

[agentsearchhq](https://clawhub.ai/user/agentsearchhq)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers can use the skill to retrieve current web search results, read a URL as Markdown, or render JavaScript-heavy pages when a task needs information from the web. Avoid sending confidential details or private URLs, and use paid endpoints only with the user's payment setup and approval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search queries and submitted URLs are processed by AgentSearch and upstream search providers.

Mitigation: Do not send passwords, API keys, personal data, confidential details, or private or token-bearing URLs; ask the user before sending confidential material.

Risk: Paid x402 requests spend USDC per call.

Mitigation: Use paid endpoints only when the user has configured their own wallet or client and approved the charges, preferably with a spend cap.

Risk: The security review is incomplete because two local path-like references could not be resolved.

Mitigation: Review the complete skill source before relying on it.

## Reference(s):

- [AgentSearch](https://agentsearchhq.com)
- [AgentSearch x402 documentation](https://agentsearchhq.com/docs/x402)
- [AgentSearch MCP package source](https://github.com/agentsearchhq-coder/agentsearch-mcp)

## Skill Output:

**Output Type(s):** [Text, Markdown, Search results]

**Output Format:** [Structured search results and extracted page content as text or Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Search results include source URLs and may include snippets, publish dates, and site names.]

## Skill Version(s):

1.0.1 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
