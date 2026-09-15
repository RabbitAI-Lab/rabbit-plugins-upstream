## Description:

Fix Plan manages fix_plan.md and checklist.md task trackers, including item schema, lifecycle transitions, priority triage, synchronization, draft planning, and completion criteria.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineering agents use this skill to keep project task trackers consistent while adding, updating, syncing, prioritizing, and completing work items.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Workspace profile and agent hook inspection can expose credentials or sensitive local configuration.

Mitigation: Review the JSON-output path and profile handling before installation, and keep token files and hook configuration scoped to trusted workspaces.

Risk: Optional Plane and Qdrant workflows can send private tracker or markdown artifact content to external services.

Mitigation: Keep Plane and Qdrant behavior opt-in, configure only trusted endpoints, and avoid enabling them for repositories containing private plans or credentials.

Risk: Qdrant import behavior depends on an external importer path and dependencies.

Mitigation: Pin or vendor the importer path and dependencies before using artifact indexing.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/drumrobot/skills/fix-plan)
- [Skill Overview](SKILL.md)
- [Format Guide](format.md)
- [Priority Guide](priority.md)
- [Sync Guide](sync.md)
- [Changelog](CHANGELOG.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with optional code and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May update tracker files, local archive state, and optional sync/indexing targets when the caller enables those workflows.]

## Skill Version(s):

0.13.0 (source: release evidence and CHANGELOG, released 2026-09-13)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
