## Description:

Advanced desktop automation with mouse, keyboard, and screen control.

This skill is ready for commercial/non-commercial use.

## Publisher:

[breckengan](https://clawhub.ai/user/breckengan)

### License/Terms of Use:


## Use Case:

Developers and automation engineers use Control to let agents perform desktop actions such as mouse and keyboard input, screen capture, window management, clipboard access, and simple autonomous application workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can control a live desktop through mouse and keyboard actions.

Mitigation: Run it first in a non-sensitive profile or virtual machine, keep failsafe enabled, and avoid administrator mode.

Risk: Screenshot and clipboard features can expose sensitive data.

Mitigation: Do not use the skill while secrets, private documents, or sensitive clipboard contents are visible or copied.

Risk: Approval safeguards are incomplete for high-impact automation.

Mitigation: Use approval mode for interactive actions and review planned desktop actions before execution.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/breckengan/skills/control)
- [Skill Documentation](artifact/SKILL.md)
- [AI Agent Guide](artifact/AI_AGENT_GUIDE.md)
- [Quick Reference](artifact/QUICK_REFERENCE.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown documentation with Python examples and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill may also produce desktop side effects, screenshots, clipboard changes, and action logs when executed.]

## Skill Version(s):

1.0.0 (source: server-resolved release metadata and artifact/_meta.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
