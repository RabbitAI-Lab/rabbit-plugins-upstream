## Description: <br>
Advanced desktop automation with mouse, keyboard, and screen control. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[eohmig](https://clawhub.ai/user/eohmig) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and automation users use this skill to let an agent operate desktop applications through mouse, keyboard, screen, window, and clipboard actions. It is suited to controlled desktop workflows such as app launching, text entry, screenshots, drawing, and form-style automation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill gives an agent broad control over the user's desktop, including typing, clicking, screenshots, app launches, window activation, and clipboard reads. <br>
Mitigation: Install only when desktop control is intentional, keep failsafe enabled, avoid use near passwords or private documents, and review autonomous task plans before allowing actions. <br>
Risk: Default consent boundaries are weak because approval mode is optional and disabled by default in the controller implementation. <br>
Mitigation: Prefer require_approval=True for sensitive workflows and require explicit confirmation before typing, clicking, clipboard access, screenshots, or public posting workflows. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/eohmig/skills/desktop-control) <br>
- [SKILL.md](artifact/SKILL.md) <br>
- [AI_AGENT_GUIDE.md](artifact/AI_AGENT_GUIDE.md) <br>
- [QUICK_REFERENCE.md](artifact/QUICK_REFERENCE.md) <br>


## Skill Output: <br>
**Output Type(s):** [Code, Shell commands, Guidance, Configuration] <br>
**Output Format:** [Markdown guidance with Python code examples and shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce screenshots, clipboard text, window titles, desktop actions, and execution result dictionaries when used by an agent.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence and artifact _meta.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
