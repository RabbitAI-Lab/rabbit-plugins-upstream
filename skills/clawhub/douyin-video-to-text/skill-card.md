## Description:

Turns supported video links into transcripts, on-screen text, and summaries using LinkDigest.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jackchew7143](https://clawhub.ai/user/jackchew7143)

### License/Terms of Use:

MIT-0

## Use Case:

Users and developers can extract speech, visible text, and key points from public Douyin and other supported video links without downloading the video.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Submitted video links and, when configured, an API key are sent to LinkDigest for processing and caching.

Mitigation: Submit only links suitable for third-party processing; avoid private links and sensitive material, and keep the API key out of chat and shared files.

Risk: The optional npx MCP bridge introduces an unpinned dependency.

Mitigation: Prefer the bundled Python script or direct HTTPS API, or independently trust and pin the bridge dependency.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/jackchew7143/skills/douyin-video-to-text)
- [LinkDigest documentation](https://linkdigest.dev/zh/docs)
- [LinkDigest API specification](https://linkdigest.dev/openapi.json)
- [LinkDigest privacy policy](https://linkdigest.dev/privacy)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Markdown by default; JSON optional]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include segment-level transcript times, approximate on-screen text times, video metadata, and credit usage; keyless access provides a limited summary.]

## Skill Version(s):

1.0.1 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
