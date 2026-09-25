## Description:

Google Sheets API integration with managed OAuth for reading and writing spreadsheet data, creating sheets, applying formatting, managing ranges, and configuring approved Maton automations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external users, developers, and operations teams use this skill to let an agent read, update, format, and manage Google Sheets through a Maton-connected account. It is suited for spreadsheet workflows that need authenticated API calls, explicit write approval, and optional scheduled or event-driven automation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access and modify spreadsheet data through the user's Maton-connected Google Sheets account.

Mitigation: Use read and list operations first, require explicit user approval for writes and new connections, and scope OAuth authorization to the specific spreadsheet, sheet, or range needed.

Risk: Hosted functions, triggers, and destinations can continue running or forwarding data after setup.

Mitigation: Create automation only after separate approval, disclose the function, destination host, payload fields, schedule or event source, and remove unused functions, triggers, or destinations.

Risk: Using a raw Maton API key instead of the CLI can expose a long-lived credential through environment variables, logs, shell history, or child processes.

Mitigation: Prefer OAuth through the Maton CLI, never print or persist API keys, send them only to api.maton.ai, and rotate the key if it was exposed.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/google-sheets)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Google Sheets API Overview](https://developers.google.com/workspace/sheets/api/reference/rest)
- [Google Sheets Batch Update Request Types](https://developers.google.com/workspace/sheets/api/reference/rest/v4/spreadsheets/request)
- [Time Trigger Reference](references/time/triggers.md)
- [Gmail Trigger Reference](references/google-mail/triggers.md)
- [GitHub Trigger Reference](references/github/triggers.md)
- [Slack Trigger Reference](references/slack/triggers.md)
- [Stripe Trigger Reference](references/stripe/triggers.md)
- [HubSpot Trigger Reference](references/hubspot/triggers.md)
- [Linear Trigger Reference](references/linear/triggers.md)
- [Notion Trigger Reference](references/notion/triggers.md)
- [Calendly Trigger Reference](references/calendly/triggers.md)

## Skill Output:

**Output Type(s):** [guidance, shell commands, code, configuration, markdown]

**Output Format:** [Markdown guidance with inline shell commands, JSON examples, Python snippets, and configuration instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands operate through Maton OAuth or, only when the CLI is unavailable, a Maton API key.]

## Skill Version(s):

1.2.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
