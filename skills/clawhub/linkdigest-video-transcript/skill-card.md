## Description:

Extracts spoken transcripts, on-screen text with approximate timestamps, summaries, and engagement data from supported public video links through LinkDigest.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jackchew7143](https://clawhub.ai/user/jackchew7143)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, analysts, and other users can turn supported public video links or shared link text into transcripts, on-screen text, and concise video insights without downloading the videos.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Video links and the LinkDigest API key are sent to linkdigest.dev.

Mitigation: Use only when comfortable sharing the link and API key with LinkDigest; keep the key in an environment variable or protected configuration.

Risk: Results may be cached by public link and accessible to others requesting that link.

Mitigation: Do not submit private or sensitive video links.

Risk: The optional npx MCP bridge adds package supply-chain exposure.

Mitigation: Prefer the bundled Python client or documented API call unless that additional risk is acceptable.

## Reference(s):

- [LinkDigest documentation](https://linkdigest.dev/zh/docs)
- [LinkDigest OpenAPI specification](https://linkdigest.dev/openapi.json)
- [ClawHub skill listing](https://clawhub.ai/jackchew7143/skills/linkdigest-video-transcript)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Markdown or JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Transcripts have segment-level timestamps; on-screen text has approximate timestamps. Results may include translation, partial-read status, and credit usage.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
