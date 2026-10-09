## Description:

Connects agents to Apple Music, iCloud Calendar, Contacts and Mail, Apple Maps, WeatherKit, and iTunes search through an unofficial MCP integration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

People and developers use this skill to ask an agent to search Apple catalogs, check weather and directions, and access or manage their configured Apple Music and iCloud services from any OS.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Configured Apple service credentials grant access to sensitive mail, calendar, contacts and music data.

Mitigation: Configure only needed services with service-specific credentials and run the healthcheck before use.

Risk: Sending mail or editing and deleting account content can have unintended effects.

Mitigation: Review previews and obtain explicit user confirmation before sending mail or making destructive changes.

Risk: Broad requests can target the wrong service when similar integrations are installed.

Mitigation: Confirm the intended integration and account before acting on ambiguous requests.

## Reference(s):

- [ClawHub release](https://clawhub.ai/chrischall/skills/apple-icloud-mcp)
- [apple-icloud-mcp npm package](https://www.npmjs.com/package/apple-icloud-mcp)

## Skill Output:

**Output Type(s):** [Text, Markdown, Configuration instructions, Guidance]

**Output Format:** [Text or Markdown with structured MCP tool results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on the Apple services and credentials configured by the user.]

## Skill Version(s):

0.3.3 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
