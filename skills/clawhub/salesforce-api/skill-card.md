## Description:

Connects an agent to Salesforce CRM through Maton to query records, manage approved changes, and set up approved automations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Salesforce administrators and developers use this skill to inspect CRM data, make explicitly approved record changes, and configure approved scheduled or event-driven workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: CRM writes or batch operations can alter or delete records.

Mitigation: Use least-privilege, preferably read-only or sandbox access; verify the connection and exact records, then obtain explicit approval before changes.

Risk: Automations can repeatedly act on CRM data or forward it to a destination.

Mitigation: Review the function, schedule or event source, destination, and data flow; approve only the specific ongoing action and destination needed.

## Reference(s):

- [Salesforce skill release](https://clawhub.ai/byungkyu/skills/salesforce-api)
- [Maton](https://maton.ai)
- [Salesforce REST API Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/intro_rest.htm)
- [Maton documentation](https://docs.maton.ai)
- [Scheduled trigger reference](references/time/triggers.md)

## Skill Output:

**Output Type(s):** [Text, API calls, Code, Shell commands, Configuration guidance]

**Output Format:** [Text or Markdown with commands and structured CRM results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [CRM responses can contain sensitive customer information; show only fields needed for the task.]

## Skill Version(s):

1.2.7 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
