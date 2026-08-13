## Description:

Publishes prepared Xiaohongshu Markdown notes and images through a local xiaohongshu-mcp service, then checks the published note_id.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dqsjqian](https://clawhub.ai/user/dqsjqian)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators with prepared Xiaohongshu Markdown copy and image assets use this skill to log in, publish single or batch image-text notes through a trusted local xiaohongshu-mcp endpoint, and retrieve the resulting note_id.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Successful runs can publish public content to the user's Xiaohongshu account.

Mitigation: Review the Markdown text and image paths before publishing, especially when using batch directory mode.

Risk: The local xiaohongshu-mcp service can hold Xiaohongshu login cookies and act on the authenticated account.

Mitigation: Keep XHS_MCP_URL pointed at a trusted local endpoint and protect the local cookies path.

Risk: Batch publishing may post unintended Markdown files from the selected directory.

Mitigation: Run the login check first and inspect the target directory contents before starting batch publication.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dqsjqian/skills/xhs-publisher)
- [xiaohongshu-mcp repository](https://github.com/xpzouying/xiaohongshu-mcp)
- [xiaohongshu-mcp v2.4.3 Darwin ARM64 release asset](https://github.com/xpzouying/xiaohongshu-mcp/releases/download/v2.4.3/xiaohongshu-mcp-darwin-arm64)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown instructions and terminal output from the publishing script, including NOTE_ID when publication succeeds]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires prepared Markdown content, local image paths, a trusted XHS_MCP_URL endpoint, and an authenticated Xiaohongshu session.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
