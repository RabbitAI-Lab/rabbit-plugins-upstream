## Description:

Fix Plan manages fix_plan.md and checklist.md tracker schemas, lifecycle cleanup, blocker priority, issue draft handling, and GitHub or Plane sync guidance for agent work plans.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent operators use this skill to keep work trackers consistent: format items, move completed work, triage blockers, draft future plans, and synchronize GitHub or Plane-backed status.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Tracker edits and archive operations can move completed entries into .bak files or remove entries from the active tracker.

Mitigation: Run archive and cleanup flows only on intended tracker files, review dry-run output where available, and keep version control or backups for tracker changes.

Risk: GitHub and Plane sync flows may poll external services and update tracker state from remote issue or PR status.

Mitigation: Use scoped credentials, prefer dry-run checks before write mode, and verify remote status changes before accepting automatic marker updates.

Risk: The workspace profile helper can include a Plane API token in JSON profile output.

Mitigation: Redact plane_token before logging, sharing, or feeding profile output into other automation.

Risk: Qdrant ingest and lookup helpers can index planning artifacts into a local or remote vector store.

Mitigation: Remove or gate Qdrant helper use unless vector indexing of planning artifacts is explicitly intended for the workspace.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/drumrobot/skills/fix-plan)
- [Skill overview](artifact/SKILL.md)
- [Tracker format](artifact/format.md)
- [Priority triage](artifact/priority.md)
- [Sync workflow](artifact/sync.md)
- [Move and archive workflow](artifact/move.md)
- [Completion criteria](artifact/completion-criteria.md)
- [Issue draft lifecycle](artifact/issue-drafts.md)
- [Model triage](artifact/model-triage.md)
- [Sync automation](artifact/sync-automation.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration, Code]

**Output Format:** [Markdown guidance with tracker snippets, command examples, and configuration conventions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May edit tracker files, archive completed entries, poll GitHub or Plane, and call optional receiver skills when configured.]

## Skill Version(s):

0.6.0 (source: ClawHub release metadata and CHANGELOG, released 2026-08-09)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
