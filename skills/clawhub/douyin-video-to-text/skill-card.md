## Description:

Turns public Douyin video links or share text into transcripts, on-screen text, summaries, and available video details through LinkDigest.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jackchew7143](https://clawhub.ai/user/jackchew7143)

### License/Terms of Use:

MIT-0

## Use Case:

Content creators, researchers, and developers use this skill to read and summarize public Douyin videos, extract spoken and on-screen text, and review video metadata without downloading video files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Submitted links and API credentials are sent to LinkDigest, and third-party model services may process video content.

Mitigation: Submit only public, non-sensitive links and keep the API key in an environment variable or protected configuration.

Risk: Text results may be cached by public link and shared with later users of that link.

Mitigation: Do not submit private or sensitive links; review LinkDigest's privacy policy before use.

Risk: The optional npx-based MCP setup runs an unpinned package.

Mitigation: Prefer the bundled Python client, or review and pin the MCP package before use.

## Reference(s):

- [LinkDigest documentation](https://linkdigest.dev/zh/docs)
- [LinkDigest OpenAPI specification](https://linkdigest.dev/openapi.json)
- [ClawHub skill listing](https://clawhub.ai/jackchew7143/skills/douyin-video-to-text)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Plain text or JSON video digest, including transcript, on-screen text, summary, and available metadata]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Full transcripts require an API key and may consume credits; unauthenticated use returns a limited daily summary. Timestamps are approximate, and some results may be partial.]

## Skill Version(s):

1.0.0 (source: frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
