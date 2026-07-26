## Description: <br>
HubSpot CRM API integration with managed OAuth for managing contacts, companies, deals, and associations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[byungkyu](https://clawhub.ai/user/byungkyu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, CRM operators, and agents use this skill to read, create, update, search, and associate HubSpot CRM records through Maton-managed OAuth. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Service credentials and HubSpot account access may expose CRM data if over-permissioned. <br>
Mitigation: Use narrow HubSpot permissions, protect MATON_API_KEY, and review any agent-proposed external actions before approving them. <br>
Risk: Create, update, archive, delete, and batch operations can modify CRM records. <br>
Mitigation: Require explicit user approval for write operations and confirm the target resource, connection, and intended effect before execution. <br>
Risk: Multiple HubSpot connections can route requests to the wrong account. <br>
Mitigation: Specify the intended connection ID when more than one active HubSpot connection exists. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/hubspot-api) <br>
- [HubSpot API Overview](https://developers.hubspot.com/docs/api/overview) <br>
- [HubSpot Contacts API](https://developers.hubspot.com/docs/api-reference/crm-contacts-v3/basic/get-crm-v3-objects-contacts.md) <br>
- [HubSpot Companies API](https://developers.hubspot.com/docs/api-reference/crm-companies-v3/basic/get-crm-v3-objects-companies.md) <br>
- [HubSpot Deals API](https://developers.hubspot.com/docs/api-reference/crm-deals-v3/basic/get-crm-v3-objects-0-3.md) <br>
- [HubSpot Associations API](https://developers.hubspot.com/docs/api-reference/crm-associations-v4/basic/get-crm-v4-objects-objectType-objectId-associations-toObjectType.md) <br>
- [HubSpot Properties API](https://developers.hubspot.com/docs/api-reference/crm-properties-v3/core/get-crm-v3-properties-objectType.md) <br>
- [HubSpot CRM Search Reference](https://developers.hubspot.com/docs/api/crm/search) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell, Python, JavaScript, and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires network access, MATON_API_KEY, and an active HubSpot OAuth connection.] <br>

## Skill Version(s): <br>
1.0.7 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
