## Description:

This skill should be used when the user asks about Apple Music, their Apple Music playlists or library, iCloud Calendar, iCloud Contacts, iCloud Mail, Apple Maps directions or places, the weather (WeatherKit), podcasts, or iTunes/App Store search — from any OS, via Apple's web services.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users can use the skill to search and manage their Apple Music library, iCloud calendar, contacts, and mail, and to retrieve Apple Maps, WeatherKit, podcast, and iTunes/App Store information. It connects to Apple's web services from any operating system.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Apple account credentials and the Apple Music web token grant access to personal account data.

Mitigation: Protect these credentials, confirm Apple is the intended provider, and pin a reviewed package version.

Risk: Tools that send mail or edit or delete account data can cause unintended changes.

Mitigation: Review confirmation previews before approving sensitive actions; use APPLE_SERVICES to limit enabled services and APPLE_WRITE_MODE=none for read-only access when appropriate.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/chrischall/skills/apple-icloud-mcp)
- [npm package](https://www.npmjs.com/package/apple-icloud-mcp)

## Skill Output:

**Output Type(s):** [Text, Structured data, API results, Configuration guidance]

**Output Format:** [Structured tool results and natural-language responses; JSON configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Some tools modify account data or send email and require confirmation.]

## Skill Version(s):

0.3.7 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
