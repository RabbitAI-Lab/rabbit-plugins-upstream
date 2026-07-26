## Description: <br>
桌面自动驾驶为 AI Agent 提供基于视觉的 GUI 自动化 guidance, covering image and OCR-based element location, intelligent waits, workflow orchestration, recording and playback, DPI adaptation, multi-monitor support, and safety controls. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to guide agents through local desktop GUI automation tasks such as form filling, data entry, cross-application data movement, UI regression testing, and repeatable workflow playback. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad GUI control can click, type, copy, paste, and move data in visible applications. <br>
Mitigation: Enable approval and failsafe modes, scope workflows to known applications, and review proposed actions before execution. <br>
Risk: Screenshots, OCR output, recordings, and operation logs may capture credentials, private documents, customer data, or financial information shown on screen. <br>
Mitigation: Close or hide sensitive material before use, avoid running the skill on sensitive systems, and review local recordings and logs before retaining or sharing them. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/desktop-autopilot) <br>
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Code, Shell commands, Configuration instructions, Guidance] <br>
**Output Format:** [Markdown with Python and shell code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include local desktop automation workflows, dependency installation commands, and safety-mode guidance.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
