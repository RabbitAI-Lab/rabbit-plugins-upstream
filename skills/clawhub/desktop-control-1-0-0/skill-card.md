## Description: <br>
Advanced desktop automation with mouse, keyboard, screen, window, and clipboard control for OpenClaw agents. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[wpegley](https://clawhub.ai/user/wpegley) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent builders use this skill to let an agent operate a live desktop through mouse movement, keyboard input, screenshots, image matching, window selection, and clipboard actions. It is intended for supervised desktop automation workflows where the agent needs to interact with local applications. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can control the live desktop and submit actions through logged-in applications. <br>
Mitigation: Use approval mode for sensitive workflows, keep the session supervised, and review actions that submit forms, change files, launch apps, or post through accounts. <br>
Risk: Screenshots and clipboard reads can expose private information visible on the desktop. <br>
Mitigation: Close private windows, avoid clipboard reads unless necessary, and limit screenshot capture to the regions needed for the task. <br>
Risk: Automation can move too quickly or target the wrong window or coordinates. <br>
Mitigation: Keep failsafe enabled, add pauses between UI actions, verify the active window before acting, and test workflows before using them on important data. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/wpegley/skills/desktop-control-1-0-0) <br>
- [Desktop Control Skill Documentation](artifact/SKILL.md) <br>
- [AI Desktop Agent Guide](artifact/AI_AGENT_GUIDE.md) <br>
- [Desktop Control Quick Reference](artifact/QUICK_REFERENCE.md) <br>


## Skill Output: <br>
**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance, Files] <br>
**Output Format:** [Markdown documentation with Python code examples and optional generated screenshot image files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Agent actions may control the active desktop, launch applications, type text, use hotkeys, read or write clipboard text, and save screenshots.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
