## Description:

Manages the structure, priorities, completion lifecycle, and external status synchronization of fix_plan.md and checklist.md task trackers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and project managers use this skill to maintain task trackers, prioritize blocked work, archive completed items, and reconcile tracker status with external issues and pull requests.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Archiving and deleting tracker entries or drafts can remove information needed later.

Mitigation: Back up trackers and drafts, and review proposed changes before allowing archive or deletion.

Risk: GitHub, Plane, Qdrant, or CollabMD integrations can change or share task information outside the local workspace.

Mitigation: Review configured destinations and credentials before enabling synchronization, publishing, or indexing.

Risk: Access to local workspace profiles and user-scoped agent or plugin directories can affect sensitive configuration.

Mitigation: Review ~/.agents and ~/.config profiles, especially token_file and shared-artifact settings, and limit access to what is needed.

## Reference(s):

- [Fix Plan on ClawHub](https://clawhub.ai/drumrobot/skills/fix-plan)
- [Tracker format guide](format.md)
- [Status synchronization guide](sync.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown tracker updates and plain-text guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May modify tracker and draft files and reconcile their status with external services.]

## Skill Version(s):

0.16.1 (source: ClawHub release, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
