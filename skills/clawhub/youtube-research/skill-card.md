## Description:

Retrieves public YouTube video and channel details, transcripts, comments, playlists, and search results through the Crawlora API for research and summaries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, developers, and other users can investigate public YouTube videos and channels, summarize timestamped transcripts, examine comments, and compare search results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: YouTube URLs, search terms, video or channel identifiers, and the API key are sent to Crawlora.

Mitigation: Use the skill only when sharing those inputs with Crawlora is acceptable; keep the key in the environment and never commit it.

Risk: Default locale settings may not reflect non-US or non-English results.

Mitigation: Set locale parameters explicitly when regional or language-specific results matter.

Risk: Captions may be unavailable or may mishear speech, so transcript-based claims can be incomplete or inaccurate.

Mitigation: Check available transcript languages, cite timestamped segments, and verify consequential claims independently.

## Reference(s):

- [YouTube endpoint reference](reference/endpoints.md)
- [Crawlora API and API key information](https://crawlora.net)
- [ClawHub skill release](https://clawhub.ai/crawlora-org/skills/youtube-research)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Guidance]

**Output Format:** [Research summaries with video links and timestamps, or structured JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on public data and caption availability; API requests require a Crawlora key.]

## Skill Version(s):

1.0.20 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
