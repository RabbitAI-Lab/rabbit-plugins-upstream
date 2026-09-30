## Description:

Operates named supported creative applications through DCC-MCP, discovers available tools and marketplace skills, and verifies resulting work.

This skill is ready for commercial/non-commercial use.

## Publisher:

[loonghao](https://clawhub.ai/user/loonghao)

### License/Terms of Use:

MIT-0

## Use Case:

Artists, developers, and production teams use this skill to discover application tools, create or edit creative projects in supported software, and check the resulting scene, document, or artifact.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Live application control and project edits can change or overwrite user work.

Mitigation: Confirm the intended target and review authorization prompts before launches or edits; verify resulting state after each operation.

Risk: Marketplace actions or software installation can introduce unwanted packages or executables.

Mitigation: Review and approve installs and updates, including the exact package or release, before proceeding.

Risk: Remote gateway use can expose project data to an unintended destination.

Mitigation: Approve the remote gateway origin explicitly, share only necessary project data, and never include credentials in tool payloads.

Risk: Cached application paths may point to an unintended program when a launch is requested.

Mitigation: Review the saved path and obtain explicit confirmation before starting the application.

## Reference(s):

- [ClawHub DCC-MCP release](https://clawhub.ai/loonghao/skills/dcc-mcp)
- [Skill homepage (release metadata)](https://github.com/dcc-mcp/dcc-mcp-agent-plugins/blob/main/plugins/dcc-mcp/skills/dcc-mcp/SKILL.md)
- [Supported products](artifact/references/PRODUCTS.json)
- [Tool execution and verification](artifact/references/TOOL_EXECUTION.md)
- [Application UI workflows](artifact/references/UI_WORKFLOWS.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Files]

**Output Format:** [Markdown guidance and application project artifacts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports observed application results after post-action verification.]

## Skill Version(s):

0.19.107 (source: skill metadata and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
