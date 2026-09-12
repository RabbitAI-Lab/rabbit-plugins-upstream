## Description:

A cross-platform agent skill for reading, pushing, syncing, exporting, and managing DingTalk cloud documents through the official DingTalk Document MCP Server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cpsean](https://clawhub.ai/user/cpsean)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and knowledge workers use this skill to operate DingTalk knowledge-base documents from an MCP-capable agent, including document creation, synchronization, export, search, file upload/download, and permission management.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The DingTalk MCP URL can contain a personal API key and may be stored in persistent agent configuration.

Mitigation: Review the exact MCP configuration before approving setup; prefer project-local configuration only when the secret-bearing file is ignored by Git, or use a user-level secret mechanism with restrictive permissions. Rotate the URL if it is ever committed, logged, or shared.

Risk: Write, delete, export, upload, download, and permission actions operate on real DingTalk cloud data.

Mitigation: Approve only specific intended changes, require explicit confirmation for cloud writes and management actions, and communicate data flow and consequences before execution.

Risk: Uploads move local file bytes to DingTalk cloud storage, while exports and downloads can create portable copies or temporary signed links.

Mitigation: Disclose the destination or copy/share risk before transfer, use DingTalk-issued upload URLs only, and remind users that exported files and signed links can be further shared.

Risk: Reading cloud document content brings potentially sensitive DingTalk data into the current agent context.

Mitigation: Read only the documents needed for the current task, confirm ambiguous targets before fetching content, and avoid writing fetched content to unrelated files.

## Reference(s):

- [DingTalk Document MCP Server](https://aihub.dingtalk.com/#/detail?mcpId=9629&detailType=marketMcpDetail)
- [DingTalk Docs](https://alidocs.dingtalk.com)
- [DingTalk Developer Getting Started](https://open.dingtalk.com/document/dingstart/dingtalk-developer)
- [MCP tool reference](references/mcp-tools.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown responses with inline shell commands, JSON configuration snippets, and operation guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce DingTalk document links, local files, downloaded or exported files, and MCP setup instructions after user confirmation.]

## Skill Version(s):

1.0.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
