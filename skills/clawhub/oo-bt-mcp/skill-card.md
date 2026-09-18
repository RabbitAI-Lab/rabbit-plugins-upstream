## Description:

BT Panel MCP (bt.cn) lets an agent inspect available BT Panel MCP tools and run selected actions through an OOMOL-connected account using the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to discover BT Panel MCP tools, inspect live schemas, and invoke BT Panel actions through the OOMOL connector. It is intended for agent-assisted server-management workflows where payloads and effects are reviewed before execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad administrative tool invocation against a BT Panel MCP connection can have state-changing or destructive effects.

Mitigation: Review each discovered tool and exact JSON payload before approval, and require explicit confirmation for write, destructive, or dangerous operations.

Risk: Unverified remote installer commands can execute external scripts.

Mitigation: Avoid using the pipe-to-shell installer unless it is independently trusted and verified; prefer pinned or signed oo CLI installation steps.

## Reference(s):

- [BT Panel MCP homepage](https://www.bt.cn/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-bt-mcp)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return JSON-formatted connector responses containing data and an execution ID.]

## Skill Version(s):

1.0.2 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
