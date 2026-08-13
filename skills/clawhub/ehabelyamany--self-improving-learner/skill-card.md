## Description:

Helps an agent record failures, corrections, missing capabilities, and useful discoveries, then periodically review and promote recurring lessons into durable memory or workflow guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ehabelyamany](https://clawhub.ai/user/ehabelyamany)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to capture meaningful errors, user corrections, knowledge gaps, and better approaches so future sessions can avoid repeated mistakes. It is most relevant for OpenClaw-style agent workflows that maintain local learning files and optional bootstrap reminders.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Persistent learning files may capture sensitive personal, business, or credential information if users log too much context.

Mitigation: Review learning entries before promotion and avoid storing secrets, credentials, private personal details, or sensitive business data.

Risk: Broad hook setup can inject reminders across projects and expose cross-project memory or prompt-file behavior.

Mitigation: Prefer project-level hooks and use global hook setup only after reviewing the exposure across workspaces.

Risk: Unreviewed lessons can turn incorrect observations into future-session guidance.

Mitigation: Review .learnings entries before promoting them into MEMORY.md, AGENTS.md, SOUL.md, or TOOLS.md.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/ehabelyamany/skills/self-improving-learner)
- [Entry Examples](references/examples.md)
- [Hook Setup Guide](references/hooks-setup.md)
- [OpenClaw Integration](references/openclaw-integration.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown guidance with inline shell commands and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide creation or update of local .learnings, MEMORY.md, AGENTS.md, SOUL.md, and TOOLS.md files.]

## Skill Version(s):

1.0.0 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
