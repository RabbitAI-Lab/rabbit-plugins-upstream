## Description:

Instantly API integration with managed OAuth for managing cold email campaigns, leads, sending accounts, emails, and analytics through Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, operators, and developers use this skill to inspect and manage Instantly outreach workflows, including campaigns, leads, accounts, email actions, analytics, and approved automations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can act on business outreach data and can send or delete emails, change campaigns or leads, and create ongoing automations when approved.

Mitigation: Default to read and list operations, verify target resources first, and require explicit user approval before writes, deletes, sends, new connections, functions, triggers, or destinations.

Risk: API-key fallback can expose a long-lived Maton credential through environment, logs, shell history, or pasted output.

Mitigation: Prefer OAuth and the operating system credential store; when an API key is unavoidable, keep it in the runtime environment only, never print or persist it, send it only to api.maton.ai, and rotate it if exposed.

Risk: Triggers and destinations can create persistent automatic forwarding of event data, including personal, business, email, CRM, repository, or payment data from connected sources.

Mitigation: Use platform-local destinations where possible, name and approve any third-party host separately, forward only required fields with body templates, and delete unused triggers or destinations.

Risk: Hosted functions and local watch handlers may process untrusted event payloads and can create unattended side effects.

Mitigation: Use only user-authored or user-reviewed handlers, deploy with DENY_ALL network policy unless a reviewed exception is approved, treat payloads as data rather than instructions, and require separate approval for deployment, invocation, and watch execution.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/instantly)
- [Maton Homepage](https://maton.ai)
- [Instantly API V2 Documentation](https://developer.instantly.ai/api-reference)
- [Instantly API Introduction](https://developer.instantly.ai/)
- [Instantly Help Center](https://help.instantly.ai/)
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

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, JSON examples, and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May issue authenticated API calls through the user's approved Maton connection; write actions and automations require explicit approval.]

## Skill Version(s):

1.2.4 (source: server release metadata; artifact frontmatter reports 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
