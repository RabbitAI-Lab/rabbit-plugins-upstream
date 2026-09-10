## Description:

This skill helps an agent suggest follow-up actions after task completion and detect stalled work that needs correction.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent users use this skill to keep coding or workflow sessions moving after a task completes by surfacing next steps, stalled work, and required user decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Persistent global hooks can interrupt normal task completion and trigger follow-up prompts or work unexpectedly.

Mitigation: Review the hook registration before installing and enable the skill only when automatic next-action prompting is desired.

Risk: Transcript-derived workspace inspection and local debug logging can expose private project context.

Mitigation: Avoid using the skill across multiple private workspaces unless that cross-workspace discovery is acceptable, and review or clear local logs as needed.

Risk: Automatic follow-up skill invocation can act on stale or inaccurate workflow state.

Mitigation: Review proposed next actions before execution and keep task trackers, PR checklists, and workspace plans current.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/drumrobot/skills/next)
- [Skill Definition](SKILL.md)
- [Ask Gates](ask-gates.md)
- [Stall Detection](stall-detect.md)
- [Suggestion Patterns](suggestion-patterns.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown with concise next-action options and occasional shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May prompt the user to choose follow-up actions and may invoke dependent skills when available.]

## Skill Version(s):

0.10.0 (source: server release metadata and CHANGELOG.md, released 2026-09-06)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
