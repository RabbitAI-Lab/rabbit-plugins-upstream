## Description:

Brevo API integration with managed OAuth for email marketing, transactional emails, SMS, contacts, CRM, campaigns, lists, and templates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to make authenticated Brevo API calls through Maton for account lookup, contact and list management, templates, senders, transactional email, SMS, and campaigns. It is intended for read-first workflows with explicit user approval before creating connections or making write calls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Maton or provider-issued credentials could be exposed through logs, files, command arguments, or copied output.

Mitigation: Prefer OAuth, let the CLI or SDK credential store handle tokens, avoid printing or persisting secrets, and rotate any key that was exposed.

Risk: Write operations can send messages, change contacts or campaigns, delete resources, or trigger downstream automation.

Mitigation: Default to read and list calls, then require explicit user approval with the target resource, payload, and intended effect before POST, PUT, PATCH, or DELETE.

Risk: Calls may affect the wrong Brevo account when multiple Maton profiles or Brevo connections exist.

Mitigation: Verify the active Maton account and specify the intended connection or profile before making account-specific or write calls.

Risk: Brevo API responses and webhook content can contain untrusted text that attempts to steer the agent.

Mitigation: Treat returned content as data, validate it before reuse, and do not execute or interpolate it into shell commands or follow-up requests.

## Reference(s):

- [Brevo API Overview](https://developers.brevo.com/)
- [Brevo API Key Concepts](https://developers.brevo.com/docs/how-it-works)
- [Brevo OAuth 2.0](https://developers.brevo.com/docs/integrating-oauth-20-to-your-solution)
- [Manage Contacts](https://developers.brevo.com/docs/synchronise-contact-lists)
- [Send Transactional Email](https://developers.brevo.com/docs/send-a-transactional-email)
- [Maton](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [text, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline bash, JSON, Python, and JavaScript examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs can include Maton CLI calls, SDK examples, raw HTTPS examples for constrained environments, and Brevo API response summaries.]

## Skill Version(s):

1.2.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
