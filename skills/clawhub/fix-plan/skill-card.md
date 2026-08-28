## Description:

Fix Plan manages fix_plan.md and checklist.md tracker schema, lifecycle state, blocker prioritization, sync, issue-draft cleanup, model triage, and completion criteria for agent workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and agents use this skill to maintain project task trackers, move completed work, validate checklist format, synchronize GitHub and Plane state, and triage blocked or model-suitable tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Tracker automation can change local fix_plan.md or checklist.md state and archive completed entries.

Mitigation: Review tracker diffs before committing changes and run the format or verify topic after automated cleanup.

Risk: Plane and GitHub sync workflows can act on external tracker state when credentials and workspace profiles are configured.

Mitigation: Confirm token and workspace configuration before use, and use dry-run behavior for Plane bulk updates before applying changes.

Risk: Optional RAG or Qdrant dispatch can send project tracker content to an external receiver.

Mitigation: Enable only approved receivers and avoid dispatching sensitive project data unless that receiver is authorized.

Risk: Hook and home-configuration checks may inspect agent configuration paths under the user's home directory.

Mitigation: Install only in environments where those paths are in scope and review hook configuration before enabling related workflows.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/drumrobot/skills/fix-plan)
- [SKILL.md](SKILL.md)
- [format.md](format.md)
- [sync.md](sync.md)
- [priority.md](priority.md)
- [CHANGELOG.md](CHANGELOG.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration]

**Output Format:** [Markdown guidance with inline commands and tracker-edit instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide edits to local tracker files and configured external-tracker workflows.]

## Skill Version(s):

0.9.1 (source: server release metadata and CHANGELOG, released 2026-08-26)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
