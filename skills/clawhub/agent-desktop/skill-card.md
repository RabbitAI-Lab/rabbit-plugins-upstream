## Description: <br>
Desktop automation via native OS accessibility trees using the agent-desktop CLI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[lahfir](https://clawhub.ai/user/lahfir) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent builders use this skill to let an AI agent observe, interact with, and automate desktop applications through the agent-desktop CLI. It is suited for GUI tasks such as reading UI state, clicking controls, filling forms, managing windows, working with notifications, using the clipboard, and taking screenshots. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill enables an agent to operate the user's desktop through Accessibility permissions. <br>
Mitigation: Install only when desktop operation is intended and grant Accessibility permissions only to trusted launchers. <br>
Risk: Screenshots and clipboard reads can expose sensitive on-screen or copied content. <br>
Mitigation: Avoid screenshots and clipboard reads around sensitive content unless they are necessary for the task. <br>
Risk: Local automation traces and replay artifacts may retain sensitive session details. <br>
Mitigation: Use --no-trace or session gc when traces should not be retained, and opt into screenshot replay artifacts only when their sensitivity is acceptable. <br>


## Reference(s): <br>
- [agent-desktop ClawHub Skill Page](https://clawhub.ai/lahfir/skills/agent-desktop) <br>
- [Observation Commands](references/commands-observation.md) <br>
- [Interaction Commands](references/commands-interaction.md) <br>
- [System Commands](references/commands-system.md) <br>
- [Common Automation Workflows](references/workflows.md) <br>
- [macOS Platform](references/macos.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guidance is oriented around invoking a desktop automation CLI that returns structured JSON envelopes.] <br>

## Skill Version(s): <br>
0.1.22 (source: release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
