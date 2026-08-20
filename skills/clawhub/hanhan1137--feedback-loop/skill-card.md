## Description:

Transforms user feedback about an agent's output or behavior into structured feedback logs, durable memory entries, and consistency checks so future responses follow agreed lessons.

This skill is ready for commercial/non-commercial use.

## Publisher:

[hanhan1137](https://clawhub.ai/user/hanhan1137)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to convert explicit praise, criticism, consensus, and behavior-change requests into persistent feedback records and reusable behavioral rules. It is intended for workflows where an agent should remember confirmed user feedback while avoiding accidental logging of ambiguous or test-only preferences.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can turn user feedback into persistent agent memory and future behavior rules.

Mitigation: Require explicit confirmation before durable writes beyond a dedicated feedback log, and avoid storing sensitive personal or credential-like information.

Risk: The skill can affect governance or control files such as AGENTS.md, MEMORY.md, skills, configuration, or git history.

Mitigation: Manually review proposed control-file, configuration, skill, or git operations before allowing them.

Risk: Ambiguous feedback or test-only preferences could be mistaken for durable user preferences.

Mitigation: Confirm unclear feedback and only persist preferences after genuine user recognition or instruction.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/hanhan1137/skills/feedback-loop)
- [Publisher profile](https://clawhub.ai/user/hanhan1137)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Files, Shell commands]

**Output Format:** [Markdown guidance with structured log entries and proposed file updates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose or create persistent feedback-log, conclusions, MEMORY, AGENTS, or configuration updates when its trigger conditions are met.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
