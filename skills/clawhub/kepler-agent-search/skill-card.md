## Description:

Routes agent search and page-reading tasks across Bing, Baidu, Zhihu, Xiaohongshu, GitHub, arXiv, 199it, Eastmoney, Zhaopin, and 51job through Kepler MCP tools.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mylike2018](https://clawhub.ai/user/mylike2018)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to retrieve current web information, read selected pages, and compare results across general search, Chinese social platforms, code, academic, data, finance, and hiring sources.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search queries and selected URLs are routed through an external Kepler MCP service at apisec.cn.

Mitigation: Review and accept the provider's privacy and security terms before use, especially for organizational deployments.

Risk: Sensitive prompts, secrets, credentials, confidential documents, customer data, or sensitive personal topics could be exposed through search or page-reading requests.

Mitigation: Do not use the skill with secrets, credentials, private customer data, confidential internal documents, or sensitive personal topics unless that data sharing has been approved.

## Reference(s):

- [Kepler MCP Service Setup Guide](references/mcp-setup.md)
- [Web Search and Code Search](references/search.md)
- [Social Media Search](references/social.md)
- [Open Source Code Search](references/github.md)
- [Academic Research Search](references/arxiv.md)
- [Industry Data and Report Search](references/data.md)
- [Finance and Stock Search](references/finance.md)
- [Recruiting and Job Search](references/career.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, API Calls, Configuration, Guidance]

**Output Format:** [Markdown with links, summaries, source labels, and optional JSON MCP configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Search behavior depends on the configured Kepler MCP service and selected source engine.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
