## Description:

Guides an MCP-capable agent through reading, creating, updating, exporting, and managing DingTalk Docs via the configured dingtalk-doc MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cpsean](https://clawhub.ai/user/cpsean)

### License/Terms of Use:

MIT

## Use Case:

Developers, knowledge workers, and agent users use this skill to synchronize local Markdown with DingTalk knowledge bases, search and retrieve cloud documents, export files, and manage document nodes or permissions through DingTalk Docs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup can persistently modify agent MCP configuration with an API-key-bearing DingTalk MCP URL.

Mitigation: Review the target config file and MCP URL before they are written, avoid repeating the full URL after setup, and install only when DingTalk document access is acceptable.

Risk: The configured MCP server can access enterprise documents and support exports, downloads, uploads, permission changes, and document deletion.

Mitigation: Confirm write, export, delete, upload, and permission operations before execution, and use the least DingTalk workspace access needed for the task.

Risk: Non-ASCII content uploaded through chat may be corrupted before it is pushed to DingTalk.

Mitigation: Prefer local file paths for Markdown files containing Chinese, Japanese, or other non-ASCII text, and check uploaded text for corruption before creating or updating documents.

## Reference(s):

- [Server-resolved GitHub source](https://github.com/CPsean/dingtalk-docs-skill)
- [ClawHub skill page](https://clawhub.ai/cpsean/skills/dingtalk-docs-skill)
- [DingTalk AI Hub MCP page](https://aihub.dingtalk.com/#/detail?mcpId=9629&detailType=marketMcpDetail)
- [DingTalk Docs](https://alidocs.dingtalk.com)
- [DingTalk developer getting started](https://open.dingtalk.com/document/dingstart/dingtalk-developer)
- [MCP tools reference](references/mcp-tools.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown or plain text guidance with optional shell commands and MCP tool-use instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide MCP calls that read, write, export, delete, upload, or change permissions on DingTalk documents after required user confirmation.]

## Skill Version(s):

1.0.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
