## Description:

Helps agents administer Zoom users, meetings, webinars, recordings, and account settings through a user-authorized admin connection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Workspace administrators and their agents can list Zoom users, review meetings and recordings, and manage meetings or account settings after authorizing the intended Zoom account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Admin-level access can expose users' meetings, recordings, and account settings across the authorized Zoom workspace.

Mitigation: Confirm the intended account, use only necessary access, and start with read or list operations.

Risk: Creating, changing, or deleting resources can affect other users and meeting participants.

Mitigation: Require explicit approval for every create, update, or delete action and confirm its target and effect.

Risk: Functions, triggers, and destinations can continue acting or forwarding data after setup.

Mitigation: Approve each automation and destination separately, inspect its scope, and remove it when no longer needed.

## Reference(s):

- [Zoom Admin skill release](https://clawhub.ai/byungkyu/skills/zoom-admin-api)
- [Maton homepage](https://maton.ai)
- [Maton documentation](https://docs.maton.ai)
- [Maton CLI manual](https://cli.maton.ai/manual)
- [Zoom API overview](https://developers.zoom.us/docs/api/)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Code, Configuration guidance]

**Output Format:** [Markdown with CLI commands, API examples, and optional code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance is scoped to the authorized Zoom account; actions may require an active Maton connection.]

## Skill Version(s):

1.2.5 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
