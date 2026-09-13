## Description:

Basecamp API integration with managed OAuth for managing projects, to-dos, messages, schedules, documents, and team collaboration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to work with Basecamp through a Maton-managed connection for project, to-do, message, schedule, document, and collaboration workflows. The skill defaults to read/list operations and requires user confirmation for writes, new connections, hosted functions, triggers, and persistent destinations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authenticated Basecamp access can expose or modify project, message, schedule, document, and collaboration data available to the authorized connection.

Mitigation: Prefer OAuth, confirm the exact account and connection before use, default to read/list operations, and require explicit approval before any write.

Risk: Hosted functions, triggers, and destinations can become persistent automation that continues running or forwarding events after setup.

Mitigation: Create or update automation only after clear approval, disclose destination host and payload scope, prefer platform destinations, and remove functions or destinations when no longer needed.

Risk: Raw API keys are long-lived credentials and can be exposed through environment variables, logs, or copied commands.

Mitigation: Use OAuth and the operating system credential store where possible; avoid raw API keys unless necessary and rotate any key that was printed, committed, or pasted.

## Reference(s):

- [ClawHub Basecamp Skill](https://clawhub.ai/byungkyu/skills/basecamp)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Basecamp 4 API Documentation](https://github.com/basecamp/bc3-api)
- [Basecamp Authentication Guide](https://github.com/basecamp/bc3-api/blob/master/sections/authentication.md)
- [Basecamp API Reference](https://github.com/basecamp/bc3-api#endpoints)
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

**Output Format:** [Markdown guidance with inline shell commands, code examples, JSON snippets, and API endpoint references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and an authorized Basecamp connection; writes and persistent automation require explicit user approval.]

## Skill Version(s):

1.2.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
