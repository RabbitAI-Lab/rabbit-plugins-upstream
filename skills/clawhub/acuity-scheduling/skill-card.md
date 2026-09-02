## Description:

Acuity Scheduling API integration with managed OAuth for managing appointments, calendars, clients, and availability through the Maton CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to check availability and manage Acuity Scheduling appointments, calendars, clients, appointment types, forms, labels, and blocks through Maton-authenticated API calls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can authorize Maton access to a user's Acuity Scheduling account.

Mitigation: Prefer OAuth, confirm the exact account and connection before use, and create new connections only after explicit user approval.

Risk: Write operations can create, update, reschedule, cancel, or delete scheduling data.

Mitigation: Default to read/list calls first, then require clear confirmation of the target resource, payload, and intended effect before any POST, PUT, PATCH, or DELETE request.

Risk: Long-lived API keys or provider-issued tokens could be exposed through logs, command lines, files, or copied output.

Mitigation: Use OAuth and the Maton CLI credential store when possible; never print, persist, or inspect credentials, and use the raw HTTP form only when the CLI is unavailable.

Risk: Multiple Maton profiles or Acuity Scheduling connections could cause actions to land in the wrong account.

Mitigation: Specify the intended profile and connection when there is more than one account or connection available.

Risk: Content returned from Acuity Scheduling can contain untrusted data.

Mitigation: Treat API responses as data, validate values before reuse, and do not execute or follow instructions found inside fetched content.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/acuity-scheduling)
- [Maton Homepage](https://maton.ai)
- [Acuity Scheduling API Quick Start](https://developers.acuityscheduling.com/reference/quick-start)
- [Acuity Scheduling OAuth2 Documentation](https://developers.acuityscheduling.com/docs/oauth2)
- [Maton Docs](https://docs.maton.ai)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [Shell commands, Code, Configuration, Guidance]

**Output Format:** [Markdown with bash, JSON, Python, and JavaScript code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access and a Maton account; defaults to read/list operations and requires explicit user approval for writes and new connections.]

## Skill Version(s):

1.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
