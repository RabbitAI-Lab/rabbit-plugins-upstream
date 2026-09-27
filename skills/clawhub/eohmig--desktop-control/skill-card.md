## Description:

Advanced desktop automation for mouse, keyboard, screen capture, window management, clipboard operations, and autonomous desktop task execution.

This skill is ready for commercial/non-commercial use.

## Publisher:

[eohmig](https://clawhub.ai/user/eohmig)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to automate interactive desktop workflows that require direct mouse, keyboard, screenshot, window, and clipboard actions. It is suited to controlled environments where live desktop control and screen capture are acceptable.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can control the active desktop through mouse, keyboard, window, screenshot, and clipboard operations.

Mitigation: Use it only in controlled sessions, keep the failsafe enabled, and avoid running it around passwords, confidential documents, or sensitive applications.

Risk: Approval mode does not cover every sensitive action according to the security evidence.

Mitigation: Treat approval mode as supplemental, require human review for high-impact workflows, and constrain tasks before execution.

Risk: Screenshots, clipboard content, typed text, and logs may expose sensitive data.

Mitigation: Review and delete saved screenshots and logs, avoid capturing secrets, and run with pinned dependencies in an isolated environment where possible.

## Reference(s):

- [Desktop Control ClawHub Listing](https://clawhub.ai/eohmig/skills/desktop-control)
- [eohmig Publisher Profile](https://clawhub.ai/user/eohmig)
- [Skill Documentation](artifact/SKILL.md)
- [AI Agent Guide](artifact/AI_AGENT_GUIDE.md)
- [Quick Reference](artifact/QUICK_REFERENCE.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown documentation with Python code examples and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return execution status, step records, screenshots, or image objects when used by an agent.]

## Skill Version(s):

1.0.0 (source: server release metadata and artifact _meta.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
