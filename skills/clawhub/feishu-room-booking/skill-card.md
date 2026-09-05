## Description:

Feishu Room Booking helps Feishu users configure tenant room catalogs, find available rooms, book or backfill meeting rooms, manage preferences, monitor waitlists, and track workspace defaults.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qiushibang](https://clawhub.ai/user/qiushibang)

### License/Terms of Use:

MIT-0

## Use Case:

Employees and their delegated agents use this skill to find, reserve, and maintain Feishu meeting-room bookings across configured office buildings. It is especially useful for tenant onboarding, room availability checks, meeting creation, preference management, automatic backfill, and waitlist monitoring.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can use Feishu calendar read/write, attendee-read, and free/busy access to scan calendars and reserve rooms.

Mitigation: Install only after confirming those Feishu permissions are acceptable for the user or organization.

Risk: Heartbeat, backfill, and waitlist workflows can reserve rooms later without per-action confirmation.

Mitigation: Enable these workflows only when the user explicitly wants automated room reservation, and review waitlist or backfill settings before use.

Risk: Bulk preference listing may expose user room preferences beyond the immediate booking task.

Mitigation: Avoid bulk preference listing unless there is an administrative reason.

## Reference(s):

- [Feishu Room Booking on ClawHub](https://clawhub.ai/qiushibang/skills/feishu-room-booking)
- [Room mapping catalog](references/room-mapping.json)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, JSON or table command output, and configuration updates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses bundled scripts to read or update tenant, preference, waitlist, workspace, and room mapping JSON files.]

## Skill Version(s):

3.2.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
