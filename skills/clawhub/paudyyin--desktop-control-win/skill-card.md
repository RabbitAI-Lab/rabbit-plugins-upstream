## Description: <br>
Control Windows desktop applications by launching, closing, focusing, resizing, and moving windows; simulating keyboard and mouse input; managing processes; controlling VSCode; reading clipboard text; and capturing screen information. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[paudyyin](https://clawhub.ai/user/paudyyin) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill when an agent needs to interact with a Windows desktop session, such as arranging windows, typing into focused applications, opening files in VSCode, inspecting running processes, or collecting display and clipboard state. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill grants broad control over windows, keyboard and mouse input, screenshots, clipboard text, processes, and VSCode extensions. <br>
Mitigation: Install only when an agent intentionally needs Windows desktop control, and require explicit user confirmation before screenshot, clipboard, input, process kill, window close, or VSCode extension changes. <br>
Risk: Screenshots and clipboard reads may expose passwords, tokens, private messages, or other sensitive information visible in the desktop session. <br>
Mitigation: Avoid using screenshot and clipboard actions when sensitive windows or clipboard contents may be present, and clear or hide sensitive material before running them. <br>
Risk: Keyboard and mouse simulation may affect the wrong application if focus is incorrect. <br>
Mitigation: Verify and focus the intended target window before sending input, clicks, shortcuts, or typed text. <br>
Risk: Closing windows or killing processes may cause data loss or interrupt user work. <br>
Mitigation: Confirm the exact window title, process name, or PID with the user before closing or killing anything that may contain unsaved work. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/paudyyin/skills/desktop-control-win) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, guidance] <br>
**Output Format:** [Markdown instructions with PowerShell command examples and plain-text command output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Windows 10/11 and PowerShell 5.1+ are required; VSCode is required only for VSCode-specific actions.] <br>

## Skill Version(s): <br>
1.0.0 (source: SKILL.md frontmatter, package.json, server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
