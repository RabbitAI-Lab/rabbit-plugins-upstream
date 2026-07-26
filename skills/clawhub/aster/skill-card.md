## Description: <br>
Your AI CoPilot on Mobile - or give your AI its own phone. Make calls, send SMS, speak via TTS on speakerphone, automate UI, manage files, search media, and 40+ more tools via MCP. Open source, self-hosted, privacy-first. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[satyajiit](https://clawhub.ai/user/satyajiit) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and external users use this skill to let an AI agent operate an Android device through Aster's MCP tools for calls, SMS, UI automation, files, media search, notifications, location, clipboard, and device events. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill gives an AI agent broad control over Android phone capabilities, including SMS, calls, files, shell, location, clipboard, and event forwarding. <br>
Mitigation: Install only when deliberate Android device control is needed, prefer a spare phone, grant only necessary Android permissions, and review actions before execution. <br>
Risk: Callback and event-forwarding behavior can cause the agent to react to incoming messages or notifications. <br>
Mitigation: Keep callbacks disabled unless needed, use trusted authenticated callback endpoints, and require explicit confirmation for actions triggered by incoming messages or notifications. <br>
Risk: High-impact operations such as SMS, calls, file deletion, shell commands, UI automation, and device approval can affect the user's device or contacts. <br>
Mitigation: Require explicit confirmation for SMS, calls, file deletion, shell commands, UI automation, and device approval. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/satyajiit/skills/aster) <br>
- [Aster Website](https://aster.theappstack.in) <br>
- [Aster GitHub Repository](https://github.com/satyajiit/aster-mcp) <br>
- [Aster Releases](https://github.com/satyajiit/aster-mcp/releases) <br>
- [Tailscale](https://tailscale.com) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, Tool calls, Text] <br>
**Output Format:** [Markdown with inline shell commands, JSON configuration, and MCP tool names] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces instructions for installing, configuring, and using Aster with an Android device and local MCP server.] <br>

## Skill Version(s): <br>
0.1.14 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
