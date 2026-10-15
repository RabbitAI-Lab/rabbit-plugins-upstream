## Description:

Searches and extracts Xiaohongshu notes, user pages, comments, popularity metrics, and content details through a locally running xiaohongshu-mcp service.

This skill is for research and development only.

## Publisher:

[neargg](https://clawhub.ai/user/neargg)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to search Xiaohongshu content, inspect note metadata, retrieve content details, and generate analysis from a logged-in local account session. The skill documentation limits use to personal research and learning and warns against commercial data collection, bulk scraping, or actions that violate Xiaohongshu platform terms.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on an unaudited third-party binary tied to a logged-in Xiaohongshu account.

Mitigation: Pin and verify the downloaded binary before use, run it only when needed, and keep it bound to 127.0.0.1.

Risk: The underlying service exposes tools that can like, favorite, or publish content from the logged-in account.

Mitigation: Require explicit user confirmation before any write action and avoid launchd or systemd autostart for the service.

Risk: The documentation warns against commercial data collection, bulk content scraping, or violating Xiaohongshu platform terms.

Mitigation: Limit use to personal research and learning, keep searches narrow, and review platform terms before collecting or reusing content.

## Reference(s):

- [xiaohongshu-mcp](https://github.com/xpzouying/xiaohongshu-mcp)
- [xiaohongshu-mcp release download](https://github.com/xpzouying/xiaohongshu-mcp/releases/latest/download/xiaohongshu-mcp-darwin-amd64.tar.gz)
- [ClawHub skill page](https://clawhub.ai/neargg/skills/xhs-search)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown, Python snippets, shell commands, and JSON-like search result data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Search output may include Xiaohongshu note IDs, titles, author names, engagement counts, comments metadata, and xsecToken values returned by the local MCP service.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
