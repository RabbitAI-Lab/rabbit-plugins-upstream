## Description:

Constant Contact API integration with managed OAuth for reading and managing contacts, campaigns, lists, tags, custom fields, segments, and marketing analytics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to administer Constant Contact marketing data through Maton-managed OAuth. It supports read workflows by default and write workflows only after explicit user confirmation of the account, resource identifiers, payload, and intended effect.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Write, bulk import/delete, or campaign send/schedule operations can change marketing data or contact external recipients.

Mitigation: Require explicit confirmation of the Constant Contact account, resource IDs, payload, and intended effect before any write or high-impact operation.

Risk: Long-lived API keys or surfaced provider tokens can expose account access.

Mitigation: Prefer OAuth with least-privilege scopes, avoid printing or storing credentials, and rotate any key that was exposed.

Risk: Ambiguous Maton profiles or connections can route a request to the wrong Constant Contact account.

Mitigation: List and verify the active profile and connection before sensitive actions, and specify the target connection when multiple connections exist.

## Reference(s):

- [Constant Contact Skill on ClawHub](https://clawhub.ai/byungkyu/skills/constant-contact)
- [Maton Homepage](https://maton.ai)
- [Constant Contact V3 API Overview](https://developer.constantcontact.com/api_guide/getting_started.html)
- [Constant Contact API Reference](https://developer.constantcontact.com/api_reference/index.html)
- [Constant Contact Technical Overview](https://developer.constantcontact.com/api_guide/v3_technical_overview.html)
- [Constant Contact Contacts Overview](https://developer.constantcontact.com/api_guide/contacts_overview.html)
- [Constant Contact Email Campaigns Guide](https://developer.constantcontact.com/api_guide/email_campaigns_get_started.html)
- [Constant Contact Contact Lists Overview](https://v3.developer.constantcontact.com/api_guide/lists_overview.html)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May generate Constant Contact API requests through the Maton CLI or raw HTTP when the CLI cannot be installed.]

## Skill Version(s):

1.2.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
