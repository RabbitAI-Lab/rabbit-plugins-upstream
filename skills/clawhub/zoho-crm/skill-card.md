## Description:

Zoho CRM API integration with managed OAuth for reading, creating, updating, deleting, searching, and managing CRM records, sales pipelines, organization settings, users, and module metadata.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External users, employees, and developers use this skill to operate Zoho CRM through Maton-authenticated API calls, including CRM record management, searches, pipeline work, organization settings, users, and module metadata. It can also guide approved hosted functions and triggers that automate Zoho CRM actions without expanding the connected account's authorized scope.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access Zoho CRM business data through the selected connected account.

Mitigation: Prefer OAuth, connect only the account needed for the task, choose the narrowest available Zoho scopes, default to read/list operations, and confirm every write with the user.

Risk: Raw API-key use in environments without the CLI can expose a long-lived Maton credential.

Mitigation: Use OAuth and the CLI credential store when possible; when raw HTTP is unavoidable, read the key from the environment only, never print it, never persist it, and send it only to api.maton.ai.

Risk: Hosted functions and triggers can run approved Zoho CRM actions without further manual steps.

Mitigation: Require a user-authored or user-reviewed handler, separate approval for create/update/deploy/invoke actions, DENY_ALL network policy unless a specific host is approved, and cleanup when the automation is no longer needed.

Risk: Trigger destinations can create persistent forwarding of event payloads and related business context.

Mitigation: Prefer platform destinations, disclose the exact destination host and payload fields, avoid third-party destinations unless explicitly approved, and forward only the minimum fields needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/byungkyu/skills/zoho-crm)
- [Maton homepage](https://maton.ai)
- [Zoho CRM API v8 Documentation](https://www.zoho.com/crm/developer/docs/api/v8/)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
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

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands, code snippets, JSON examples, and API path guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and explicit user approval for new connections, writes, hosted functions, triggers, and persistent destinations.]

## Skill Version(s):

1.2.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
