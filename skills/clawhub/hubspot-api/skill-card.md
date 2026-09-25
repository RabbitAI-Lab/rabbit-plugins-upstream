## Description:

Helps agents manage HubSpot CRM records and set up approved CRM automations through a Maton connection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Sales teams and developers use this skill to find and manage HubSpot contacts, companies, deals, and associations, and to configure approved CRM event workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The connected account may grant access to more HubSpot data than the current CRM task needs.

Mitigation: Prefer OAuth and approve only the needed connection and scopes.

Risk: Writes or deletions can change or remove live CRM records.

Mitigation: Review the target and exact change, then obtain explicit approval before each action.

Risk: Event triggers and destinations can continue forwarding CRM events after setup.

Mitigation: Review destinations before enabling them, and disable triggers when they are no longer needed.

## Reference(s):

- [HubSpot skill on ClawHub](https://clawhub.ai/byungkyu/skills/hubspot-api)
- [Maton](https://maton.ai)
- [HubSpot API overview](https://developers.hubspot.com/docs/api/overview)
- [Maton documentation](https://docs.maton.ai)
- [HubSpot trigger reference](references/hubspot/triggers.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code]

**Output Format:** [Markdown with shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

1.2.7 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
