## Description:

Baserow API integration with managed API key authentication for managing database rows, fields, and tables through Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Agents use this skill to help users read, create, update, delete, filter, and sort Baserow database rows, fields, and tables through an authenticated Maton connection. It is intended for developers, operators, and business users who manage Baserow data or approved automations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can read and modify Baserow database data through a Maton-mediated connection.

Mitigation: Prefer read/list calls first, confirm every write or delete with the user, and scope the Baserow connection to the current task.

Risk: Connection creation and hosted automation can grant ongoing access to user data.

Mitigation: Create connections, functions, triggers, and destinations only after explicit approval, and remove functions or triggers when no longer needed.

Risk: Long-lived credentials or third-party trigger destinations can increase exposure if mishandled.

Mitigation: Prefer OAuth, never print or persist keys, send Maton credentials only to Maton endpoints, and use third-party destinations only when the user explicitly trusts the host.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/byungkyu/skills/baserow-api)
- [Maton homepage](https://maton.ai)
- [Baserow API Documentation](https://baserow.io/api-docs)
- [Baserow Database API](https://baserow.io/user-docs/database-api)
- [Database Tokens](https://baserow.io/user-docs/personal-api-tokens)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Time Trigger Reference](references/time/triggers.md)
- [GitHub Trigger Reference](references/github/triggers.md)
- [Slack Trigger Reference](references/slack/triggers.md)
- [Stripe Trigger Reference](references/stripe/triggers.md)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, code, API calls]

**Output Format:** [Markdown with inline shell commands, JSON examples, and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance emphasizes read/list calls first, explicit approval for writes and automation, scoped connections, and careful credential handling.]

## Skill Version(s):

1.2.8 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
