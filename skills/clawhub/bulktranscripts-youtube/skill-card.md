## Description:

Fetches YouTube video transcripts, searches YouTube, lists channel or playlist videos, and tracks new uploads through the BulkTranscripts API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pratie](https://clawhub.ai/user/pratie)

### License/Terms of Use:

MIT

## Use Case:

Developers and external agent users use this skill to retrieve transcripts, search YouTube content, research channels or playlists, and monitor new uploads for summarization, quoting, comparison, and reporting workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: YouTube URLs, video IDs, channel handles, playlist IDs, and search terms are sent to bulktranscripts.co.

Mitigation: Use the skill only when sending those YouTube-related inputs to BulkTranscripts is acceptable, and set BULKTRANSCRIPTS_API_KEY only for accounts trusted for those requests.

Risk: Bulk transcript fetching can spend account credits.

Mitigation: Show the user counts before large channel or playlist jobs, fetch selectively, and monitor billing.remaining or out_of_credits responses.

Risk: Installing directly from a remote skill URL can change behavior if the source changes later.

Mitigation: Review SKILL.md before installation and prefer a pinned or packaged source when possible.

## Reference(s):

- [BulkTranscripts API documentation](https://bulktranscripts.co/docs)
- [BulkTranscripts OpenAPI specification](https://bulktranscripts.co/openapi.json)
- [BulkTranscripts YouTube transcript agent skill](https://bulktranscripts.co/youtube-transcript-agent-skill)
- [ClawHub skill page](https://clawhub.ai/pratie/skills/bulktranscripts-youtube)
- [Summarize a video example](examples/summarize-video.md)
- [Research a channel example](examples/research-channel.md)
- [Monitor a channel for new uploads example](examples/monitor-channel.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and API response handling]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide agents to fetch JSON, text, Markdown, SRT, VTT, CSV, or AI-formatted transcript outputs from the BulkTranscripts API.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
