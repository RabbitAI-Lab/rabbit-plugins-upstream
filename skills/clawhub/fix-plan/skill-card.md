## Description:

Fix Plan manages fix_plan.md and checklist.md task trackers, including schema validation, item lifecycle updates, priority triage, external issue sync, issue drafts, model triage, and completion movement.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineering teams use this skill to keep project tracker files consistent, triage blocked work, sync GitHub and configured backlog state, record progress, and move completed work into concise history sections.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can edit fix_plan.md and checklist.md and run bundled scripts that change tracker state.

Mitigation: Review diffs before accepting tracker changes, keep backups enabled, and use the documented scripts instead of ad hoc direct edits.

Risk: External sync, indexing, and comment-posting paths can expose project planning details through GitHub, Plane, Qdrant, CollabMD, or shared artifact directories.

Mitigation: Disable or review those workflows before using the skill on private projects, and verify destination URLs, collections, and comment targets before running them.

Risk: Workspace profile and token resolution can connect the skill to local Plane or Qdrant credentials.

Mitigation: Use least-privilege tokens, scope workspace profile files carefully, and confirm the active profile before running sync or ingest commands.

Risk: Persistent hook-style state and stop-hook nudges can affect agent workflow timing.

Mitigation: Install hooks deliberately, inspect the generated state path, and disable the hook automation when automatic sync nudges are not desired.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/drumrobot/skills/fix-plan)
- [Skill definition](artifact/SKILL.md)
- [Format guide](artifact/format.md)
- [Priority guide](artifact/priority.md)
- [Sync guide](artifact/sync.md)
- [Claim guide](artifact/claim.md)
- [Sync automation guide](artifact/sync-automation.md)
- [Release changelog](artifact/CHANGELOG.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown tracker edits, concise status reports, command snippets, and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May modify local tracker files, create backups or shared artifact copies, and invoke configured external sync or indexing tools when the user enables those workflows.]

## Skill Version(s):

0.15.0 (source: server release metadata and CHANGELOG, released 2026-09-20)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
