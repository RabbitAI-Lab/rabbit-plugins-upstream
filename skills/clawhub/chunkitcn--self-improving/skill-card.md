## Description:

Self-reflection, self-criticism, self-learning, and self-organizing memory help an agent evaluate its work, catch mistakes, and improve future behavior from explicit corrections and reusable lessons.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chunkitcn](https://clawhub.ai/user/chunkitcn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to add a local memory workflow for learning from explicit user corrections, self-reflection, and repeated work patterns. It is intended for agents that need transparent, user-controlled improvement across sessions without storing sensitive data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Persistent local memory can affect future agent behavior across sessions.

Mitigation: Install only when persistent memory is desired, periodically inspect or export ~/self-improving/, and use the documented forget and export flows when needed.

Risk: Workspace steering files and self-improving files can change how future agents operate.

Mitigation: Review proposed AGENTS.md, SOUL.md, HEARTBEAT.md, and ~/self-improving/ changes before applying them.

Risk: The optional Proactivity companion install may require trusting an additional resolved package.

Mitigation: Decline the optional Proactivity install unless the package source and behavior are trusted.

## Reference(s):

- [Self Improving on ClawHub](https://clawhub.ai/chunkitcn/skills/self-improving)
- [Self-Improving Homepage](https://clawic.com/skills/self-improving)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown instructions with shell commands and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces local memory files under ~/self-improving/ and optional workspace steering snippets when installed.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
