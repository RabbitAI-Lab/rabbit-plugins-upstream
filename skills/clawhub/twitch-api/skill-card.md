## Description:

Pull a Twitch channel's profile and live status, list its VODs, highlights and uploads, read its stream schedule, and resolve a clip to downloadable MP4 qualities.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, agents, and creator-research workflows use this skill to retrieve structured Twitch channel, video, schedule, and clip data through Scavio API endpoints.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Twitch channel and clip queries are sent to Scavio and consume Scavio credits.

Mitigation: Use the skill only when that data sharing and credit usage are acceptable for the workflow.

Risk: The skill requires SCAVIO_API_KEY for API access.

Mitigation: Keep SCAVIO_API_KEY in an environment variable or secret store and out of source control.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/scavio-ai/skills/twitch-api)
- [Scavio documentation](https://scavio.dev/docs?utm_source=agent-skills&utm_medium=skill&utm_campaign=twitch-api)
- [Scavio rate limits](https://scavio.dev/docs/rate-limits?utm_source=agent-skills&utm_medium=skill&utm_campaign=twitch-api)

## Skill Output:

**Output Type(s):** [guidance, shell commands, code, configuration, JSON]

**Output Format:** [Markdown guidance with command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses SCAVIO_API_KEY and returns structured JSON envelopes with data, response_time, credits_used, and credits_remaining.]

## Skill Version(s):

1.0.1 (source: server release metadata; artifact frontmatter lists 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
