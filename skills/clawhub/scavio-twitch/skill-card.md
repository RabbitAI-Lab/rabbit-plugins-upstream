## Description:

Pull a Twitch channel's profile and live status, list its VODs / highlights / uploads, read its stream schedule, and resolve a clip to downloadable MP4 qualities. 4 endpoints, 1 credit each, structured JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to retrieve structured Twitch channel, video, schedule, and clip metadata through Scavio API endpoints for creator research, live-status checks, and clip archival workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Twitch lookups are routed through Scavio as an intermediary service.

Mitigation: Use the skill only when that service path is acceptable for the user's data and workflow.

Risk: Successful API requests consume Scavio credits and require the SCAVIO_API_KEY secret.

Mitigation: Keep SCAVIO_API_KEY out of source control and confirm requests before making repeated or automated calls.

Risk: Downloadable Twitch clip URLs may raise rights or archival concerns.

Mitigation: Check applicable Twitch terms and rights before using clip URLs for archival or redistribution.

## Reference(s):

- [Scavio documentation](https://scavio.dev/docs?utm_source=agent-skills&utm_medium=skill&utm_campaign=twitch-api)
- [Scavio rate limits](https://scavio.dev/docs/rate-limits?utm_source=agent-skills&utm_medium=skill&utm_campaign=twitch-api)
- [ClawHub skill page](https://clawhub.ai/scavio-ai/skills/scavio-twitch)

## Skill Output:

**Output Type(s):** [API Calls, JSON, Shell commands, Code, Guidance]

**Output Format:** [Markdown with JSON responses and inline Python or bash examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should reflect Scavio API responses without fabricating Twitch metrics, titles, URLs, or schedule data.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
