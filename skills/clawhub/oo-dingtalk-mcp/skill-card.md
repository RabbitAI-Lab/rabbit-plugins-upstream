## Description:

DingTalk MCP helps an agent discover DingTalk MCP tools and run DingTalk connector actions through the OOMOL `oo` CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to let an agent inspect the live DingTalk MCP tool contract, prepare JSON payloads, and run read or confirmed write actions through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The generic DingTalk MCP action path can expose tools that send, overwrite, cancel, or delete DingTalk data.

Mitigation: Inspect the live schema first and require explicit user confirmation for every non-read or destructive operation, including the exact payload and expected effect.

Risk: First-time setup includes remote installer one-liners for the `oo` CLI.

Mitigation: Use managed installation where possible, or independently verify the installer source and scope before running remote installation commands.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-dingtalk-mcp)
- [DingTalk MCP homepage](https://www.dingtalk.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are JSON objects with data and execution metadata when actions are run.]

## Skill Version(s):

1.0.0 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
