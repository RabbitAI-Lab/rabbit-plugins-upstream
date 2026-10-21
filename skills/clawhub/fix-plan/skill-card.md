## Description:

Manages the format, prioritization, synchronization, and lifecycle of fix-plan and checklist trackers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and project managers use this skill to maintain task trackers, triage blockers, draft and complete items, and reconcile linked issue or pull-request status.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Tracker consolidation or migrations may overwrite or remove planning files or home-directory agent/session data.

Mitigation: Review the proposed file changes and require a dry run or explicit confirmation before consolidation or migration.

Risk: External issue updates, indexing, or hook audits can change project state beyond the local tracker.

Mitigation: Require explicit confirmation before GitHub or Plane changes, Qdrant indexing, or hook audits.

## Reference(s):

- [Fix Plan on ClawHub](https://clawhub.ai/drumrobot/skills/fix-plan)

## Skill Output:

**Output Type(s):** [Markdown, Guidance, Shell commands]

**Output Format:** [Markdown tracker updates and guidance with optional shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May modify tracker files, issue drafts, and connected project records.]

## Skill Version(s):

0.18.0 (source: ClawHub release and CHANGELOG; frontmatter lists 0.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
