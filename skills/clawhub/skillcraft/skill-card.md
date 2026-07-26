## Description: <br>
Design and build OpenClaw skills. Use when asked to "make/build/craft a skill", extract ad-hoc functionality into a skill, or package scripts/instructions for reuse. Covers OpenClaw-specific integration (tool calling, memory, message routing, cron, canvas, nodes) and ClawHub publishing. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jmz1](https://clawhub.ai/user/jmz1) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and skill authors use Skillcraft to design, package, and publish OpenClaw skills, including skills that wrap CLIs, web APIs, monitors, scheduled workflows, and reusable instructions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated skill designs can include local command execution, scheduled jobs, browser-authenticated sessions, API tokens, persistent memory, or background subagents. <br>
Mitigation: Review proposed skills before installation or publication; require explicit approval, least-privilege credentials, dry runs, and logs for higher-risk behaviors. <br>
Risk: Skill-building guidance can introduce incorrect or misleading instructions into reusable skills. <br>
Mitigation: Test generated skills against representative examples and run security review or scanning before deployment. <br>


## Reference(s): <br>
- [Skillcraft ClawHub page](https://clawhub.ai/jmz1/skills/skillcraft) <br>
- [OpenClaw Skills documentation](https://docs.openclaw.ai/tools/skills) <br>
- [OpenClaw Creating Skills documentation](https://docs.openclaw.ai/tools/creating-skills) <br>
- [AgentSkills specification](https://agentskills.io) <br>
- [patterns/api-wrapper.md](patterns/api-wrapper.md) <br>
- [patterns/cli-wrapper.md](patterns/cli-wrapper.md) <br>
- [patterns/composable-examples.md](patterns/composable-examples.md) <br>
- [patterns/monitor.md](patterns/monitor.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with code, shell command, and configuration examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose skill file structures, OpenClaw integration choices, state locations, and review checklists.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
