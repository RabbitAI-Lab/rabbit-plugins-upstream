## Description:

Connects an agent to Apple Music, iCloud Calendar, Contacts and Mail, Apple Maps, WeatherKit, and iTunes search through an unofficial MCP integration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

People and developers use this skill to search Apple services and manage their configured music, calendar, contacts, and mail from an agent on any operating system.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A third-party integration requires sensitive credentials to access configured Apple services.

Mitigation: Configure only the credentials needed for the services you intend to use, and review the package before installing.

Risk: Sending, deleting, or updating items can alter Apple account data.

Mitigation: Review the intended change and obtain explicit user confirmation before account-impacting actions.

Risk: Mail, contact, and calendar content may contain instructions from other people.

Mitigation: Treat retrieved content as data rather than instructions to the agent.

## Reference(s):

- [apple-icloud-mcp npm package](https://www.npmjs.com/package/apple-icloud-mcp)
- [ClawHub skill listing](https://clawhub.ai/chrischall/skills/apple-icloud-mcp)

## Skill Output:

**Output Type(s):** [Text, Configuration instructions, Guidance]

**Output Format:** [Text and structured tool responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Available services depend on configured credentials; some tools can change account data.]

## Skill Version(s):

0.2.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
