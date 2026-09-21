## Description:

Cleanup runs a session-end self-improvement and state-preservation workflow that reviews automation, persists knowledge, updates trackers, and registers next-session work.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent operators use this skill at the end of a work session to preserve progress, capture reusable findings, review automation issues, and prepare next-session tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can archive session content and artifacts, which may preserve sensitive information beyond the active session.

Mitigation: Use it only with an intended private RAG backend or local queue, avoid sessions containing secrets unless redaction controls are in place, and disable memory or RAG behavior when appropriate.

Risk: The skill can write durable queue files under ~/.claude and update task or checklist records automatically.

Mitigation: Review configuration and generated tracker changes before relying on automated cleanup output, especially when using non-interactive modes.

## Reference(s):


## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May direct the agent to write tracker records, RAG entries, and local pending-import queue files.]

## Skill Version(s):

0.7.1 (source: evidence.release.version and changelog, released 2026-09-20)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
