## Description:

Retrieves YouTube video and channel details, transcripts, comments, playlists, and search results through the Crawlora API for research and summaries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, developers, and other users can collect public YouTube transcripts, comments, video and channel details, and search results to prepare evidence-backed summaries and comparisons.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Requested YouTube lookups and the Crawlora API key are sent to Crawlora.

Mitigation: Use the skill only if this disclosure is acceptable; keep the key in CRAWLORA_API_KEY and never hardcode it.

Risk: Public YouTube transcripts and comments may be missing, incomplete, or inaccurate.

Mitigation: Check transcript availability and verify consequential claims against the source video.

## Reference(s):

- [YouTube endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [YouTube Research on ClawHub](https://clawhub.ai/crawlora-org/skills/youtube-research)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands]

**Output Format:** [Markdown summaries and structured JSON results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include video URLs and timestamped transcript evidence; availability varies by video.]

## Skill Version(s):

1.0.19 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
