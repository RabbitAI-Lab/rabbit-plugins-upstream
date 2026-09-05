## Description:

Pull a Twitch channel's profile and live status, list its VODs, highlights, and uploads, read its stream schedule, and resolve a clip to downloadable MP4 qualities.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to retrieve structured Twitch channel, video, schedule, and clip data through Scavio for creator research, live-status monitoring, and clip archival workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends requested Twitch channel handles or clip identifiers to Scavio.

Mitigation: Send only the Twitch identifiers needed for the requested lookup and avoid including unrelated secrets or personal data.

Risk: Successful API calls consume Scavio credits, and clip downloads may involve Twitch terms or content-owner rights.

Mitigation: Monitor credit usage and only download or archive clips when the user has appropriate permission and complies with applicable terms.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/scavio-ai/skills/twitch-api)
- [Scavio Twitch API documentation](https://scavio.dev/docs?utm_source=agent-skills&utm_medium=skill&utm_campaign=twitch-api)
- [Scavio rate limits](https://scavio.dev/docs/rate-limits?utm_source=agent-skills&utm_medium=skill&utm_campaign=twitch-api)

## Skill Output:

**Output Type(s):** [guidance, code, shell commands, configuration, API Calls]

**Output Format:** [Markdown with JSON request examples, Python snippets, and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY; API responses use structured JSON envelopes.]

## Skill Version(s):

1.0.2 (source: release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
