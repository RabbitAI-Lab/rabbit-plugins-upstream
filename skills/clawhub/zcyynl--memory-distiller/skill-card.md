## Description:

OpenClaw's subconscious. Automatically distills conversation insights, corrections, and preferences into durable memory. The agent that learns from every session so you never have to repeat yourself.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zcyynl](https://clawhub.ai/user/zcyynl)

### License/Terms of Use:


## Use Case:

External OpenClaw users and agent developers use this skill to turn durable corrections, preferences, and insights from conversations into persistent memory entries. It is intended to reduce repeated mistakes by updating long-term memory only when a reusable, actionable rule passes the documented quality gate.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can silently save broad conversation-derived memories that affect future sessions.

Mitigation: Install only when automatic persistent memory is desired, and regularly review MEMORY.md, USER.md, and dated memory files.

Risk: Sensitive information could be captured if a conversation includes secrets or personal data while the skill is active.

Mitigation: Avoid sharing passwords, tokens, API keys, identification numbers, bank details, or sensitive third-party information during active use.

Risk: Installing with an unpinned @latest command can make the installed package version less explicit.

Mitigation: Prefer a pinned or otherwise verified ClawHub installer version for controlled environments.

## Reference(s):

- [Memory Distiller ClawHub page](https://clawhub.ai/zcyynl/skills/memory-distiller)
- [Claudeception inspiration](https://github.com/disler/claudeception)
- [claw-multi-agent](https://github.com/zcyynl/claw-multi-agent)

## Skill Output:

**Output Type(s):** [Text, Markdown, Configuration, Guidance]

**Output Format:** [Markdown memory entries and concise user-facing status text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes structured memory entries to MEMORY.md, USER.md, or dated memory files when trigger and quality checks pass.]

## Skill Version(s):

1.0.1 (source: server release metadata; artifact frontmatter lists 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
