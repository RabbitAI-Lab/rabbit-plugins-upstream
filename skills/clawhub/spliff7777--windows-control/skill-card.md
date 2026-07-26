## Description: <br>
Full Windows desktop control. Mouse, keyboard, screenshots - interact with any Windows application like a human. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[spliff7777](https://clawhub.ai/user/spliff7777) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and automation users can use this skill to let an agent inspect and control a Windows desktop through mouse, keyboard, screenshot, window, UI element, browser, and dialog actions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can read and change arbitrary Windows applications, browser pages, dialogs, and screenshots. <br>
Mitigation: Install only for sessions where broad desktop control is intended, keep sensitive apps and secrets closed, and treat captured UI text and screenshots as sensitive. <br>
Risk: Click, type, dismiss, close, and dialog actions can modify local desktop state. <br>
Mitigation: Prefer exact window targeting and review proposed click, type, dismiss, and close actions before execution. <br>
Risk: Screenshots and UI extraction can expose confidential data from visible windows. <br>
Mitigation: Use the skill in a bounded session and avoid running it where confidential data may appear on screen. <br>


## Reference(s): <br>
- [ClawHub Windows Control skill page](https://clawhub.ai/spliff7777/skills/windows-control) <br>
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Text, JSON, Files, Guidance] <br>
**Output Format:** [Markdown guidance with Windows shell commands; command results may be plain text, JSON, or base64 PNG.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Runs local Python scripts that can inspect and control visible Windows desktop state.] <br>

## Skill Version(s): <br>
1.0.0 (source: package.json and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
