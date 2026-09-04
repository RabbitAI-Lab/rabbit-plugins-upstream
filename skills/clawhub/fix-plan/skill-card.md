## Description:

Fix Plan manages fix_plan.md and checklist.md tracker schemas, lifecycle transitions, priority triage, sync checks, issue drafts, model triage, completion criteria, and related maintenance flows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and project maintainers use this skill to keep agent-readable project trackers consistent, deduplicate new work items, sync external issue and pull-request state, and move completed work into summaries or archives.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Default and cleanup flows can broadly mutate tracker and archive files.

Mitigation: Review tracker diffs after default runs, configure archive or RAG options deliberately, and keep backups before move or archive cleanup when completed-work detail matters.

Risk: workspace_profile.py --json can expose a Plane token in logged contexts.

Mitigation: Avoid running workspace_profile.py --json in logs unless the token is redacted.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/drumrobot/skills/fix-plan)
- [Skill overview](artifact/SKILL.md)
- [Changelog](artifact/CHANGELOG.md)
- [Tracker format guide](artifact/format.md)
- [Priority guide](artifact/priority.md)
- [Sync guide](artifact/sync.md)
- [Move guide](artifact/move.md)
- [Upsert guide](artifact/upsert.md)
- [Completion criteria guide](artifact/completion-criteria.md)

## Skill Output:

**Output Type(s):** [Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown tracker edits with inline shell commands and helper-script guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May update tracker files, archive completed-work entries, and emit local or external sync guidance depending on configured tools and receivers.]

## Skill Version(s):

0.11.0 (source: server release metadata and CHANGELOG, released 2026-09-01)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
