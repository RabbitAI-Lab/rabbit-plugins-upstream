## Description: <br>
AI remote control for Windows desktop. Captures screen on-demand via POST request and provides an HTTP API for mouse/keyboard actions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[haidiantoutou](https://clawhub.ai/user/haidiantoutou) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and desktop automation users use Wincontrol to let an agent capture the local Windows desktop and send localhost HTTP requests for mouse and keyboard actions during trusted local workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Any local caller can use the running HTTP API to capture the screen and control mouse or keyboard actions. <br>
Mitigation: Run the server only on a trusted single-user machine, keep it bound to localhost, and stop it when desktop automation is not actively needed. <br>
Risk: The generated screenshot.jpg may contain sensitive information such as passwords, messages, or private documents. <br>
Mitigation: Treat screenshot.jpg as sensitive local data, avoid running the skill while sensitive content is visible, and rely on server shutdown cleanup after use. <br>
Risk: Exposing port 8767 beyond localhost would allow unintended desktop-control access. <br>
Mitigation: Do not expose port 8767 to a network and review local firewall or tunneling configuration before starting the server. <br>


## Reference(s): <br>
- [Wincontrol ClawHub page](https://clawhub.ai/haidiantoutou/skills/wincontrol) <br>
- [SKILL.md](SKILL.md) <br>
- [README.md](README.md) <br>
- [Declared project homepage](https://github.com/QQSHI13/nova-workspace/tree/main/skills/wincontrol) <br>
- [pywin32 releases](https://github.com/mhammond/pywin32/releases) <br>


## Skill Output: <br>
**Output Type(s):** [API Calls, Shell commands, Files, Configuration instructions, Guidance] <br>
**Output Format:** [Markdown instructions, shell commands, JSON HTTP responses, and screenshot JPEG file paths] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes and overwrites screenshot.jpg in the skill directory; the local server listens on localhost port 8767 while running.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release metadata; artifact declares 2.0.1 in CHANGELOG.md and skill.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
