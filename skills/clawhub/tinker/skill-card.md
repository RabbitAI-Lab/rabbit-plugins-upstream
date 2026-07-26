## Description: <br>
Tinker desktop toolbox CLI for AI agents that helps open Tinker plugins, list installed or running plugins, control plugin windows from the command line, call plugin MCP tools, and integrate Tinker with an AI agent via MCP. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[surunzi](https://clawhub.ai/user/surunzi) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and AI-agent users use this skill to control the Tinker desktop app and its plugins through the `tinker` CLI, including opening plugins, listing active plugin windows, and routing MCP-oriented plugin workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may launch Tinker and let an agent operate installed Tinker plugins through the local CLI. <br>
Mitigation: Install it only when you trust the Tinker desktop app and review the capabilities of installed plugins before allowing sensitive actions. <br>
Risk: The CLI depends on a local Tinker installation and command-line setup. <br>
Mitigation: Verify Tinker is installed, running, and reachable with `tinker ps` before relying on skill-driven automation. <br>


## Reference(s): <br>
- [Tinker skill release](https://clawhub.ai/surunzi/skills/tinker) <br>
- [Tinker desktop app](https://tinker.liriliri.io/) <br>
- [Publisher profile](https://clawhub.ai/user/surunzi) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration] <br>
**Output Format:** [Markdown with inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands target the local `tinker` CLI and may depend on installed Tinker plugins.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
