## Description:

Zoho CRM API integration with managed OAuth for reading, creating, updating, deleting, searching, and managing CRM records through the Maton CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and CRM operators use this skill to let an agent inspect and manage Zoho CRM leads, contacts, accounts, deals, users, organization details, and module metadata. It supports read-first CRM workflows and user-approved record creation, updates, deletion, search, and bulk operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can read and modify data in a connected Zoho CRM account.

Mitigation: Use OAuth with the narrowest available scopes, confirm the exact account and connection, default to read or list calls, and require explicit approval before create, update, or delete operations.

Risk: Credentials or provider-issued tokens could be exposed if mishandled.

Mitigation: Use Maton-managed OAuth and the operating system credential store; do not print, log, persist, export, or inspect tokens or API keys.

Risk: CRM writes may affect the wrong account or record when multiple Maton profiles or Zoho CRM connections exist.

Mitigation: Specify the intended Maton profile and Zoho CRM connection, verify identifiers with read calls first, and review the payload and intended effect before approving a mutation.

Risk: CRM fields and other API-returned content may contain untrusted instructions.

Mitigation: Treat returned CRM content as data, do not execute or follow instructions found in fetched records, and pass external values as discrete arguments rather than interpolating them into commands.

## Reference(s):

- [Zoho CRM API v8 Documentation](https://www.zoho.com/crm/developer/docs/api/v8/)
- [Zoho CRM Get Records API](https://www.zoho.com/crm/developer/docs/api/v8/get-records.html)
- [Zoho CRM Insert Records API](https://www.zoho.com/crm/developer/docs/api/v8/insert-records.html)
- [Zoho CRM Update Records API](https://www.zoho.com/crm/developer/docs/api/v8/update-records.html)
- [Zoho CRM Delete Records API](https://www.zoho.com/crm/developer/docs/api/v8/delete-records.html)
- [Zoho CRM Search Records API](https://www.zoho.com/crm/developer/docs/api/v8/search-records.html)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API calls, Configuration]

**Output Format:** [Markdown with inline bash and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and a Zoho CRM connection.]

## Skill Version(s):

1.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
