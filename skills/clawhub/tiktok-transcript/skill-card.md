## Description:

Extracts speech, on-screen text, metadata, and key points from supported video links, with optional translation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jackchew7143](https://clawhub.ai/user/jackchew7143)

### License/Terms of Use:

MIT-0

## Use Case:

People who want to understand or repurpose public videos use the skill to get transcripts, on-screen text, summaries, and optional translations from supported video links.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The service accepts links from multiple video platforms and offers paid analysis, which may exceed a TikTok-only use case.

Mitigation: Review the supported platforms and paid options in the LinkDigest documentation before use.

Risk: Video links are sent to an external digest service, and text results may be cached and reused for requests to the same public link.

Mitigation: Use only public video links that you are comfortable submitting to the service; avoid private or sensitive content.

## Reference(s):

- [LinkDigest documentation](https://linkdigest.dev/zh/docs?ref=skill-tiktok-transcript)
- [LinkDigest privacy policy](https://linkdigest.dev/privacy)
- [ClawHub release page](https://clawhub.ai/jackchew7143/skills/tiktok-transcript)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Markdown or JSON transcript and video summary]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Transcript timestamps are segment-level; on-screen text timestamps are approximate.]

## Skill Version(s):

1.0.4 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
