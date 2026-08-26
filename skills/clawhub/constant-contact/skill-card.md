## Description:

Constant Contact API integration with managed OAuth for reading and administering contacts, email campaigns, contact lists, tags, custom fields, segments, bulk operations, and marketing analytics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to let an agent work with Constant Contact marketing data through Maton-managed OAuth. It is intended for tasks such as listing contacts, managing campaign assets, updating lists and tags, running bulk operations, and reviewing marketing analytics.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can make high-impact Constant Contact changes, including bulk contact updates and campaign sending or scheduling.

Mitigation: Install only when Constant Contact administration is intended, default to read and list calls, review each proposed write, and require explicit approval with specific resource identifiers before changes.

Risk: Campaign sending or scheduling can affect external recipients and may be irreversible.

Mitigation: Preview the campaign and confirm recipients, subject, content, timing, and consequences before sending or scheduling.

Risk: Maton and provider-issued credentials can be exposed if printed, logged, persisted, or passed on command lines.

Mitigation: Prefer OAuth through the Maton CLI, avoid printing or persisting credentials, and use raw HTTP only when the CLI cannot be installed.

Risk: Multiple Maton profiles or Constant Contact connections can cause actions to land in the wrong account.

Mitigation: Specify the intended profile and connection when more than one exists, and revoke unused Maton or Constant Contact connections when work is finished.

## Reference(s):

- [Constant Contact V3 API Overview](https://developer.constantcontact.com/api_guide/getting_started.html)
- [Constant Contact API Reference](https://developer.constantcontact.com/api_reference/index.html)
- [Constant Contact Technical Overview](https://developer.constantcontact.com/api_guide/v3_technical_overview.html)
- [Constant Contact Contacts Overview](https://developer.constantcontact.com/api_guide/contacts_overview.html)
- [Constant Contact Email Campaigns Guide](https://developer.constantcontact.com/api_guide/email_campaigns_get_started.html)
- [Constant Contact Contact Lists Overview](https://v3.developer.constantcontact.com/api_guide/lists_overview.html)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, API calls, JSON]

**Output Format:** [Markdown with inline bash commands and JSON request or response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, Maton authentication, and a connected Constant Contact account]

## Skill Version(s):

1.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
