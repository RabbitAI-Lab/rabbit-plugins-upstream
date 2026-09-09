## Description:

Launch and drive coding agents (codex, claude, agy) through the Herdr CLI. Use before starting or prompting a subagent via herdr agent or pane commands, and when a herdr command fails or an agent seems stuck or silently lost a prompt.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tenequm](https://clawhub.ai/user/tenequm)

### License/Terms of Use:

Apache 2.0

## Use Case:

Developers and engineers use this skill to launch, prompt, monitor, and troubleshoot Codex, Claude Code, and Antigravity agents through Herdr. It provides operational guidance for avoiding lost prompts, misread agent states, and fragile terminal-multiplexer workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Default launch recipes can reduce trust and approval gates for coding agents.

Mitigation: Review recipes before use, prefer trusted isolated disposable directories, avoid automatic approval or accept-edits on unreviewed repositories, and remove temporary Gemini trusted-folder entries after the session.

Risk: Agent state and prompt-delivery signals can be misleading during Herdr-driven sessions.

Mitigation: Confirm progress by reading the pane or checking expected output files before resending prompts, closing panes, or treating an agent as finished.

## Reference(s):

- [Herdr documentation](https://herdr.dev)
- [ClawHub skill page](https://clawhub.ai/tenequm/skills/herdr-faq)
- [OpenClaw homepage](https://github.com/tenequm/skills/tree/main/skills/herdr-faq)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration]

**Output Format:** [Markdown with inline bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Operational guidance for agent launch recipes, prompt handling, state checks, and failure triage.]

## Skill Version(s):

0.3.2 (source: frontmatter, changelog, release evidence; released 2026-09-09)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
