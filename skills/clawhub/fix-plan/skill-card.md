## Description:

Fix Plan manages fix_plan.md and checklist.md task trackers, including schema validation, lifecycle updates, priority triage, external tracker sync, issue-draft cleanup, and pinned-mission checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and project maintainers use Fix Plan to keep local planning trackers structured, synchronized with GitHub and optional secondary trackers, and cleaned up as work moves from active tasks to completed records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can direct agents to publish planning artifacts or post comments to external trackers without sufficiently explicit user consent.

Mitigation: Deploy it only where external publication and tracker comments are expected, and review or disable those instructions before use in local-only or read-only planning workflows.

Risk: The skill may interact with GitHub, Plane, Qdrant, CollabMD/Syncthing, hooks, and optional session-launch workflows.

Mitigation: Review registered hooks, workspace profiles, and token-file settings before installation so only intended external integrations are enabled.

## Reference(s):

- [Fix Plan overview](SKILL.md)
- [Tracker format](format.md)
- [Priority triage](priority.md)
- [GitHub and secondary-tracker sync](sync.md)
- [Issue draft lifecycle](issue-drafts.md)
- [Flowchart and pinned-mission checks](flowchart.md)
- [ClawHub skill page](https://clawhub.ai/drumrobot/skills/fix-plan)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline commands, tracker edits, and supporting script or configuration changes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May update planning files, issue-draft files, hook-related resources, and external tracker state when invoked with those topics.]

## Skill Version(s):

0.16.0 (source: server release evidence, target metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
