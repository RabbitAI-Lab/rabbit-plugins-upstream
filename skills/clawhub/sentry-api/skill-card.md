## Description:

Helps agents monitor Sentry errors and events and manage issues, projects, teams, and releases through a connected Maton account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operations teams use this skill to inspect Sentry errors, events, and application performance, and to manage Sentry resources through their authorized connection. Optional Maton functions and triggers can automate approved actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A Sentry connection can expose error, event, and project data beyond what a task needs.

Mitigation: Use only the necessary Sentry scopes, prefer read-only access, and avoid sharing raw responses unnecessarily.

Risk: Writes and optional functions or triggers can change data or keep running after the task ends.

Mitigation: Confirm each write, connection, function, and trigger before use; remove unused automations and connections afterward.

Risk: Third-party destinations can receive data from automated actions.

Mitigation: Confirm each destination and the data it will receive; avoid third-party destinations unless the data flow is understood.

## Reference(s):

- [Sentry skill release on ClawHub](https://clawhub.ai/byungkyu/skills/sentry-api)
- [Sentry API documentation](https://docs.sentry.io/api/)
- [Sentry API authentication](https://docs.sentry.io/api/auth/)
- [Maton documentation](https://docs.maton.ai)
- [Maton CLI manual](https://cli.maton.ai/manual)
- [Maton homepage](https://maton.ai)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Text or Markdown with optional CLI commands and API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses depend on the authorized Sentry connection and the requested operation.]

## Skill Version(s):

1.2.5 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
