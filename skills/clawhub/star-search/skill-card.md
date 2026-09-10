## Description:

Star Search helps agents run Chinese and English web, news, finance, academic, and code searches and produce source-linked LLM answers through MCP, API, LangChain, and Dify integrations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[muchenhengxin](https://clawhub.ai/user/muchenhengxin)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent builders use this skill to add real-time search, research, news, finance, academic, and code lookup to agent workflows. It is especially oriented toward Chinese web search with source-linked LLM answers and integration paths for MCP, LangChain, Dify, CLI, and HTTP/SSE APIs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security evidence says this release bundles unsafe account, payment, credential, upload, and broad web-fetching behavior.

Mitigation: Treat it as a Review install and avoid running it as a public service or on a machine or account with valuable local credentials until those areas are removed, secured, or reviewed.

Risk: Broad web fetching can expose the host or service to unsafe URL access patterns.

Mitigation: Sandbox or allowlist arbitrary URL fetching before deployment.

Risk: LLM endpoint configuration and local credentials may be exposed or misused if unrestricted.

Mitigation: Restrict LLM endpoints to trusted HTTPS hosts, replace auth secrets and password storage, and keep credentials out of the runtime environment when they are not required.

Risk: The security evidence calls out undefined upload retention and unpinned dependencies.

Mitigation: Define upload retention behavior and pin dependencies before production installation.

Risk: Cloudflare bot or WAF changes can affect shared infrastructure.

Mitigation: Apply Cloudflare bot or WAF instructions only after explicit administrator approval.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/muchenhengxin/skills/star-search)
- [README](artifact/README.md)
- [MCP server implementation](artifact/mcp/mcp_server.py)
- [LangChain adapter](artifact/integrations/langchain/star_search_tool.py)
- [Dify integration guide](artifact/integrations/dify/README.md)
- [Search engine research](artifact/references/search-engine-research.md)
- [star-search vs baidu-search comparison](artifact/references/vs-baidu-search-comparison.md)
- [v16 engine addition checklist](artifact/references/v16-engine-addition-checklist.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON, shell command, and configuration snippets; tool calls return JSON search results and source-linked text answers.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May call external search, LLM, MCP/SSE, and integration endpoints depending on configuration.]

## Skill Version(s):

20.42.1 (source: server release evidence; artifact frontmatter reports 20.42.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
