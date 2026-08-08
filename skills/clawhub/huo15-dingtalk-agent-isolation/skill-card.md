## Description: <br>
Creates isolated OpenClaw agent workspaces, agent directories, memory, and conversation history for individual DingTalk users through manual bindings or optional dynamic agent creation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zhaobod1](https://clawhub.ai/user/zhaobod1) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and operators use this skill to configure DingTalk-backed OpenClaw deployments so individual users can be routed to separate agents, workspaces, memory, and conversation history. It supports known-user manual binding and an advanced dynamic mode for onboarding first-time direct-message users. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Dynamic mode can add persistent agents and bindings after first-time DingTalk direct messages. <br>
Mitigation: Prefer manual binding unless automatic onboarding is required, and set a strict maxAgents value before enabling dynamic creation. <br>
Risk: The skill asks users to patch DingTalk connector code and modify OpenClaw configuration. <br>
Mitigation: Review the patch before applying it, keep backups of ~/.openclaw/openclaw.json and connector files, and test changes in a staging environment first. <br>
Risk: Cleanup examples include destructive directory removal commands. <br>
Mitigation: Verify each resolved workspace and agent directory path before running removal commands. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zhaobod1/skills/huo15-dingtalk-agent-isolation) <br>
- [DingTalk dynamic agent patch reference](references/dynamic-agent-patch.ts) <br>
- [Feishu dynamic agent implementation reference](references/feishu-reference.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON configuration examples, TypeScript patch reference, and shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes manual binding guidance, dynamic agent patching guidance, configuration snippets, and verification commands.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
