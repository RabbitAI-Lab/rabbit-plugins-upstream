## Description:

Guides agents in using the Mailtrap Contacts API or UI to add, update, bulk import, list, segment, and sync marketing contacts, custom fields, and custom events.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mailtrap](https://clawhub.ai/user/mailtrap)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, marketers, and automation builders use this skill to manage Mailtrap marketing contacts, synchronize audiences from CRMs or data warehouses, and prepare contact lists, segments, custom fields, and custom events for campaigns.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A Mailtrap token with excessive permissions could allow unintended contact changes.

Mitigation: Use a properly scoped Mailtrap token and verify the account ID before running API commands.

Risk: Bulk import or delete operations could modify large contact sets.

Mitigation: Review bulk operations carefully before execution.

Risk: Contact data could be sent to the Mailtrap API without proper authorization.

Mitigation: Only process contact data that the user is authorized to handle.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/mailtrap/skills/managing-contacts)
- [Mailtrap Contacts OpenAPI spec](https://github.com/mailtrap/mailtrap-openapi/blob/main/specs/contacts.openapi.yml)
- [Mailtrap Contacts API documentation](https://docs.mailtrap.io/developers/promotional/contacts/contacts.md)
- [Mailtrap bulk import documentation](https://docs.mailtrap.io/developers/promotional/contacts/bulk-import.md)
- [Mailtrap import contacts documentation](https://docs.mailtrap.io/email-marketing/contacts/import-contacts.md)
- [Mailtrap custom fields documentation](https://docs.mailtrap.io/email-marketing/contacts/custom-fields.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, API request examples, Configuration instructions]

**Output Format:** [Markdown with inline tables and bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses Mailtrap account IDs and bearer tokens supplied by the user or agent environment.]

## Skill Version(s):

1.0.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
