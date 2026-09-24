## Description:

JotForm API integration with managed OAuth for creating forms, managing submissions, and accessing form data through Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to connect a JotForm account through Maton, inspect form data, manage submissions, and perform approved form or webhook operations. It also guides approved hosted functions and triggers when users need ongoing JotForm automation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: JotForm write calls, webhooks, hosted functions, and triggers can modify data or create ongoing forwarding of form submissions.

Mitigation: Review the exact operation and require explicit user approval before any write, webhook, function, or trigger is created or run.

Risk: API keys are long-lived credentials and can be exposed through environment variables or copied into raw HTTP workflows.

Mitigation: Prefer OAuth login through Maton, store credentials in the operating system credential store, and use raw API-key HTTP only when the CLI cannot be installed.

Risk: Automations can keep running after the original task and continue using the connected JotForm account.

Mitigation: Delete unused connections, functions, triggers, and destinations when the task is complete.

Risk: Form submissions may contain personal or business-sensitive data.

Mitigation: Read only the fields required for the task and avoid dumping raw responses into logs, files, or shared surfaces unless the user asks for that output.

## Reference(s):

- [JotForm ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/jotform)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [JotForm API Overview](https://api.jotform.com/docs/)
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

**Output Format:** [Markdown with inline shell commands, code examples, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce authenticated API call guidance and automation setup steps; users must approve writes, new connections, webhooks, functions, and triggers.]

## Skill Version(s):

1.2.7 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
