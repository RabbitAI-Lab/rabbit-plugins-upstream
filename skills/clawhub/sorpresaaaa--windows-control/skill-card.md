## Description: <br>
Full Windows desktop control. Mouse, keyboard, screenshots - interact with any Windows application like a human. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[sorpresaaaa](https://clawhub.ai/user/sorpresaaaa) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and automation users can use this skill to let an agent inspect and operate Windows desktop applications through screenshots, keyboard input, mouse actions, window management, dialogs, and UI Automation text extraction. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad desktop control can click, type, close windows, handle dialogs, and save files in any reachable Windows application. <br>
Mitigation: Run only in a controlled desktop session and require explicit review before actions that submit, delete, overwrite, approve, close, or save. <br>
Risk: Screen reading and UI Automation can expose sensitive text, form values, browser content, and screenshots. <br>
Mitigation: Avoid using the skill with password managers, banking, email, admin consoles, private browser sessions, or other sensitive applications. <br>
Risk: Optional OCR-based region reading depends on Tesseract and pytesseract and may be unavailable or less reliable than UI Automation. <br>
Mitigation: Prefer UI Automation readers when available and verify OCR-derived text before acting on it. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/sorpresaaaa/skills/windows-control) <br>
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, JSON, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands; helper scripts return text, JSON, or base64 PNG screenshots.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs may include screen text, UI element coordinates, active window titles, dialog contents, command status messages, and screenshots.] <br>

## Skill Version(s): <br>
1.0.0 (source: package.json and ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
