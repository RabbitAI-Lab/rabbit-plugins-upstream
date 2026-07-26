## Description: <br>
Control desktop applications on Windows by launching and focusing apps, managing windows and processes, simulating keyboard or mouse input, controlling VSCode, reading clipboard content, and capturing screen information. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[eohmig](https://clawhub.ai/user/eohmig) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, support engineers, and automation agents use this skill to operate Windows desktop applications during interactive workflows: arranging windows, typing or clicking, controlling VSCode, inspecting processes, capturing screen state, and handling clipboard text. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Input simulation, window focus, and mouse actions may affect the wrong application or account if the target window is not active. <br>
Mitigation: Confirm the intended window is focused before sending text, shortcuts, clicks, or scroll actions. <br>
Risk: Closing windows, killing processes, or uninstalling VSCode extensions can interrupt work or discard unsaved changes. <br>
Mitigation: Ask for explicit confirmation before destructive actions and prefer graceful close or user-approved process termination. <br>
Risk: Clipboard and screenshot actions can expose sensitive content or overwrite user clipboard state. <br>
Mitigation: Warn before overwriting clipboard content and avoid capturing or sharing sensitive screen or clipboard data unless the user explicitly requests it. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/eohmig/skills/desktop-control-win) <br>


## Skill Output: <br>
**Output Type(s):** [text, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline PowerShell commands; scripts return console text and may create screenshot files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Designed for an interactive Windows desktop session with PowerShell and the relevant target applications available.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
