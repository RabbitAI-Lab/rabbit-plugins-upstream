## Description:

Pull a Twitch channel's profile and live status, list its VODs, highlights, and uploads, read its stream schedule, and resolve a clip to downloadable MP4 qualities through structured JSON API responses.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, agents, and creator-research workflows use this skill to retrieve Twitch channel profile data, live status, videos, schedules, and clip download qualities. It is suited for Twitch lookup, monitoring, and archival tasks that require structured API results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Using the skill calls Scavio's external API with a user-provided API key and consumes credits for successful Twitch lookups.

Mitigation: Confirm the user intends to call Scavio before requests, keep SCAVIO_API_KEY in the environment or a secret store, and do not hardcode the key in source files.

Risk: Returned Twitch counts, titles, schedules, and clip URLs may be time-sensitive or unavailable if the source changes.

Mitigation: Report only values returned by the API, handle 400, 401, 404, 422, 429, and 502 responses explicitly, and avoid fabricating missing Twitch data.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/scavio-ai/skills/twitch-api)
- [Scavio Twitch API Documentation](https://scavio.dev/docs?utm_source=agent-skills&utm_medium=skill&utm_campaign=twitch-api)
- [Scavio Rate Limits](https://scavio.dev/docs/rate-limits?utm_source=agent-skills&utm_medium=skill&utm_campaign=twitch-api)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON API response descriptions and inline Python, curl, and shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses a Scavio API key, calls external Scavio endpoints, and returns structured JSON envelopes containing data, response_time, credits_used, and credits_remaining.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
