## Description:

Helps agents search and manage HubSpot CRM contacts, companies, deals, associations, and properties through a user-authorized Maton connection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Teams and developers use this skill to find and update HubSpot CRM records through an authorized connection. With explicit approval, they can also set up HubSpot-related hosted functions and event or scheduled triggers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The authorized connection may grant access beyond CRM or expose personal data.

Mitigation: Review OAuth scopes, prefer narrow read-only access, and return only the CRM fields needed.

Risk: Writes and automation can change records or forward future event data.

Mitigation: Confirm each write or automation step and review trigger destinations before enabling them.

## Reference(s):

- [HubSpot skill release](https://clawhub.ai/byungkyu/skills/hubspot-api)
- [Maton](https://maton.ai)
- [Maton documentation](https://docs.maton.ai)
- [HubSpot API overview](https://developers.hubspot.com/docs/api/overview)
- [HubSpot trigger reference](references/hubspot/triggers.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Code, Configuration guidance]

**Output Format:** [Markdown with commands, code snippets, and CRM result summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include CRM personal data; limit results to the fields needed.]

## Skill Version(s):

1.2.8 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
