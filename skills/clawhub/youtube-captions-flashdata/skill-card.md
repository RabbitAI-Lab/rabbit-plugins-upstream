## Description:

Retrieves existing YouTube caption tracks through FlashData and supports local text, SRT, and WebVTT exports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[rocosen](https://clawhub.ai/user/rocosen)

### License/Terms of Use:

MIT-0

## Use Case:

OpenClaw users and developers retrieve language-specific, existing YouTube captions with timestamps and export them as plain text or subtitles. A FlashData API key and paid Credits are required for data queries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Video identifiers and caption query settings are sent to FlashData for processing.

Mitigation: Send only identifiers needed for the user's request and confirm external data sharing is acceptable.

Risk: Data queries spend FlashData Credits, and a timed-out submission may already have been charged.

Mitigation: Check pricing and the approved budget first; after a timeout, check the existing job or Jobs console instead of automatically resubmitting.

Risk: Exposure of the FlashData API key or unreviewed third-party package execution.

Mitigation: Keep the key in protected settings and out of prompts or files; review the pinned npm package where dependency provenance matters.

## Reference(s):

- [FlashData YouTube captions documentation](https://flashdata.dev/docs/sources/youtube_captions?utm_source=clawhub&utm_medium=integration&utm_campaign=intent_gtm_2026q4&utm_content=youtube_captions-task)
- [Caption query example](references/query.json)
- [Caption query schema](references/schema.json)
- [FlashData MCP documentation](https://flashdata.dev/mcp)

## Skill Output:

**Output Type(s):** [Text, Subtitle files, Guidance]

**Output Format:** [Plain text, SRT, WebVTT, or Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Caption segments retain their original wording and timestamps; availability depends on the selected video, language, and track type.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
