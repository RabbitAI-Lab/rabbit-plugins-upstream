## Description:

Connects agents on any OS to Apple Music, iCloud Calendar, Contacts and Mail, Apple Maps, WeatherKit, and iTunes search through an unofficial MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Individuals and developers use this skill to search Apple media and services, review personal calendar, contacts and mail, and make authorized changes to Apple account content.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad access to personal Apple account data and credentials.

Mitigation: Enable only needed services, keep the iCloud app password and Apple Music token secret, and review the package before installation.

Risk: Actions can send mail or change and delete calendar, contacts, and music data.

Mitigation: Require explicit user confirmation before sending mail, deleting data, or changing account content.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/chrischall/skills/apple-icloud-mcp)
- [apple-icloud-mcp npm package](https://www.npmjs.com/package/apple-icloud-mcp)

## Skill Output:

**Output Type(s):** [Text, Guidance, Configuration instructions]

**Output Format:** [Markdown and structured tool responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can return personal account data and perform authorized account changes.]

## Skill Version(s):

0.3.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
