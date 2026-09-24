## Description:

Self-reflection + Self-criticism + Self-learning + Self-organizing memory. Agent evaluates its own work, catches mistakes, and improves permanently.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gasgangrene](https://clawhub.ai/user/gasgangrene)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to help an agent learn from explicit corrections, self-reflection, and repeated workflow patterns by maintaining local memory files and workspace guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill installs persistent local learning files and workspace steering that can affect future agent behavior.

Mitigation: Review planned edits to AGENTS.md, SOUL.md, HEARTBEAT.md, and ~/self-improving/ before setup, and keep memory entries visible and auditable.

Risk: Long-term memory can accidentally retain sensitive corrections, secrets, or personal information.

Mitigation: Follow the documented security boundaries: do not store credentials, health data, third-party information, location routines, or access patterns, and support explicit deletion requests.

Risk: Optional Proactivity companion installation may add additional package behavior beyond the base skill.

Mitigation: Install the companion only after explicit user consent and only when the resolved package is trusted.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/gasgangrene/skills/self-improving)
- [Skill Homepage](https://clawic.com/skills/self-improving)
- [Setup Guide](artifact/setup.md)
- [Security Boundaries](artifact/boundaries.md)
- [Learning Mechanics](artifact/learning.md)
- [Memory Operations](artifact/operations.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates and maintains local files under ~/self-improving/ and may suggest workspace steering updates when installed.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact frontmatter reports 1.2.16)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
