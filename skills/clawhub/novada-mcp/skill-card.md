## Description:

Connect OpenClaw to Novada MCP for web scraping, SERP API and web search across Google, Bing, DuckDuckGo and Yandex, with page extraction, crawling, structured Amazon, YouTube and LinkedIn data, and proxy access. Use when the user needs live web data, SERP results, product or social data, or asks to set up or troubleshoot the Novada connection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[novada-proxy](https://clawhub.ai/user/novada-proxy)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use Novada MCP to search the live web, extract pages, retrieve structured platform data, monitor pages, and access proxy services through a Novada account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan could not resolve a referenced path, leaving the scan evidence incomplete.

Mitigation: Review the skill and verify the unresolved reference before installation.

Risk: Scraping calls are billed to the user's Novada account.

Mitigation: Use a small result limit for initial requests and confirm expected account usage before scaling up.

Risk: Setup and account-management commands can change the saved MCP connection or account data.

Mitigation: Review the command and its effects with the user before running it; create proxy sub-accounts only when requested.

## Reference(s):

- [Novada MCP product page](https://novada.com/products/novada-mcp/)
- [ClawHub release page](https://clawhub.ai/novada-proxy/skills/novada-mcp)

## Skill Output:

**Output Type(s):** [Text, Structured data, Guidance]

**Output Format:** [Text and structured records returned by MCP tools]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results vary by search, scraping, extraction, monitoring, or proxy request.]

## Skill Version(s):

1.0.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
