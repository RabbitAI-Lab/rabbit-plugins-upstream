## Description:

Search YouTube and retrieve videos, shorts, comments, transcripts, streams, and channel data as structured JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to search YouTube and retrieve structured video, channel, comment, transcript, stream, and related-video data through Scavio endpoints.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses Scavio as a third-party YouTube data provider and requires SCAVIO_API_KEY.

Mitigation: Install only after confirming the third-party provider and secret-handling requirements are acceptable for the deployment environment.

Risk: Endpoint calls spend credits, especially transcripts, streams, search, and paginated requests.

Mitigation: Inform users before broad pagination or high-cost requests and monitor credit usage.

## Reference(s):

- [Scavio documentation](https://scavio.dev/docs)
- [ClawHub skill page](https://clawhub.ai/scavio-ai/skills/youtube-data-api)
- [Publisher profile](https://clawhub.ai/user/scavio-ai)

## Skill Output:

**Output Type(s):** [guidance, shell commands, code, configuration]

**Output Format:** [Markdown with JSON-oriented API guidance and inline shell or Python examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY; API responses are structured JSON returned by Scavio.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
