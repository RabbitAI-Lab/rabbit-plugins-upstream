## Description:

Twenty CRM integrates agent workflows with Twenty CRM through managed Maton authentication to read and manage companies, people, opportunities, notes, tasks, workflows, and workspace members.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, operations teams, and developers use this skill to inspect and update Twenty CRM records and to set up approved Maton-based automations around CRM workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: CRM write operations and automations can change live business records, workflows, or workspace state.

Mitigation: Default to read/list operations, verify target records first, and require explicit user approval for every POST, PUT, PATCH, DELETE, function, trigger, or destination.

Risk: Long-lived API keys can be exposed through environment variables, logs, shell history, or copied output.

Mitigation: Prefer OAuth through the documented Maton CLI, use API keys only where the CLI cannot be installed, and never print, persist, or pass credentials on command lines.

Risk: Triggers and destinations can create persistent automated data flows involving CRM or third-party event data.

Mitigation: Connect only the minimum needed accounts and scopes, keep destinations on approved Maton-controlled routes when possible, and review destination host, payload fields, cadence, and credential handling before approval.

## Reference(s):

- [ClawHub Twenty CRM skill page](https://clawhub.ai/byungkyu/skills/twenty)
- [Maton homepage](https://maton.ai)
- [Twenty API Documentation](https://docs.twenty.com/developers/extend/api)
- [Twenty GitHub](https://github.com/twentyhq/twenty)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [API Gateway Skill](https://clawhub.ai/byungkyu/api-gateway)
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

**Output Type(s):** [guidance, shell commands, code, configuration]

**Output Format:** [Markdown guidance with bash, JSON, Python, and JavaScript snippets.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and user approval for CRM writes, new connections, hosted functions, triggers, and destinations.]

## Skill Version(s):

1.2.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
