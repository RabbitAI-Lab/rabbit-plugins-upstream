## Description: <br>
Desktop Control helps agents automate desktop tasks through mouse, keyboard, screen, window, and clipboard operations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and automation-focused users use this skill to ask an agent to operate desktop applications, capture screen state, manage windows, and automate repetitive local workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad desktop control can expose visible windows, clipboard contents, private documents, credentials, and other sensitive local state. <br>
Mitigation: Use only when desktop automation is intentional; close sensitive windows and avoid exposing passwords, private documents, or sensitive clipboard data before enabling the skill. <br>
Risk: Mouse and keyboard automation can perform unintended actions in focused applications or privileged windows. <br>
Mitigation: Keep failsafe and approval mode enabled, avoid administrator privileges unless necessary, and review high-impact actions before execution. <br>
Risk: Weak scoping may allow automation beyond the originally intended task. <br>
Mitigation: Limit use to clearly bounded workflows and stop the session when the required desktop task is complete. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/desktop-control) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, code, shell commands, configuration] <br>
**Output Format:** [Markdown instructions with Python and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May require local desktop permissions and PyAutoGUI, Pillow, OpenCV, and PyGetWindow dependencies.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
