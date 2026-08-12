## Description:

An anthropomorphic psychology engine for modeling cognition, emotion, motivation, and social behavior as deterministic, modular agent-persona state.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nohn3043-arch](https://clawhub.ai/user/nohn3043-arch)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent builders use this skill to design or run deterministic persona-simulation components for long-running interactive agents, narrative characters, and emotionally consistent behavior modeling.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional cross-session persona persistence can store persona memories, relationship scores, or episodes that may contain sensitive personal data.

Mitigation: Confirm whether persona JSON files are stored in the workspace, ~/.openclaw/personas, or a server store, and avoid storing sensitive real personal data unless there is a deletion plan.

Risk: State synchronization with another extension can make persona data available outside the immediate skill workflow.

Mitigation: Review storage and sync behavior before enabling persistence or extension integration, and keep workspace or server stores scoped to the intended agent.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/nohn3043-arch/skills/anthropomorphic-agent-engine)
- [Project homepage](https://github.com/nohn3043-arch/Anthropomorphic-Agent-Engine)
- [EmotionBehaviorMap](references/EmotionBehaviorMap.md)
- [MotiveConflictRules](references/MotiveConflictRules.md)
- [PersonaPersistence](references/PersonaPersistence.md)
- [spl-agent-engine on PyPI](https://pypi.org/project/spl-agent-engine/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with Python examples and JSON-shaped persona state schemas]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce deterministic persona-state snapshots, motive-resolution records, and persistence guidance.]

## Skill Version(s):

1.1.1 (source: server release metadata; artifact frontmatter reports 2.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
