## Description:

Unified backlog lifecycle management and task tracking across session TODOs, workspace checklists, and issue trackers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to capture, triage, prioritize, synchronize, and prune backlog items across local markdown checklists and issue trackers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Default backlog synchronization may contact configured issue trackers and share repository task, branch, issue, or pull request context.

Mitigation: Run synchronization only in repositories where sharing that context with configured trackers is acceptable.

Risk: Backlog maintenance can update local checklist files such as fix_plan.md and checklist.md.

Mitigation: Review proposed file changes before accepting edits and keep the workspace under version control.

## Reference(s):


## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown reports, checklist updates, and command guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May update local backlog files and may use configured issue tracker commands during synchronization.]

## Skill Version(s):

0.1.0 (source: frontmatter, CHANGELOG, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
