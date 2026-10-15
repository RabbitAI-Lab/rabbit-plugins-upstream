## Description:

Helps agents work with OurFamilyWizard co-parenting messages, calendars, expenses, and journal entries through an MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

People using OurFamilyWizard and their assistants can check co-parenting records, draft or send messages, manage calendar events and expenses, and review journal entries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The connected server can access sensitive co-parenting messages, calendar entries, expenses, journal entries, attachments, and profile details.

Mitigation: Review access before installation and connect only accounts whose records you are comfortable sharing with the server.

Risk: Example setup stores the OFW password in project configuration or an .env file, where it could be exposed or committed.

Mitigation: Use a protected secret manager or tightly permissioned user-only configuration instead of project-local or committed credentials.

Risk: Sending messages, deleting records, sharing uploads, and changing events or expenses can affect other people or permanently change records.

Mitigation: Show the intended action and obtain explicit user approval before each send, delete, shared upload, event change, or expense change.

Risk: Some reads can mark messages as read or notifications as seen.

Mitigation: Warn users before reads that could change read or seen status, and avoid fetching them silently.

## Reference(s):

- [OFW skill on ClawHub](https://clawhub.ai/chrischall/skills/ofw)
- [ofw-mcp package on npm](https://www.npmjs.com/package/ofw-mcp)

## Skill Output:

**Output Type(s):** [Text, Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with configuration and command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can guide agent use of OFW tools to retrieve or change account records.]

## Skill Version(s):

2.20.4 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
