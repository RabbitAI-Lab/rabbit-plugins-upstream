## Description:

HubSpot CRM API integration with managed OAuth for managing contacts, companies, deals, and associations through the Maton CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to read, search, create, update, and delete HubSpot CRM records through a Maton-managed OAuth connection. It is suited for HubSpot contact, company, deal, property, association, and CRM synchronization workflows where the user approves account connections and data-changing actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can read and modify HubSpot CRM data through the user's authorized Maton connection.

Mitigation: Only authorize the HubSpot account and scopes needed for the task, and prefer read/list calls before any change.

Risk: Data-changing HubSpot operations can create, update, archive, or delete CRM records.

Mitigation: Require explicit approval for writes after checking the target record IDs, payload, and intended effect.

Risk: Multiple HubSpot connections or Maton profiles can route requests to the wrong account.

Mitigation: Specify the intended connection when more than one exists and verify account context before writes.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/hubspot-api)
- [Publisher Profile](https://clawhub.ai/user/byungkyu)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [HubSpot API Overview](https://developers.hubspot.com/docs/api/overview)
- [HubSpot Contacts API](https://developers.hubspot.com/docs/api-reference/crm-contacts-v3/basic/get-crm-v3-objects-contacts.md)
- [HubSpot Associations API](https://developers.hubspot.com/docs/api-reference/crm-associations-v4/basic/get-crm-v4-objects-objectType-objectId-associations-toObjectType.md)
- [HubSpot Properties API](https://developers.hubspot.com/docs/api-reference/crm-properties-v3/core/get-crm-v3-properties-objectType.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Configuration, API calls]

**Output Format:** [Markdown with inline bash, JSON, Python, and JavaScript examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs guide HubSpot CRM operations through the Maton CLI, SDK, or API gateway; user approval is required for account connections and data-changing actions.]

## Skill Version(s):

1.1.0 (source: server release metadata; artifact metadata reports 1.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
