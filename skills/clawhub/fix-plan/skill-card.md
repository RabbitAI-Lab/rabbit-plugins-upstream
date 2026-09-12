## Description:

Manages fix_plan.md and checklist.md task trackers, including schema checks, priority triage, item lifecycle updates, GitHub and Plane sync, issue-draft cleanup, and completion records.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineering teams use this skill to keep project task trackers consistent, prioritized, synchronized with external issue state, and clear about completed or blocked work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Tracker edits, archive moves, and external-state sync can change task status or remove live tracker content from its original section.

Mitigation: Review proposed diffs before accepting changes and run sync only with trusted GitHub or Plane configuration.

Risk: Optional hook, indexing, and integration paths may read local configuration, write persistent checkpoints, or send markdown artifacts to a configured Qdrant service.

Mitigation: Enable hooks, Qdrant, and Plane paths only after reviewing the publisher, local helper scripts, and configured endpoints.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/drumrobot/skills/fix-plan)
- [Skill overview](artifact/SKILL.md)
- [Tracker format guide](artifact/format.md)
- [Priority triage guide](artifact/priority.md)
- [External sync guide](artifact/sync.md)
- [Claim lease guide](artifact/claim.md)
- [Completion and archive guide](artifact/move.md)
- [Release changelog](artifact/CHANGELOG.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline commands and file edits]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May update tracker files and write archive or checkpoint files when invoked with those topics.]

## Skill Version(s):

0.12.1 (source: ClawHub release metadata and CHANGELOG, released 2026-09-08)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
