## Description:

YouTube data API: search videos, Shorts and channels, then pull video metadata, comments and replies, transcripts, related videos, download streams, and channel info, videos and community posts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to search YouTube, retrieve video and channel metadata, read comments and transcripts, and generate API requests that return structured JSON for research, content analysis, and retrieval workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search terms and requested YouTube resource identifiers are sent to Scavio when the skill is used.

Mitigation: Avoid sending sensitive queries or private identifiers, and use an appropriate SCAVIO_API_KEY for the intended environment.

Risk: Repeated calls, pagination, transcripts, and stream lookups can consume API credits.

Mitigation: Check endpoint credit costs before broad collection and paginate only as needed.

Risk: Stream URLs can provide direct access to YouTube media and may expire.

Mitigation: Use stream URL functionality only where the user has the right to access or download the content, and treat returned URLs as short-lived.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/scavio-ai/skills/youtube-data-api)
- [Scavio YouTube API documentation](https://scavio.dev/docs?utm_source=clawhub&utm_medium=skill&utm_campaign=youtube-data-api)

## Skill Output:

**Output Type(s):** [guidance, code, shell commands, configuration, text]

**Output Format:** [Markdown with JSON request and response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses SCAVIO_API_KEY for authenticated API calls; Scavio API responses are structured JSON and stream URLs may expire.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
