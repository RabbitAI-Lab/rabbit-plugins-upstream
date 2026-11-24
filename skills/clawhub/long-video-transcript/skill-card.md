## Description:

Turns supported video links into timestamped transcripts, on-screen text, key points, and metadata using LinkDigest.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jackchew7143](https://clawhub.ai/user/jackchew7143)

### License/Terms of Use:

MIT-0

## Use Case:

External users can turn supported public video links into transcripts and viewing notes for lectures, courses, podcasts, and social videos.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Processing sends video links and an API key to LinkDigest, and the default mode may use more credits than expected.

Mitigation: Verify that you trust linkdigest.dev, choose the processing mode deliberately, and set a credit limit when needed.

Risk: Results are cached by link and may be returned to other users who submit the same public link.

Mitigation: Do not submit private or sensitive video links.

Risk: The optional local MCP setup invokes mcp-remote through npx without a pinned version.

Mitigation: Skip this setup or inspect and pin the package version before using it.

## Reference(s):

- [LinkDigest documentation](https://linkdigest.dev/zh/docs?ref=skill-long-video-transcript)
- [LinkDigest privacy policy](https://linkdigest.dev/privacy)
- [LinkDigest API reference](https://linkdigest.dev/openapi.json)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Markdown or JSON transcript and summary data]

**Output Parameters:** [1D (video link or shared-link text)]

**Other Properties Related to Output:** [Timestamps are segment-level; completeness and maximum video length depend on processing mode and account plan.]

## Skill Version(s):

1.0.4 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
