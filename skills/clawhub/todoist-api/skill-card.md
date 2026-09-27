## Description:

Todoist API integration with managed OAuth for reading and managing tasks, projects, sections, labels, and comments through Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to connect an authorized Todoist account, inspect Todoist records, and perform approved task, project, section, label, and comment updates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Writes, deletions, connection creation, hosted functions, triggers, and destinations can modify Todoist data or create ongoing automation.

Mitigation: Default to read and list operations; require explicit user approval before any write, deletion, new connection, hosted function, trigger, or destination.

Risk: Todoist records and Maton credentials can expose personal or business data if broad responses are logged or long-lived keys are used carelessly.

Mitigation: Prefer OAuth with the operating system credential store, use raw API keys only when the CLI cannot be installed, and extract only the response fields needed for the task.

Risk: Hosted automation runs under the deploying Maton account and can keep acting after the original request.

Mitigation: Use user-authored or user-reviewed handlers, deploy with DENY_ALL network policy by default, scope triggers narrowly, keep functions private, and delete automation when the task is complete.

## Reference(s):

- [ClawHub Todoist Skill](https://clawhub.ai/byungkyu/skills/todoist-api)
- [Maton Homepage](https://maton.ai)
- [Todoist API v1 Documentation](https://developer.todoist.com/api/v1)
- [Todoist OAuth Documentation](https://developer.todoist.com/guides/#oauth)
- [Todoist Filter Syntax](https://todoist.com/help/articles/introduction-to-filters)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Time Trigger Reference](references/time/triggers.md)
- [Calendly Trigger Reference](references/calendly/triggers.md)
- [Gmail Trigger Reference](references/google-mail/triggers.md)
- [GitHub Trigger Reference](references/github/triggers.md)
- [HubSpot Trigger Reference](references/hubspot/triggers.md)
- [Linear Trigger Reference](references/linear/triggers.md)
- [Notion Trigger Reference](references/notion/triggers.md)
- [Slack Trigger Reference](references/slack/triggers.md)
- [Stripe Trigger Reference](references/stripe/triggers.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Code, Guidance]

**Output Format:** [Markdown guidance with shell commands, JSON examples, and configuration details]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs guide authenticated Todoist API calls, connection management, and approved automation setup through Maton.]

## Skill Version(s):

1.2.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
