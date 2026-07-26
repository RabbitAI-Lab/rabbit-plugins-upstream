## Description: <br>
Windows desktop control skill for screenshots, window management, mouse and keyboard control, process management, system information, OCR, UI Automation, and local agent-driven desktop workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[sunsettide](https://clawhub.ai/user/sunsettide) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agent users use this skill to let an authorized OpenClaw agent operate a local Windows desktop through mouse, keyboard, screenshots, OCR, UI Automation, window management, scripting, and function-calling tools. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can control mouse and keyboard input, inspect screen/OCR/UIA content, use the clipboard, and optionally record or replay global input. <br>
Mitigation: Install and run it only on authorized local Windows desktops, keep user confirmation enabled for sensitive workflows, review generated scripts before execution, and shut down the daemon when desktop control is not needed. <br>
Risk: The security scan says local-only privacy claims conflict with code that can send prompts to remote LLM services. <br>
Mitigation: Keep LLM_API_KEY and LLM_BASE_URL unset unless remote LLM use is intentional, and avoid helper scripts that download resources when validating offline operation. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/sunsettide/skills/desktop-control) <br>
- [Project homepage](https://github.com/sunsettide/desktop-control) <br>
- [README](README.md) <br>
- [Security policy](SECURITY.md) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, JSON, Files, Guidance] <br>
**Output Format:** [Command-line invocations with JSON parameters and JSON or file outputs such as screenshots] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Runs on Windows 10/11 with Python 3.9+ and local desktop access.] <br>

## Skill Version(s): <br>
1.1.3 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
