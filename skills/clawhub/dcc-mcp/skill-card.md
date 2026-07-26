## Description: <br>
DCC-MCP helps agents connect to and operate live DCC applications through structured DCC-MCP tools, with CLI-first marketplace discovery and setup guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[loonghao](https://clawhub.ai/user/loonghao) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, technical artists, and agent operators use this skill to route DCC control requests to live Maya, Blender, Houdini, Photoshop, 3ds Max, Nuke, Unreal, Godot, RenderDoc, Substance 3D, and related DCC tooling. It also guides marketplace search, package inspection, consent-gated installs or updates, and gateway troubleshooting. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can guide agents to control live DCC applications and change active creative sessions. <br>
Mitigation: Use the skill only when DCC-MCP control is intended, inspect tool schemas before calls, prefer structured tools, and verify results after actions. <br>
Risk: CLI installs, marketplace installs or updates, adapter setup, remote gateway profiles, and daemon actions can change local tools or installed skills. <br>
Mitigation: Require explicit user consent before these actions and follow the artifact's consent-gated setup and marketplace inspection steps. <br>
Risk: A missing CLI may trigger a binary installation path. <br>
Mitigation: Use only the documented verified installer path, which checks the official release manifest and SHA-256 digest and fails closed on mismatch. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/loonghao/skills/dcc-mcp) <br>
- [Clawdis Homepage](https://github.com/dcc-mcp/dcc-mcp-core/blob/main/skills/dcc-mcp/SKILL.md) <br>
- [CLI Cheatsheet](references/CLI_CHEATSHEET.md) <br>
- [Zero Instances CLI Setup Guide](references/ZERO_INSTANCES_CLI.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance, JSON] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON command results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs may include consent-gated setup steps, CLI command sequences, gateway profile guidance, DCC tool-call arguments, and bounded troubleshooting summaries.] <br>

## Skill Version(s): <br>
0.19.79 (source: frontmatter metadata and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
