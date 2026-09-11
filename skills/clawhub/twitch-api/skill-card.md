## Description:

Pull a Twitch channel's profile and live status, list its VODs, highlights, and uploads, read its stream schedule, and resolve a clip to downloadable MP4 qualities with structured JSON responses.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and agents use this skill to retrieve structured Twitch profile, live-status, VOD, schedule, and clip data through Scavio API endpoints for creator research, monitoring, and clip archival.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on Scavio as a third-party API provider and requires a SCAVIO_API_KEY that may spend credits for successful requests.

Mitigation: Confirm Scavio use and billing expectations before installation, store SCAVIO_API_KEY in an environment variable or secret manager, and monitor credit usage.

Risk: Resolved Twitch clip MP4 URLs are directly downloadable and may have short-lived access windows or content-rights constraints.

Mitigation: Use downloaded clip URLs promptly and only access, archive, or share content where the user has the right to do so.

Risk: Twitch data may be missing, unavailable, rate-limited, or constrained by first-page video pagination.

Mitigation: Handle documented 400, 401, 404, 422, 429, and 502 responses explicitly, raise the first parameter up to 100 instead of using deeper pagination, and return only data provided by the API.

## Reference(s):

- [Scavio API documentation](https://scavio.dev/docs?utm_source=agent-skills&utm_medium=skill&utm_campaign=twitch-api)
- [Scavio rate limits](https://scavio.dev/docs/rate-limits?utm_source=agent-skills&utm_medium=skill&utm_campaign=twitch-api)
- [ClawHub skill listing](https://clawhub.ai/scavio-ai/skills/twitch-api)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with Python and curl examples for JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY; successful Twitch API responses use structured JSON envelopes and consume one Scavio credit per endpoint call.]

## Skill Version(s):

1.0.3 (source: server-resolved release evidence; artifact frontmatter says 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
