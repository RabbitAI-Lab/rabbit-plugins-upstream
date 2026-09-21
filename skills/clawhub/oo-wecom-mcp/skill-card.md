## Description:

WeCom MCP (work.weixin.qq.com) supports reading, creating, updating, and deleting WeCom MCP data through the OOMOL `wecom_mcp` connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to discover available WeCom MCP tools, inspect live input schemas, and run WeCom MCP actions through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path includes running a remote oo CLI installer script.

Mitigation: Review and verify the installer before running it, and install only if OOMOL is trusted.

Risk: The connected WeCom MCP account may expose actions that send, overwrite, cancel, or delete WeCom data.

Mitigation: Require explicit user confirmation for state-changing or destructive actions, including the target and exact payload.

## Reference(s):

- [WeCom MCP ClawHub listing](https://clawhub.ai/oomol/skills/oo-wecom-mcp)
- [WeCom MCP homepage](https://work.weixin.qq.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands may return JSON responses from the OOMOL connector.]

## Skill Version(s):

1.0.3 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
