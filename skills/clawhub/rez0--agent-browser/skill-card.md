## Description:

Agent Browser provides CLI-driven browser automation for AI agents to navigate sites, fill forms, click controls, capture screenshots, extract data, test web apps, and automate related Electron, Slack, and cloud-browser tasks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[rez0](https://clawhub.ai/user/rez0)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and AI-agent users use this skill to automate browser workflows, exploratory testing, screenshots, data extraction, form submission, and selected desktop or cloud-browser automation tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill grants broad browser, Slack, and desktop-app automation authority while delegating detailed workflow content to mutable CLI-served content outside the reviewed artifact.

Mitigation: Review and pin the exact agent-browser package and installed browser components before use.

Risk: Automation could interact with logged-in accounts, private workspaces, forms, messages, or third-party data.

Mitigation: Use an isolated browser profile or sandbox and require explicit confirmation before logging in, sending messages, searching private workspaces, submitting forms, or modifying third-party data.

## Reference(s):

- [Agent Browser ClawHub Release](https://clawhub.ai/rez0/skills/agent-browser)
- [Artifact SKILL.md](artifact/SKILL.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown guidance with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May direct the agent to retrieve version-matched workflow content from the installed agent-browser CLI before use.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
