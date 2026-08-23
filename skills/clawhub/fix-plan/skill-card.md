## Description:

Fix Plan helps agents manage fix_plan.md and checklist.md files, including item formatting, priority triage, completion movement, draft planning, external issue synchronization, and role-scoped tracker maintenance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineering agents use this skill to keep long-lived project trackers consistent, current, and actionable across planning, implementation, synchronization, and completion workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can modify planning and checklist files during lifecycle, cleanup, sync, and completion workflows.

Mitigation: Run cleanup and sync operations with dry-run or diff review where available, and review proposed tracker changes before committing them.

Risk: Bundled Plane and Qdrant helper scripts can interact with external systems when credentials and endpoints are configured.

Mitigation: Install only in workspaces that intentionally use those integrations, and avoid exposing broad Plane, Qdrant, or kubectl credentials to routine tracker maintenance.

Risk: plane_create_issue.py includes a Kubernetes fallback path for Plane issue creation.

Mitigation: Review or remove plane_create_issue.py before enabling the skill unless Kubernetes-backed Plane administration is explicitly required.

Risk: artifact_post_ingest.py can send Markdown documents to Qdrant.

Mitigation: Review or remove artifact_post_ingest.py before enabling the skill in environments where document indexing is not intended.

## Reference(s):

- [Fix Plan skill definition](artifact/SKILL.md)
- [Tracker format guide](artifact/format.md)
- [Priority triage guide](artifact/priority.md)
- [External sync guide](artifact/sync.md)
- [Completion movement guide](artifact/move.md)
- [Completion criteria guide](artifact/completion-criteria.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with tracker edits, command examples, scripts, and configuration conventions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May update planning files and may call local helper scripts or external tracker CLIs when invoked in an enabled workspace.]

## Skill Version(s):

0.9.0 (source: server release metadata and CHANGELOG.md, released 2026-08-20)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
