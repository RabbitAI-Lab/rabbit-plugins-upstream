## Description:

Live data and AI tools over plain HTTP, paid per call with no account: web search, page and PDF text, news, website audits, speech, token prices and technical indicators, wallet and chain reads, sanctions and payee checks, CVE, company and SEC lookups, stock quotes, FX, weather and 680+ more. Pay each call from a wallet over x402 (USDC) or with a prepaid key. Use when a task needs current information or an outside lookup and no better tool is connected. The tool finder is free.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nutshell2000](https://clawhub.ai/user/nutshell2000)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use the skill to retrieve current information or perform external lookups when no better connected tool is available. It can return web, media, market, blockchain, compliance, company, and other data through the documented service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review flags possible exposure of prepaid API keys through the URL-based MCP fallback; the scan was partial, and external disclosure of task details is an unconfirmed concern.

Mitigation: Use the documented Authorization or X-API-Key header option instead of putting a key in a URL, and consider whether the task details are appropriate to send to the external service.

## Reference(s):

- [Service homepage](https://agent-data-tools.revmesh2074.workers.dev)
- [API catalog (OpenAPI)](https://agent-data-tools.revmesh2074.workers.dev/openapi.json)
- [API catalog guide](https://agent-data-tools.revmesh2074.workers.dev/llms.txt)
- [Prepaid credits](https://agent-data-tools.revmesh2074.workers.dev/credits)
- [Publisher profile](https://clawhub.ai/user/nutshell2000)
- [Support issues](https://github.com/Nutshell2000/agent-data-tools/issues)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Guidance]

**Output Format:** [Data returned by external tools, commonly JSON or extracted text/Markdown, with usage guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses depend on the selected tool; some tools return media or encoded media data.]

## Skill Version(s):

1.0.0 (source: SKILL.md frontmatter, server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
