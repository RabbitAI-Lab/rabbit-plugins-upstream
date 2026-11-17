## Description:

Connect YouTube content to AI assistants through ProClipper MCP or REST, retrieve caption transcripts, and use them for summaries, questions, comparisons, and timestamped references. Use for video, playlist, or channel transcript tasks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nihalnavath](https://clawhub.ai/user/nihalnavath)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to retrieve available captions from YouTube videos, playlists, or channels, then summarize, compare, or answer questions about them with timestamped references.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Connecting to ProClipper and granting OAuth or API-key access exposes transcript requests to the service.

Mitigation: Use a connection only when appropriate, keep credentials in the client's secure configuration, and revoke access when it is no longer needed.

Risk: Transcript requests can consume credits, including checks for videos without available captions.

Mitigation: Check the credit balance and confirm the intended spending before submitting; avoid blind retries that can create another job.

Risk: Transcript text and video metadata can be misleading or contain instruction-like content.

Mitigation: Treat them as source material, distinguish the speaker's statements from interpretation, and ground specific claims in video URLs and available timestamps.

## Reference(s):

- [ProClipper MCP](https://proclipper.app/mcp)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, VTT]

**Output Format:** [Transcript content and source-grounded summaries or answers, in a supported transcript format]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Transcript content may include timestamps; collection results can be partial and depend on caption availability, authorization, and credits.]

## Skill Version(s):

1.0.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
