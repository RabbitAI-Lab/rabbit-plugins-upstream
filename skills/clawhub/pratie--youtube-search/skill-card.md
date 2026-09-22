## Description:

Search YouTube for videos, channels, or playlists through the BulkTranscripts API, then fetch relevant transcripts for agent research workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pratie](https://clawhub.ai/user/pratie)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, researchers, and external users use this skill to find relevant YouTube videos or creator-specific content and retrieve transcripts for research, comparison, or citation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: YouTube search terms, channel handles, video URLs or IDs, and transcript requests are sent to BulkTranscripts.

Mitigation: Use the skill only when external API processing is acceptable, and avoid sending sensitive search terms or private research targets.

Risk: Search and transcript calls may consume BulkTranscripts account credits.

Mitigation: Check billing.remaining in responses, limit result counts and transcript fetches, and pause when the API reports out_of_credits.

Risk: The BulkTranscripts API key is required for all endpoints.

Mitigation: Keep the key in BULKTRANSCRIPTS_API_KEY and avoid echoing bearer tokens in user-visible output.

## Reference(s):

- [BulkTranscripts Documentation](https://bulktranscripts.co/docs)
- [BulkTranscripts OpenAPI Specification](https://bulktranscripts.co/openapi.json)
- [BulkTranscripts YouTube MCP Server](https://bulktranscripts.co/youtube-mcp-server)
- [ClawHub Skill Page](https://clawhub.ai/pratie/skills/youtube-search)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown guidance with inline shell commands and API response summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include transcript text or links to supported transcript render formats; API calls require BULKTRANSCRIPTS_API_KEY and may consume account credits.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
