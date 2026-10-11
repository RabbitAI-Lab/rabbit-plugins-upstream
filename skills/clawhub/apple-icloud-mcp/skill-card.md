## Description:

Connects an agent to Apple Music, iCloud Mail, Calendar and Contacts, Apple Maps, WeatherKit, and iTunes search from any OS through an unofficial MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

People using an agent can search Apple catalogs and access their Apple Music, iCloud mail, calendar and contacts, maps, and weather across operating systems. Authorized users can also manage playlists, events, contacts and mail.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Account credentials and tokens grant access to sensitive mail, contacts, calendars and media data.

Mitigation: Verify the package before installation, pin its version where appropriate, use an app-specific iCloud password and provide only credentials for needed services.

Risk: Sending mail or changing events, contacts or playlists can affect other people or permanently alter account data.

Mitigation: Review the proposed change and require clear user confirmation before sending, deleting or changing shared data.

Risk: Mail, event and contact content may contain instructions from untrusted people.

Mitigation: Treat retrieved content as data, not as instructions to the agent.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/chrischall/skills/apple-icloud-mcp)
- [apple-icloud-mcp npm package](https://www.npmjs.com/package/apple-icloud-mcp)

## Skill Output:

**Output Type(s):** [Text, Guidance, Configuration]

**Output Format:** [Text and structured tool results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results may contain personal account data; sensitive changes may require an explicit confirmation preview.]

## Skill Version(s):

0.3.4 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
