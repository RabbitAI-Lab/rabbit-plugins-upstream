## Description:

Generates phased, dependency-ordered implementation tasks from specifications.

This skill is ready for commercial/non-commercial use.

## Publisher:

[athola](https://clawhub.ai/user/athola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill after a specification is complete to turn specs and implementation plans into phased tasks with explicit dependencies, parallel markers, affected files, and completion criteria.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad triggers may cause the skill to appear in ordinary planning or implementation conversations more often than intended.

Mitigation: Review whether task-planning behavior is appropriate for the current request before relying on its task breakdown.

Risk: Generated task plans can still contain incorrect dependencies, unsafe parallel markers, or incomplete file coordination.

Mitigation: Review dependencies, shared files, shared state, and completion criteria before assigning tasks for execution.

Risk: The inspected release is documentation-only, while the related full plugin may contain separate agents, hooks, or commands.

Mitigation: Review and scan any separate Claude Code plugin before installing it as part of a larger workflow.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-spec-kit-task-planning)
- [Project homepage from ClawHub metadata](https://github.com/athola/claude-night-market/tree/master/plugins/spec-kit)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown task breakdowns with task IDs, phases, dependencies, affected files, parallel markers, and completion criteria]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include configuration or ignore-file guidance when the implementation plan identifies a relevant technology stack.]

## Skill Version(s):

1.9.19 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
