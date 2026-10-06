## Description:

Helps an agent access Apple Music, iCloud Calendar, Contacts and Mail, Apple Maps, WeatherKit, and iTunes search through an unofficial MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Users and developers use this skill to search Apple content, check directions and weather, and access or manage their Apple Music and iCloud account data when the required credentials are configured.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The linked third-party MCP package requires sensitive Apple credentials and can access personal account data.

Mitigation: Install only if the account access is intended; store the iCloud app password and Apple Music token as secrets, never commit them, and rotate them if exposed.

Risk: Mail sending, deletion, and other account changes can have unintended consequences.

Mitigation: Require explicit user confirmation before sending mail, deleting records, or changing account data.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/chrischall/skills/apple-icloud-mcp)
- [apple-icloud-mcp npm package](https://www.npmjs.com/package/apple-icloud-mcp)

## Skill Output:

**Output Type(s):** [Text, Guidance, Configuration instructions]

**Output Format:** [Text or Markdown, including MCP setup configuration]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Available services depend on configured credentials; account-changing actions may require confirmation.]

## Skill Version(s):

0.3.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
