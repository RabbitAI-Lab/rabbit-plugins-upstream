## Description:

WeCom MCP helps agents search, read, and operate an OOMOL-connected WeCom MCP account through the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to discover current WeCom MCP tools, inspect live schemas, and run read or approved write/destructive WeCom actions through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access an OOMOL-connected WeCom MCP account and may expose tools that send, overwrite, cancel, or delete WeCom data.

Mitigation: Review live tool schemas before approving write or destructive actions, confirm the exact payload and intended effect with the user, and require explicit approval for destructive targets.

Risk: Setup commands and login steps configure the oo CLI and connect the user's OOMOL account.

Mitigation: Run install, login, or connection steps only when the connector fails for the matching setup reason and only if the user trusts OOMOL and needs the connector configured.

Risk: Credentials are handled server-side by OOMOL, so account access depends on the user's connected OOMOL environment.

Mitigation: Install the skill only when the user intends Codex to use their OOMOL-connected WeCom MCP account.

## Reference(s):

- [WeCom MCP homepage](https://work.weixin.qq.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-wecom-mcp)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, API Calls, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill directs agents to fetch live connector schemas before constructing payloads and to request confirmation for write or destructive actions.]

## Skill Version(s):

1.0.0 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
