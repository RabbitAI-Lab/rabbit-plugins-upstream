## Description:

This skill should be used when the user asks about Apple Music, their Apple Music playlists or library, iCloud Calendar, iCloud Contacts, iCloud Mail, Apple Maps directions or places, the weather (WeatherKit), podcasts, or iTunes/App Store search — from any OS, via Apple's web services. Unofficial; not affiliated with Apple. Triggers on phrases like "make an Apple Music playlist", "add this song to my playlist", "what's on my calendar", "schedule a meeting", "find free time", "what's Jane's number", "check my iCloud email", "directions to", "how long to drive", "will it rain", "top charts", "find a podcast".

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

People using an agent can query and manage Apple Music, iCloud Calendar, Contacts and Mail, Apple Maps, WeatherKit, and iTunes/App Store catalogs through Apple's web services. The skill supports these tasks from any operating system when the needed service credentials are configured.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The connector can access personal Apple account data and perform account changes.

Mitigation: Enable only the services needed, protect the app password and Music cookie, and retain explicit confirmations for sending mail and destructive actions.

Risk: The review covers the bundled instructions, while the external npm implementation and enforcement of its safeguards remain unverified.

Mitigation: Review the implementation and its safeguards before relying on them; use APPLE_SERVICES and APPLE_WRITE_MODE=none for narrower access as described in the publisher's documentation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/apple-icloud-mcp)
- [Source repository and write protection guidance](https://github.com/chrischall/apple-icloud-mcp#write-protection-apple_write_mode)
- [npm package](https://www.npmjs.com/package/apple-icloud-mcp)

## Skill Output:

**Output Type(s):** [Text, Structured data, Guidance]

**Output Format:** [Natural-language responses with service results such as event, contact, message, map, weather, and catalog data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Varies by requested Apple service; paginated lists and searched date windows are identified in results.]

## Skill Version(s):

0.4.0 (source: server-resolved ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
