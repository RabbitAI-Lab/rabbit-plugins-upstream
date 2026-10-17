## Description:

Manages the schema and lifecycle of fix_plan.md and checklist.md trackers, including item authoring, prioritization, completion, and synchronization.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and project teams use this skill to maintain actionable work trackers, triage blocked tasks, keep item states aligned with external issues and pull requests, and archive completed work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Tracker consolidation and cleanup can alter important untracked .ralph data.

Mitigation: Back up affected trackers, use dry-run paths where available, and confirm consolidation manually before replacing files or directories.

Risk: Sync and hooks may interact with local Plane/Qdrant credentials and agent automation.

Mitigation: Review configured integrations and hook behavior before installation or execution, and limit access to necessary credentials.

Risk: Pinned mission auto-graduation can edit the tracker unexpectedly.

Mitigation: Avoid --auto-graduate unless tracker edits are intended; review proposed changes before accepting them.

## Reference(s):

- [ClawHub fix-plan release](https://clawhub.ai/drumrobot/skills/fix-plan)
- [Tracker format guide](format.md)
- [Synchronization guide](sync.md)
- [Tracker move and completion guide](move.md)

## Skill Output:

**Output Type(s):** [Markdown, Files, Shell commands, Guidance]

**Output Format:** [Markdown guidance and edits to Markdown tracker files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May update tracker items, summaries, and priority flowcharts.]

## Skill Version(s):

0.17.2 (source: server-resolved ClawHub release; bundled frontmatter says 0.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
