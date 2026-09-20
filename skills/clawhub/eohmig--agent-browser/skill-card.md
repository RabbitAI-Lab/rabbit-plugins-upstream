## Description:

agent-browser is a browser automation CLI that lets AI agents navigate pages, fill forms, click buttons, take screenshots, extract data, test web apps, and automate supported Electron, Slack, and cloud-browser workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[eohmig](https://clawhub.ai/user/eohmig)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and AI-agent users use this skill to drive browser and supported desktop-style automation tasks, including page interaction, form completion, screenshots, data extraction, QA, Slack workflows, and cloud-browser sessions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide broad browser, Slack, and desktop-style automation in authenticated contexts.

Mitigation: Require explicit confirmation before logins, messages, form submissions, purchases, deletions, or extraction from private sessions.

Risk: The skill can rely on runtime tooling that may be dynamically resolved if used through npx.

Mitigation: Pin and review the agent-browser package version, and prefer an installed reviewed version over live npx resolution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/eohmig/skills/agent-browser)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and operational guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill may guide an agent to invoke agent-browser commands that act in browser, Slack, Electron, and cloud-browser contexts.]

## Skill Version(s):

1.0.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
