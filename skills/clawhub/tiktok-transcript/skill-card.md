## Description:

Turns supported video links into transcripts, on-screen text, key points, and optional translations through LinkDigest.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jackchew7143](https://clawhub.ai/user/jackchew7143)

### License/Terms of Use:

MIT-0

## Use Case:

People and content teams use this skill to extract spoken words, visible text, and key points from supported video links for review, summarization, or translation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Submitted video links and the optional API key are sent to LinkDigest.

Mitigation: Use the service only when that transfer is acceptable; keep the API key out of chats and shared files.

Risk: Text results may be cached by link and available to others requesting the same link.

Mitigation: Do not submit private or sensitive video links.

Risk: The optional npx MCP setup downloads and runs mcp-remote.

Mitigation: Review or pin mcp-remote before using that setup.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/jackchew7143/skills/tiktok-transcript)
- [LinkDigest documentation](https://linkdigest.dev/zh/docs)
- [LinkDigest privacy policy](https://linkdigest.dev/privacy)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Markdown by default; JSON on request]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include segment-level timestamps, on-screen text, engagement counts, and optional translations; results can be partial.]

## Skill Version(s):

1.0.1 (source: ClawHub release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
