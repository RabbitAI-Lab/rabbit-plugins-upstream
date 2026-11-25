## Description:

Live web search, news, search-and-read, screenshots, URL-to-markdown extract and JavaScript page render for agents via AgentSearch. Free tier with no API key or account (25 free searches per IP in total, 10 free news / search-and-read / screenshot calls per IP each, small daily extract/render trials), then pay per call over x402 with USDC on Base. Use when a task needs current web results, recent news, a page screenshot, or the readable text of a URL.

This skill is ready for commercial/non-commercial use.

## Publisher:

[agentsearchhq-coder](https://clawhub.ai/user/agentsearchhq-coder)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to find current web information, search recent news, read public URLs as Markdown, and capture or render webpages when a task needs current online sources.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search queries and URLs are processed by AgentSearch and upstream providers, so sensitive content could be disclosed.

Mitigation: Do not include credentials, personal or confidential data, or private and token-bearing URLs in requests.

Risk: Calls may become paid after free limits and incur per-call USDC charges.

Mitigation: Use paid endpoints only with an authorized x402 wallet or client and a suitable spend cap.

## Reference(s):

- [AgentSearch](https://agentsearchhq.com)
- [AgentSearch x402 documentation](https://agentsearchhq.com/docs/x402)
- [AgentSearch MCP source repository](https://github.com/agentsearchhq-coder/agentsearch-mcp)

## Skill Output:

**Output Type(s):** [Text, Markdown, Images]

**Output Format:** [Search results and news as text, URL extracts as Markdown, and screenshots as images]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on the selected endpoint and its availability.]

## Skill Version(s):

1.0.2 (source: frontmatter, server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
