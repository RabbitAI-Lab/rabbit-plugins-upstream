## Description:

Suggests next actions after task completion, using explicit invocation, hooks, stall detection, ask gates, and suggestion templates to surface follow-up choices.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent users use this skill to decide what to do after a task completes, including whether to verify, continue, delegate, clean up, or hold work. It is especially relevant in workflows where hook-triggered completion checks and task-list-aware follow-up options are desired.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Hook-based automation can prompt follow-up actions without explicit user invocation.

Mitigation: Review and enable the Stop and UserPromptSubmit hook setup only in workspaces where automatic next-action prompts are desired.

Risk: The skill may inspect transcript context, task state, and planning files while discovering follow-up candidates.

Mitigation: Review the transcript/context-usage behavior and cross-workspace fix_plan.md discovery behavior before installation.

Risk: Fallback behavior can write selected follow-up work to project checklist files when task tools are unavailable.

Mitigation: Confirm fallback write targets and repository checklist conventions before using multi-selection workflows.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/drumrobot/skills/next)
- [Ask gates](ask-gates.md)
- [Stall detection](stall-detect.md)
- [Suggestion patterns](suggestion-patterns.md)
- [Changelog](CHANGELOG.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with structured follow-up options and inline command guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May invoke or recommend follow-up skill calls, task registration, hook configuration, and checklist updates depending on the selected workflow.]

## Skill Version(s):

0.10.2 (source: ClawHub release metadata and CHANGELOG, released 2026-09-24)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
