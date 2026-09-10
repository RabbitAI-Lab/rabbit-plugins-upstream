## Description:

HubSpot API integration with managed OAuth for CRM contacts, companies, deals, associations, and properties, with a Maton API passthrough that can reach any HubSpot API path authorized for the connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, operators, and developers use this skill to read, search, create, update, and delete HubSpot CRM records through Maton-managed authentication. Non-CRM HubSpot API access should be used only when the user explicitly names and approves the endpoint.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The generic Maton API passthrough can reach more HubSpot APIs than the documented CRM surface when the connected account authorizes them.

Mitigation: Use the narrowest HubSpot scopes available, prefer read-only access, and require the user to name and approve any non-CRM endpoint before use.

Risk: Write operations can create, modify, delete, publish, message, or trigger automation depending on the HubSpot endpoint used.

Mitigation: Default to read and list operations, verify the target connection and identifiers, and confirm the exact payload and intended effect before any POST, PUT, PATCH, or DELETE request.

Risk: Maton API keys or provider-issued tokens can be exposed through logs, shell history, files, or command arguments.

Mitigation: Prefer OAuth through the Maton CLI, keep keys in approved secret stores or process memory only, never print or persist credentials, and send Maton credentials only to api.maton.ai.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/hubspot-api)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [HubSpot API Overview](https://developers.hubspot.com/docs/api/overview)
- [HubSpot Contacts API](https://developers.hubspot.com/docs/api-reference/crm-contacts-v3/basic/get-crm-v3-objects-contacts.md)
- [HubSpot Companies API](https://developers.hubspot.com/docs/api-reference/crm-companies-v3/basic/get-crm-v3-objects-companies.md)
- [HubSpot Deals API](https://developers.hubspot.com/docs/api-reference/crm-deals-v3/basic/get-crm-v3-objects-0-3.md)
- [HubSpot Associations API](https://developers.hubspot.com/docs/api-reference/crm-associations-v4/basic/get-crm-v4-objects-objectType-objectId-associations-toObjectType.md)
- [HubSpot Properties API](https://developers.hubspot.com/docs/api-reference/crm-properties-v3/core/get-crm-v3-properties-objectType.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API Calls, Code, Configuration]

**Output Format:** [Markdown with inline bash, JSON, Python, and JavaScript code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce HubSpot API responses containing CRM or account data; responses should be minimized to the fields needed for the task.]

## Skill Version(s):

1.2.1 (source: server release metadata; frontmatter reports 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
