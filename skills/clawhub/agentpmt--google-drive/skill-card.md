## Description:

Google Drive file management for searching, uploading, downloading, organizing, moving or copying, sharing, and exporting files through AgentPMT-hosted remote tool calls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[agentpmt](https://clawhub.ai/user/agentpmt)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to let an agent manage Google Drive files and folders, including search, upload, download, organization, sharing, and Google Workspace export workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can trash or permanently delete Google Drive files and folders, including shared-drive content.

Mitigation: Require explicit user confirmation before trash or permanent delete actions and verify the target file or folder ID.

Risk: The skill can create user, group, domain, or anyone sharing permissions.

Mitigation: Require explicit confirmation for public or domain sharing and review the requested permission role before execution.

Risk: The skill can download potentially sensitive Drive files into temporary storage.

Mitigation: Confirm sensitive downloads with the user, keep download size limits scoped, and rely on the documented temporary expiration behavior.

Risk: Unpinned setup commands can change behavior over time.

Mitigation: Prefer ClawHub setup routes or pinned install commands when installing related AgentPMT skills.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/agentpmt/skills/google-drive)
- [AgentPMT marketplace page](https://www.agentpmt.com/marketplace/google-drive)
- [Generated action schema](artifact/schema.md)
- [Related File Management skill](https://clawhub.ai/agentpmt/file-management)
- [AgentPMT account MCP/REST setup](https://clawhub.ai/agentpmt/agentpmt-account-mcp-rest-api-setup)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration, API calls]

**Output Format:** [Markdown instructions with JSON request examples and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Covers 12 Google Drive actions and emphasizes schema lookup when live details are needed.]

## Skill Version(s):

1.0.0 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
