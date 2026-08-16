## Description:

Provides structured task and time management guidance using GTD, Pomodoro, Eisenhower prioritization, OKR planning, time blocking, reviews, and habit tracking.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qq435912743](https://clawhub.ai/user/qq435912743)

### License/Terms of Use:

MIT-0

## Use Case:

External users and teams use this skill to turn fragmented tasks and goals into structured task lists, priority matrices, daily plans, OKR breakdowns, Pomodoro schedules, and review templates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill includes a persistent learning component that can record user preferences, usage history, notes, and error patterns locally.

Mitigation: Use the learning component only with user consent, avoid sensitive task content in notes, and provide a clear way to review, edit, or delete learned_patterns.json.

Risk: The learner can target skill directories supplied as command arguments.

Mitigation: Run learner commands only against the intended task-time-manager directory and review path arguments before execution.

Risk: The skill describes changing SKILL.md based on accumulated errors or usage.

Mitigation: Require explicit human review before any skill instruction edits are applied.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qq435912743/skills/task-time-manager)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Structured Markdown with tables, optional CSV-style tables, and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces plans, task states, priorities, schedules, OKRs, review templates, and optional local learning records.]

## Skill Version(s):

1.0.0 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
