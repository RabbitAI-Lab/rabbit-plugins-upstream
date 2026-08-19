## Description:

Suggests context-aware next actions after task completion, including stall detection, ask gates, and follow-up option templates for agent workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent operators use this skill to surface actionable follow-up choices after work completes, detect stalled workflow handoffs, and route selected next steps through task tracking or helper skills.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Auto-triggered workflow coordination may run in response to task-completion signals rather than explicit user invocation.

Mitigation: Keep automatic hooks disabled unless this behavior is desired, and use the skill only in workspaces where assertive follow-up coordination is acceptable.

Risk: The skill may inspect broad local or project state, including task lists, workspace trackers, transcript paths, and GitHub-related workflow state.

Mitigation: Scope GitHub tokens, transcript access, and workspace trackers to projects where this inspection is acceptable before installation.

Risk: The skill can depend on helper skills, run local helper scripts, modify trackers, and dispatch follow-up work.

Mitigation: Review the fix and hook-kit dependencies and require user confirmation for externally visible or state-changing follow-up actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/drumrobot/skills/next)
- [Ask Gates](artifact/ask-gates.md)
- [Stall Detection](artifact/stall-detect.md)
- [Suggestion Patterns](artifact/suggestion-patterns.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration instructions]

**Output Format:** [Markdown guidance with structured next-action options and inline commands when relevant]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May call agent task and question tools, read local workspace trackers, and propose follow-up actions based on current task state.]

## Skill Version(s):

0.8.1 (source: server release metadata and CHANGELOG top entry)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
