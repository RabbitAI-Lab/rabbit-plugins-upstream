## Description:

Clockify API integration with managed OAuth for tracking time and managing projects, clients, tasks, workspaces, and related automation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Clockify through Maton-managed OAuth: listing and updating time entries, projects, clients, tasks, tags, workspaces, and approved automations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create or use a Maton OAuth connection to a user's Clockify account.

Mitigation: Require explicit user approval before creating a connection, verify the target account and connection ID, and select only the scopes needed for the task.

Risk: Write, delete, function, or trigger actions can change Clockify data or create ongoing automation.

Mitigation: Default to read and list operations; before any change, disclose the exact resource, payload, intended effect, and whether an automation will continue running.

Risk: Using raw HTTP or environment variables can expose long-lived Maton credentials.

Mitigation: Prefer OAuth through the Maton CLI and OS credential store; use raw HTTP only when the CLI cannot be installed and avoid reading or printing credential values.

Risk: Trigger destinations can establish persistent event forwarding.

Mitigation: Create or update destinations only after a separate approval that names the destination host, data fields, delivery persistence, and any credential-bearing headers or body fields.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/byungkyu/skills/clockify)
- [Maton homepage](https://maton.ai)
- [Clockify API Documentation](https://docs.clockify.me/)
- [Clockify Time Entry API Reference](https://docs.clockify.me/#tag/Time-entry)
- [Calendly Trigger Reference](references/calendly/triggers.md)
- [GitHub Trigger Reference](references/github/triggers.md)
- [Gmail Trigger Reference](references/google-mail/triggers.md)
- [HubSpot Trigger Reference](references/hubspot/triggers.md)
- [Linear Trigger Reference](references/linear/triggers.md)
- [Notion Trigger Reference](references/notion/triggers.md)
- [Slack Trigger Reference](references/slack/triggers.md)
- [Stripe Trigger Reference](references/stripe/triggers.md)
- [Time Trigger Reference](references/time/triggers.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands, API paths, JSON examples, and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include Maton CLI commands, Clockify API requests, hosted function examples, and trigger configuration guidance.]

## Skill Version(s):

1.2.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
