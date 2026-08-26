## Description:

Brevo API integration with managed OAuth for email marketing, transactional emails, SMS, contacts, and CRM.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to connect a Brevo account through Maton, inspect account and contact data, manage contacts, lists, templates, campaigns, and send or schedule communications with explicit approval for write actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can send emails or SMS, alter contacts, campaigns, lists, templates, and delete Brevo resources through the connected account.

Mitigation: Use OAuth when possible, verify the intended Brevo connection, and require explicit confirmation before write, send, schedule, or delete actions.

Risk: Ambiguous Maton profiles or Brevo connections can cause an action to affect the wrong account.

Mitigation: Specify the Maton profile and Brevo connection when multiple accounts or connections are available, and confirm target identifiers before making changes.

Risk: Credential exposure can occur if API keys or provider tokens are printed, stored, or passed through shell arguments.

Mitigation: Prefer OAuth-backed CLI authentication, avoid printing or persisting credentials, and use stdin-based raw HTTP fallback only when the CLI cannot be installed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/byungkyu/skills/brevo-api)
- [Maton homepage](https://maton.ai)
- [Brevo API Overview](https://developers.brevo.com/)
- [Brevo API Key Concepts](https://developers.brevo.com/docs/how-it-works)
- [Brevo OAuth 2.0](https://developers.brevo.com/docs/integrating-oauth-20-to-your-solution)
- [Manage Contacts](https://developers.brevo.com/docs/synchronise-contact-lists)
- [Send Transactional Email](https://developers.brevo.com/docs/send-a-transactional-email)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [Shell commands, API calls, Configuration, Guidance]

**Output Format:** [Markdown with inline bash and JSON code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and a valid Brevo connection.]

## Skill Version(s):

1.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
