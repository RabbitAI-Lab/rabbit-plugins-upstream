## Description:

Converts supported public video links or share text into spoken transcripts, on-screen text, key points, and available engagement data through LinkDigest.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jackchew7143](https://clawhub.ai/user/jackchew7143)

### License/Terms of Use:

MIT-0

## Use Case:

External users and content researchers use this skill to extract spoken words, on-screen text, and summaries from public Douyin, Xiaohongshu, TikTok, YouTube, and X videos for review or analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Submitted video links or share text and cached text results may expose sensitive content to the LinkDigest service or other users of the same link.

Mitigation: Submit only public, non-sensitive links and review the service's privacy terms before use.

Risk: A paid API key can be disclosed or incur unexpected credit usage.

Mitigation: Keep LINKDIGEST_API_KEY out of chats and code, and set a per-request credit limit when appropriate.

Risk: Running an unpinned MCP bridge command introduces avoidable dependency risk.

Mitigation: Prefer the bundled Python script or a pinned MCP bridge version.

## Reference(s):

- [LinkDigest documentation](https://linkdigest.dev/zh/docs)
- [LinkDigest API reference](https://linkdigest.dev/openapi.json)
- [LinkDigest API keys](https://linkdigest.dev/app/keys)
- [ClawHub skill release](https://clawhub.ai/jackchew7143/skills/linkdigest-video-transcript)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown by default; optional JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Transcript segments and approximate on-screen text times; may include key points, engagement data, and coverage details.]

## Skill Version(s):

1.1.0 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
