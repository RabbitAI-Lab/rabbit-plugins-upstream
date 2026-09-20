## Description:

DingTalk MCP (dingtalk.com). Use this skill for ANY DingTalk MCP request: reading, creating, updating, and deleting data through the OOMOL-connected DingTalk MCP connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to discover DingTalk MCP tools and run DingTalk actions through an OOMOL-connected account. It supports read, write, and potentially destructive DingTalk operations when the current connector exposes those tools.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can operate a connected DingTalk account and may expose tools that change, overwrite, cancel, or delete DingTalk data.

Mitigation: Review the live tool schema and require explicit user confirmation for write or destructive operations before execution.

Risk: First-time setup includes shell-based installation paths for the oo CLI.

Mitigation: Use a verified package or reviewed installer when possible, and install only when the CLI is missing.

Risk: The skill depends on OOMOL-managed account connection and credential injection.

Mitigation: Install only when the user trusts OOMOL and intends to grant access to the connected DingTalk account.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-dingtalk-mcp)
- [DingTalk homepage](https://www.dingtalk.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing DingTalk MCP payloads.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
