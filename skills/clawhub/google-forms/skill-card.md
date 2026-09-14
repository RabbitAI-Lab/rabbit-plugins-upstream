## Description:

Google Forms API integration with managed OAuth for creating forms, adding questions, and retrieving responses through Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and automation users use this skill to connect an authenticated Google Forms account through Maton, create or update forms, add questions, retrieve form metadata and responses, and optionally run user-approved hosted automations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses Maton as the gateway for Google Forms and requires OAuth approval or a Maton API key.

Mitigation: Confirm the user is comfortable approving the connection, prefer OAuth with the platform credential store, select only required scopes, and avoid exporting long-lived API keys unless the CLI cannot be installed.

Risk: Write operations, connection creation, hosted functions, triggers, and destinations can change resources or keep running after setup.

Mitigation: Default to read and list calls, require explicit approval for each write or automation step, summarize destination, data fields, event source or schedule, and cleanup plan before creation, and delete unneeded functions or triggers when the task is complete.

Risk: Persistent destinations or local event handlers can forward or process third-party event data continuously.

Mitigation: Keep Google Forms automations on Maton-hosted functions where possible, use DENY_ALL network policy for hosted functions, do not forward Google Forms-derived data to destination payloads, and avoid local --exec handlers unless the user supplies and approves the handler.

## Reference(s):

- [Google Forms API Overview](https://developers.google.com/workspace/forms/api/reference/rest)
- [Get Form](https://developers.google.com/workspace/forms/api/reference/rest/v1/forms/get)
- [Create Form](https://developers.google.com/workspace/forms/api/reference/rest/v1/forms/create)
- [Batch Update](https://developers.google.com/workspace/forms/api/reference/rest/v1/forms/batchUpdate)
- [List Responses](https://developers.google.com/workspace/forms/api/reference/rest/v1/forms.responses/list)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/google-forms)
- [Time Trigger Reference](references/time/triggers.md)
- [Gmail Trigger Reference](references/google-mail/triggers.md)
- [GitHub Trigger Reference](references/github/triggers.md)
- [Slack Trigger Reference](references/slack/triggers.md)
- [Stripe Trigger Reference](references/stripe/triggers.md)
- [Calendly Trigger Reference](references/calendly/triggers.md)
- [HubSpot Trigger Reference](references/hubspot/triggers.md)
- [Linear Trigger Reference](references/linear/triggers.md)
- [Notion Trigger Reference](references/notion/triggers.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, JSON examples, Python code snippets, and API request paths.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are task-specific agent instructions and commands; API responses may contain user data and should be minimized to the fields needed for the task.]

## Skill Version(s):

1.2.2 (source: server release evidence; artifact frontmatter metadata.version is 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
