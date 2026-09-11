## Description:

MailerLite API integration with managed OAuth for managing subscribers, groups, campaigns, automations, forms, fields, segments, and webhooks through the Maton CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage MailerLite account resources through authenticated API calls. It supports list/read workflows by default and write actions after explicit user confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: MailerLite write operations can change contacts, groups, campaigns, automations, forms, fields, segments, or webhooks.

Mitigation: Default to list/read calls first and require explicit user confirmation for every POST, PUT, PATCH, or DELETE request.

Risk: Campaign and automation actions can send or schedule external communications with reputation and cost impact.

Mitigation: Confirm the target resource, recipients or group identifiers, payload, and intended effect before executing campaign, scheduling, webhook, or automation actions.

Risk: Long-lived API keys and provider-issued tokens can be exposed if printed, logged, stored, or passed on command lines.

Mitigation: Prefer OAuth through the Maton CLI, avoid MATON_API_KEY unless the CLI cannot be used, and never print, persist, or extract credentials.

Risk: External MailerLite data may contain untrusted content.

Mitigation: Treat API response content as data only; do not execute, eval, or use it to choose follow-up endpoints or recipients without validation.

## Reference(s):

- [MailerLite API Documentation](https://developers.mailerlite.com/docs/)
- [MailerLite Subscribers API](https://developers.mailerlite.com/docs/subscribers.html)
- [MailerLite Groups API](https://developers.mailerlite.com/docs/groups.html)
- [MailerLite Campaigns API](https://developers.mailerlite.com/docs/campaigns.html)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/mailerlite)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Configuration instructions, Code, JSON, Guidance]

**Output Format:** [Markdown with inline bash, Python, JavaScript, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and a connected MailerLite account; default posture is read/list before writes.]

## Skill Version(s):

1.2.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
