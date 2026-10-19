## Description:

Turns supported video links into spoken transcripts, on-screen text, summaries, and engagement snapshots through LinkDigest.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jackchew7143](https://clawhub.ai/user/jackchew7143)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, analysts, and developers use the skill to read public Douyin, Xiaohongshu, TikTok, YouTube, or X videos as text, extract speech and visible text, and optionally draft original scripts inspired by a video's structure.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Video links and resulting text are processed by LinkDigest and its model providers; results are cached by link.

Mitigation: Submit only public links and avoid private or sensitive content.

Risk: Exposing the LinkDigest API key can allow unauthorized use.

Mitigation: Keep LINKDIGEST_API_KEY in environment or configuration storage, not in chats or source code.

Risk: Processing videos or requesting optional features can consume paid credits.

Mitigation: Set --max-credits and review the reported credit usage.

Risk: The optional npx mcp-remote setup can execute an unpinned third-party package.

Mitigation: Avoid that setup or pin the package version if MCP access is needed.

## Reference(s):

- [LinkDigest documentation](https://linkdigest.dev/zh/docs)
- [LinkDigest API reference](https://linkdigest.dev/openapi.json)
- [LinkDigest API key setup](https://linkdigest.dev/app/keys)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Code]

**Output Format:** [Markdown or JSON; optional draft video scripts in text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include segment-level timestamps, on-screen text, summaries, engagement snapshots, translations, and credit usage; does not provide video files.]

## Skill Version(s):

1.2.0 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
