## Description:

WeCom MCP helps agents discover live WeCom MCP tools and invoke them through an OOMOL-connected account using the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external operators use this skill to route WeCom MCP requests through an OOMOL-connected account, inspect live tool schemas, and run approved read or write actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can invoke WeCom MCP tools that may perform write or destructive actions.

Mitigation: Require explicit user approval before call_tool unless the discovered live tool is verified read-only.

Risk: The skill recommends remote installer commands for the oo CLI.

Mitigation: Install the oo CLI through a trusted, versioned, and verified method before use.

Risk: A connected WeCom account may expose actions beyond searching and reading data.

Mitigation: Use a WeCom connection scoped to actions the agent is allowed to perform for a human operator.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-wecom-mcp)
- [WeCom MCP Homepage](https://work.weixin.qq.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing payloads.]

## Skill Version(s):

1.0.2 (source: evidence release and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
