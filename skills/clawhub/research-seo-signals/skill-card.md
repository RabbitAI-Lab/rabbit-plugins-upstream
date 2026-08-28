## Description:

Retrieve traceable keyword, search result, trend, ranked-keyword, traffic-estimation, GEO, competitor, and backlink data for SEO research and analysis via SignalDig.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jerrykik](https://clawhub.ai/user/jerrykik)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to scope SEO research requests and retrieve evidence-backed keyword, SERP, trend, competitor, GEO, backlink, ranked-keyword, and traffic-estimation reports through the SignalDig MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: SEO research inputs are sent to the SignalDig MCP service after setup and scope selection.

Mitigation: Review each scoped request before submission and send only the smallest sufficient keyword, domain, market, language, and data-scope inputs.

Risk: The workflow requires a SignalDig API key for the MCP server.

Mitigation: Store the key in an environment variable or client secret store, keep tool approval prompted where supported, and do not commit the key to project files.

Risk: Unavailable tools, failed jobs, or partial results could lead to unsupported SEO claims.

Mitigation: Stop when the MCP tools are unavailable, report partial coverage explicitly, and cite only evidence returned by the live tool result.

## Reference(s):

- [Setup Guide: Connect the SignalDig SEO MCP Server](references/setup-guide.md)
- [SEO Research Functional Contract](references/mcp-contract.md)
- [SignalDig](https://signaldig.com/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown reports with evidence references and occasional inline configuration or shell snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Default output is concise; full exports are produced only when requested.]

## Skill Version(s):

1.8.0 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
