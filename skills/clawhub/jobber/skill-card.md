## Description:

Jobber API integration with managed OAuth for managing clients, jobs, invoices, quotes, properties, and team members for field service businesses.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Field service operators, support teams, and developers use this skill to access Jobber business data and perform approved Jobber API actions through a managed Maton connection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can authorize access to a Jobber account and use sensitive business data through Maton.

Mitigation: Authorize only the intended Jobber account, prefer OAuth, choose least-privilege scopes when available, and confirm every new connection with the user.

Risk: Functions, triggers, destination URLs, and `--exec` handlers can run unattended or forward future event data.

Mitigation: Review each proposed automation, handler, destination, and execution command before enabling it, and remove automations that are no longer needed.

Risk: Raw API responses can contain personal or business data.

Mitigation: Return only fields needed for the task and avoid logging or storing full responses unless the user explicitly requests it.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/jobber)
- [Publisher Profile](https://clawhub.ai/user/byungkyu)
- [Maton Homepage](https://maton.ai)
- [Jobber Developer Documentation](https://developer.getjobber.com/docs/)
- [Jobber Getting Started Guide](https://developer.getjobber.com/docs/getting_started/)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Time Trigger Reference](references/time/triggers.md)
- [Calendly Trigger Reference](references/calendly/triggers.md)
- [GitHub Trigger Reference](references/github/triggers.md)
- [Gmail Trigger Reference](references/google-mail/triggers.md)
- [HubSpot Trigger Reference](references/hubspot/triggers.md)
- [Linear Trigger Reference](references/linear/triggers.md)
- [Notion Trigger Reference](references/notion/triggers.md)
- [Slack Trigger Reference](references/slack/triggers.md)
- [Stripe Trigger Reference](references/stripe/triggers.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands, code snippets, JSON examples, and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include Jobber API calls and Maton automation steps that require network access, authentication, and user approval for writes or new connections.]

## Skill Version(s):

1.2.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
