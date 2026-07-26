## Description: <br>
Advanced desktop automation with mouse, keyboard, screen capture, window management, clipboard access, and simple autonomous desktop task execution. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[matagul](https://clawhub.ai/user/matagul) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent users use this skill to let an agent operate a local desktop through mouse movement, clicks, keyboard input, screenshots, window activation, clipboard operations, and rule-based task automation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill gives an agent broad control over the live desktop, including clicks, typing, hotkeys, application launches, and window actions. <br>
Mitigation: Install it only when desktop control is intended, keep failsafe enabled, use approval mode where possible, and review autonomous actions before form submissions, public posts, file changes, or app launches. <br>
Risk: Screenshots and clipboard access can expose passwords, private messages, financial data, or confidential documents. <br>
Mitigation: Avoid running the skill with sensitive content visible, avoid using it around passwords or confidential data, and review any saved screenshots before sharing or retaining them. <br>
Risk: The scan verdict is suspicious because the skill has powerful desktop automation behavior with limited default safeguards. <br>
Mitigation: Keep human review in the loop for high-impact actions and disable autonomous workflows when the environment contains sensitive data or irreversible operations. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/matagul/skills/desktop-control) <br>
- [AI Agent Guide](AI_AGENT_GUIDE.md) <br>
- [Quick Reference](QUICK_REFERENCE.md) <br>


## Skill Output: <br>
**Output Type(s):** [Code, Shell commands, Configuration, Guidance, Files] <br>
**Output Format:** [Markdown documentation with Python examples, shell commands, configuration snippets, and optional screenshot image files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May return Python result dictionaries for autonomous tasks and may save screenshots to user-specified paths.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
