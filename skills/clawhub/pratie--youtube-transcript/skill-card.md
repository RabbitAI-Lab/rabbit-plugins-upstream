## Description:

Get the transcript of a single YouTube video (or Short, or TikTok video) as clean text, timestamped segments, or SRT/VTT/Markdown via the BulkTranscripts API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pratie](https://clawhub.ai/user/pratie)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to retrieve video transcripts for summarization, quoting with timestamps, translation, fact-checking, and note generation. It depends on the BulkTranscripts API and requires a user-provided API key.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Video URLs or IDs are sent to the third-party BulkTranscripts service, and transcript requests may consume account credits.

Mitigation: Use the skill only with videos appropriate to share with the service, check billing.remaining in API responses, and avoid sensitive private links unless the provider is trusted.

Risk: The skill requires a BulkTranscripts API key.

Mitigation: Provide the key through BULKTRANSCRIPTS_API_KEY and avoid exposing it in prompts, logs, or shared transcript output.

## Reference(s):

- [BulkTranscripts documentation](https://bulktranscripts.co/docs)
- [BulkTranscripts OpenAPI specification](https://bulktranscripts.co/openapi.json)
- [BulkTranscripts MCP server](https://bulktranscripts.co/youtube-mcp-server)
- [youtube-transcript on ClawHub](https://clawhub.ai/pratie/skills/youtube-transcript)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and transcript formats such as text, Markdown, SRT, VTT, CSV, or JSON from the API.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Transcript retrieval sends supplied video URLs or IDs to the BulkTranscripts API and may consume account credits.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
