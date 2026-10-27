## Description:

Runs a session-end cleanup workflow that reviews improvements, preserves useful knowledge, and hands off unfinished work.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users invoke this skill at the end of a session to review work, save reusable knowledge, update task state, and prepare a handoff.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Session-end actions may run hooks or scripts and alter task or checklist state.

Mitigation: Review enabled actions and hook configuration before installation; approve state changes appropriate to the project.

Risk: Session content may be persisted to RAG or local queues, including sensitive material.

Mitigation: Set explicit do-not-store expectations for sensitive projects and disable persistence when it is not appropriate.

Risk: The graph-stop evaluator may execute code resolved from the active workspace.

Mitigation: Disable or fix the evaluator unless it resolves only trusted code outside the active workspace.

## Reference(s):

- [Cleanup on ClawHub](https://clawhub.ai/drumrobot/skills/cleanup)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown with optional commands and status summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May update checklists and persist session knowledge when enabled.]

## Skill Version(s):

0.11.0 (source: ClawHub release metadata and CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
