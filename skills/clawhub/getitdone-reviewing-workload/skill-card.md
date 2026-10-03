## Description:

Summarizes due, blocked, in-progress, and in-review GetItDone tasks by workspace or project without changing them.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bsalaeddin](https://clawhub.ai/user/bsalaeddin)

### License/Terms of Use:

MIT-0

## Use Case:

GetItDone users can review their workload by workspace or project, identify blocked and upcoming tasks, and choose their next actions without modifying tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A summary could cover an unintended workspace or project.

Mitigation: Confirm the workspace when ambiguous and use the named project's ID when filtering tasks.

Risk: A workload review could accidentally change tasks if write tools are used.

Mitigation: Use only the disclosed read-only workspace, project, task-list, and task-detail tools.

## Reference(s):

- [GetItDone: Reviewing Workload release](https://clawhub.ai/bsalaeddin/skills/getitdone-reviewing-workload)
- [Publisher profile](https://clawhub.ai/user/bsalaeddin)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Prioritized workload summary with up to three suggested next actions.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
