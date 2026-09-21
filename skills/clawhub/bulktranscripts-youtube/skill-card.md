## Description:

Fetch YouTube video transcripts, search YouTube, list channel or playlist videos, run a background bulk job for a whole channel or playlist, and track new uploads via the BulkTranscripts API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pratie](https://clawhub.ai/user/pratie)

### License/Terms of Use:

Proprietary API; skill file freely redistributable

## Use Case:

External users and developers use this skill to retrieve YouTube transcripts, search videos, inspect channels or playlists, and run bulk transcript jobs through BulkTranscripts. It is useful for summarization, quotation, creator research, recent-upload tracking, and channel or playlist analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API keys, YouTube queries or links, and bulk-job requests are sent to BulkTranscripts as a third-party service.

Mitigation: Use the skill only when that data sharing is acceptable, provide a BulkTranscripts API key intentionally, and avoid sending sensitive YouTube research requests.

Risk: Transcript, search, channel, playlist, and bulk operations may consume BulkTranscripts credits and store retrieved transcripts in the user's BulkTranscripts account library.

Mitigation: Check billing status in API responses, prefer free latest-upload checks for monitoring, and confirm expected credit use before large channel or playlist jobs.

Risk: Bulk jobs can process many videos and continue asynchronously after the initial request.

Mitigation: Set an appropriate max_videos limit, poll no sooner than the returned interval, and review job status and results before fetching additional transcripts.

## Reference(s):

- [BulkTranscripts](https://bulktranscripts.co)
- [BulkTranscripts Documentation](https://bulktranscripts.co/docs)
- [BulkTranscripts OpenAPI Specification](https://bulktranscripts.co/openapi.json)
- [BulkTranscripts MCP Server](https://bulktranscripts.co/youtube-mcp-server)
- [BulkTranscripts API Key Setup](https://bulktranscripts.co/app?tab=mcp)
- [BulkTranscripts Pricing](https://bulktranscripts.co/#pricing)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands, API parameters, and JSON response guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference transcript text, timestamps, billing status, bulk job status, and error handling guidance from BulkTranscripts API responses.]

## Skill Version(s):

1.0.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
