## Description: <br>
Phone Agent connects OpenClaw or Qoder to a local MCP bridge so an agent can run Mobile AI Agent tasks on a connected Android phone, including screenshots, device status checks, task execution, and task control. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mobileaiuse](https://clawhub.ai/user/mobileaiuse) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and automation users use this skill to connect an agent workflow to Mobile AI Agent and operate a USB-connected Android phone through natural-language tasks, screenshots, device status checks, and task result queries. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can let an agent operate a connected phone and view screenshots, which may expose sensitive messages, accounts, payments, authentication codes, or other private data. <br>
Mitigation: Keep the MCP bridge disconnected except when needed, review tasks before execution, and avoid using the skill on sensitive screens or apps. <br>
Risk: A broad phone automation task may perform unintended actions on the connected device. <br>
Mitigation: Use narrow task goals, monitor execution, and use the abort tool when behavior does not match the intended task. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/mobileaiuse/skills/phone-agent) <br>
- [Server-resolved GitHub source](https://github.com/MobileAiUse/skills/tree/main/phone-agent) <br>
- [Mobile AI Agent](https://mobile-ai-use.com/mobileAi) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance, images] <br>
**Output Format:** [Markdown guidance with bash and JSON configuration examples; MCP tool outputs may include text status, task results, and PNG screenshots.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The skill exposes MCP tools for running and aborting phone automation tasks, taking screenshots, checking device status, and retrieving task results.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
