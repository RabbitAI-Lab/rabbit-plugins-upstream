## Description:

Manages fix_plan.md and checklist.md planning trackers, including schema formatting, blocked priority triage, completion movement, GitHub or Plane sync, issue drafts, model triage, and completion criteria.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and project maintainers use this skill to keep planning trackers structured, synchronized with external issue state, and clear about blocked work, completion criteria, deferred plans, and archive movement.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automatic tracker edits and archive movement can change local planning files.

Mitigation: Review planned file changes before accepting them, keep version control enabled, and use dry-run modes where helper scripts provide them.

Risk: Artifact lookup and ingest helpers can read markdown content and interact with configured Qdrant collections.

Mitigation: Run these helpers only after confirming the target workspace profile, Qdrant URL, collection names, and the content being indexed or queried.

Risk: Workspace profile JSON output can include an environment-derived Plane API token.

Mitigation: Do not capture or share workspace_profile.py --json output unless the plane_token field is removed or redacted.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/drumrobot/skills/fix-plan)
- [SKILL.md](artifact/SKILL.md)
- [format.md](artifact/format.md)
- [priority.md](artifact/priority.md)
- [move.md](artifact/move.md)
- [sync.md](artifact/sync.md)
- [completion-criteria.md](artifact/completion-criteria.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with tracker edits, checklist entries, shell commands, configuration notes, and optional script-backed file updates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May edit local planning files and invoke helper scripts for cleanup, sync checks, or artifact indexing when directed by the user or workflow.]

## Skill Version(s):

0.5.1 (source: server release metadata, target metadata, and changelog, released 2026-08-05)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
