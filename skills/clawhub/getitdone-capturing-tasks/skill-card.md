## Description:

Helps users capture and manage GetItDone tasks from notes or requests, including creation, updates, dependencies, completion, and reversible archiving.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bsalaeddin](https://clawhub.ai/user/bsalaeddin)

### License/Terms of Use:

MIT-0

## Use Case:

GetItDone users can turn notes and requests into tasks and manage existing tasks, recurring completions, dependencies, and archives.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Incorrectly extracted tasks or dates could create unintended task changes.

Mitigation: Preview extracted tasks and resolved dates before writing, and ask the user to correct them.

Risk: Duplicate tasks or unintended archiving could disrupt task tracking.

Mitigation: Check for existing tasks before creation, require confirmation before archiving, and use reversible archiving rather than deletion.

Risk: Task access grants the agent permission to read project and task context and make changes.

Mitigation: Grant task and project permissions only when comfortable with those actions; confirm the target workspace before changes.

## Reference(s):

- [GetItDone: Capturing Tasks on ClawHub](https://clawhub.ai/bsalaeddin/skills/getitdone-capturing-tasks)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Plain text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Task previews, short IDs, and updated task states; approved changes are made in GetItDone.]

## Skill Version(s):

1.0.1 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
