## Description:

WeCom MCP (work.weixin.qq.com) helps an agent discover and invoke live WeCom MCP tools through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to let an agent inspect WeCom MCP tool schemas and run WeCom MCP actions through the OOMOL connector. It is suited for WeCom data lookup and carefully confirmed state-changing operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill exposes broad WeCom MCP tool execution, including tools that may send, overwrite, cancel, delete, or otherwise change business data.

Mitigation: Inspect the live tool schema before every invocation and require explicit user confirmation for any non-read, write, or destructive operation.

Risk: The security summary notes that parts of the instructions describe the skill as read-oriented while the generic connector action can reach write or destructive tools.

Mitigation: Treat live tool schemas and behavior annotations as authoritative, and do not assume an action is read-only unless its schema and annotations support that conclusion.

Risk: First-time setup includes pipe-to-shell installer commands.

Mitigation: Avoid running installer commands unless the user independently trusts and verifies the installer source.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-wecom-mcp)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [WeCom MCP homepage](https://work.weixin.qq.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses may include JSON data and execution metadata.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
