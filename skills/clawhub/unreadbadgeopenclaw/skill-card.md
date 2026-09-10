## Description:

Marks OpenClaw sessions with a sidebar unread badge when a reply completes or fails, using an attention icon and timestamp note that auto-clears through the native session lifecycle.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pondsi](https://clawhub.ai/user/pondsi)

### License/Terms of Use:

MIT-style with mandatory attribution

## Use Case:

Developers and OpenClaw operators use this skill to keep completed or failed replies visible in the Control UI session list until the session is opened, updated, or the badge expires. It is useful for reply notifications, unread session markers, and session status flags.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can modify OpenClaw session status badges through local gateway calls.

Mitigation: Install it only when sidebar unread badge updates are desired, and review when and where the scripts are invoked.

Risk: The keep-alive script stores badge state locally and may run on a schedule.

Mitigation: Review the scheduler configuration and set OPENCLAW_STATE_DIR when the default ~/.openclaw state location is not appropriate.

Risk: Unread marks may be misleading if treated as durable workflow state instead of UI attention markers.

Mitigation: Use the native OpenClaw lifecycle as authoritative: opening the session, sending a new message, TTL expiry, and the seven-day fallback clear marks.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/pondsi/skills/unreadbadgeopenclaw)
- [OpenClaw](https://openclaw.ai)
- [Internals: how sidebar marks actually render and clear](references/internals.md)
- [SKILL.md](SKILL.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and Node.js script usage]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces local OpenClaw gateway command guidance and uses state in OPENCLAW_STATE_DIR when keep-alive behavior is scheduled.]

## Skill Version(s):

1.1.4 (source: server release metadata and CHANGELOG, released 2026-09-09)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
