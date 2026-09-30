## Description:

Connects to YouTube Analytics through Maton to retrieve channel reports and manage analytics groups.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Channel owners, analysts, and developers use this skill to review YouTube performance by date, geography, or video, and to manage groups of videos, playlists, or channels. With approval, they can set up recurring analytics checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Connecting an account grants Maton-managed access to YouTube Analytics data.

Mitigation: Confirm the intended account and required permissions with the user before creating a connection; protect credentials and share only the data needed.

Risk: Group changes or hosted automations can alter resources or run repeatedly without further interaction.

Mitigation: Obtain explicit approval for each write, hosted function, and trigger; check the exact resource, fields, schedule, and destination URL before enabling it.

## Reference(s):

- [YouTube Analytics API documentation](https://developers.google.com/youtube/analytics)
- [YouTube Analytics API reference](https://developers.google.com/youtube/analytics/reference)
- [Maton](https://maton.ai)
- [Maton documentation](https://docs.maton.ai)
- [YouTube Analytics skill on ClawHub](https://clawhub.ai/byungkyu/skills/youtube-analytics-api)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Code, Configuration guidance]

**Output Format:** [Markdown with command and code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May summarize YouTube Analytics reports and describe optional automations.]

## Skill Version(s):

1.2.5 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
