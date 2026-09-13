## Description:

Jobber API integration with managed OAuth for managing clients, jobs, invoices, quotes, properties, and team members for field service businesses.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to access Jobber through Maton-managed OAuth, inspect account and scheduling data, and create or update clients, jobs, invoices, quotes, properties, and team members after explicit approval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses Maton credentials and may use a long-lived API key where the CLI cannot be installed.

Mitigation: Prefer OAuth through the Maton CLI, never print or persist credentials, and send API keys only to api.maton.ai.

Risk: Write operations can modify Jobber business records such as clients, jobs, invoices, quotes, properties, and team members.

Mitigation: Default to read and list calls, verify identifiers and account context first, and obtain explicit approval for every POST, PUT, PATCH, or DELETE operation.

Risk: Hosted functions and triggers can create persistent automations or event forwarding paths.

Mitigation: Approve every function, trigger, and destination separately, keep destinations on Maton-controlled hosts unless the user explicitly approves another host, and delete unused connections or automations.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/jobber)
- [Maton Homepage](https://maton.ai)
- [Jobber Developer Documentation](https://developer.getjobber.com/docs/)
- [Jobber Getting Started Guide](https://developer.getjobber.com/docs/getting_started/)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Calendly Trigger Reference](references/calendly/triggers.md)
- [GitHub Trigger Reference](references/github/triggers.md)
- [Google Mail Trigger Reference](references/google-mail/triggers.md)
- [HubSpot Trigger Reference](references/hubspot/triggers.md)
- [Linear Trigger Reference](references/linear/triggers.md)
- [Notion Trigger Reference](references/notion/triggers.md)
- [Slack Trigger Reference](references/slack/triggers.md)
- [Stripe Trigger Reference](references/stripe/triggers.md)
- [Time Trigger Reference](references/time/triggers.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands, GraphQL JSON payloads, and code snippets.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce Maton CLI commands, raw HTTPS examples, Jobber GraphQL queries or mutations, and approval checklists.]

## Skill Version(s):

1.2.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
