## Description:

Fix Plan helps agents manage fix_plan.md and checklist.md trackers, including item formatting, priority triage, completion movement, GitHub issue and pull-request state syncing, issue-draft lifecycle work, and role-scoped default workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineering teams use this skill to keep agent-maintained work trackers consistent, current, and actionable across planning, implementation, blocker triage, completion cleanup, and GitHub state checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Trackers can contain sensitive plans, customer data, or private operational details, and this skill is designed to read, edit, archive, and reorganize tracker content.

Mitigation: Review the skill before installation, restrict it to intended workspaces, and avoid using it on trackers that contain sensitive data unless the handling and retention behavior is acceptable.

Risk: The skill can poll GitHub state, optionally sync with a secondary tracker, and may use RAG or Qdrant workflows that move tracker content outside the active tracker file.

Mitigation: Disable or remove optional Qdrant ingest and lookup scripts, hook scripts, and secondary-sync paths unless those integrations are explicitly required and configured for the workspace.

Risk: Broad workflow mutation can misclassify, move, archive, or delete tracker entries if the tracker structure is already corrupt or stale.

Mitigation: Run the skill only after reviewing its proposed scope, inspect tracker diffs after execution, and keep backups or version-control history for fix_plan.md, checklist.md, issue drafts, and archive files.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/drumrobot/skills/fix-plan)
- [Fix Plan Overview](SKILL.md)
- [Format Guide](format.md)
- [Priority Guide](priority.md)
- [Sync Guide](sync.md)
- [Move Guide](move.md)
- [Issue Drafts Guide](issue-drafts.md)
- [Completion Criteria Guide](completion-criteria.md)
- [Model Triage Guide](model-triage.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with tracker edits, command examples, and configuration conventions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce or modify tracker files such as fix_plan.md, checklist.md, issue-draft files, and local archive files when invoked by an agent with write access.]

## Skill Version(s):

0.10.0 (source: server release metadata and CHANGELOG, released 2026-08-29)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
