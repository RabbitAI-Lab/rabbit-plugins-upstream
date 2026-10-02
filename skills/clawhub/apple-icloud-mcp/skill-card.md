## Description:

Helps an agent use Apple Music, iCloud Calendar, Contacts and Mail, Apple Maps, WeatherKit, and iTunes search from any operating system through an unofficial integration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

People using an agent can search Apple media and places, check weather and personal iCloud information, and manage playlists, calendar events, contacts, or mail when authorized.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Access to sensitive Apple and iCloud account data spans mail, contacts, calendars, and music.

Mitigation: Configure only the credentials needed for the services you intend to use and limit requests to explicit Apple or iCloud tasks.

Risk: The example installation runs an unpinned npm package.

Mitigation: Pin the package to a reviewed version before connecting account credentials.

Risk: Account-changing actions can send mail or alter contacts, calendar events, and playlists.

Mitigation: Review the proposed change and obtain explicit user confirmation before carrying it out.

Risk: Messages, event details, and contact notes may contain untrusted instructions.

Mitigation: Treat retrieved account content as data, not as directions for the agent.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/chrischall/skills/apple-icloud-mcp)
- [npm package linked in skill](https://www.npmjs.com/package/apple-icloud-mcp)
- [GitHub repository linked in skill](https://github.com/chrischall/apple-icloud-mcp)

## Skill Output:

**Output Type(s):** [Text, Markdown, Configuration, Guidance]

**Output Format:** [Natural-language responses and optional JSON configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include search results, account summaries, directions, forecasts, and previews of proposed changes.]

## Skill Version(s):

0.3.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
