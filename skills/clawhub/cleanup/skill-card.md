## Description:

Runs a configurable end-of-session workflow to review improvements, preserve knowledge, update work records, and recommend next actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent users use this skill at session end to review lessons learned, persist useful knowledge, reconcile checklists and trackers, and prepare a handoff or next action.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Session or artifact content may be persisted to RAG or a local retry queue.

Mitigation: Review what will be stored and disable persistence in sensitive workspaces.

Risk: End-of-session automation may commit changes or modify work records and external trackers.

Mitigation: Review proposed changes and tracker connections before running cleanup.

Risk: Broad wrap-up triggers and hook enforcement may block or alter normal session flow.

Mitigation: Review triggers and disable hook enforcement where it is not wanted.

## Reference(s):

- [Cleanup on ClawHub](https://clawhub.ai/drumrobot/skills/cleanup)

## Skill Output:

**Output Type(s):** [Markdown, Guidance, Shell commands, Configuration]

**Output Format:** [Markdown with checklists and command suggestions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May update local work records or external trackers and persist session content when configured.]

## Skill Version(s):

0.9.0 (source: ClawHub release and CHANGELOG; skill metadata says 0.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
