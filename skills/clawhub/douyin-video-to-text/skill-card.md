## Description:

Extracts transcripts, on-screen text, summaries, and engagement details from supported video links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jackchew7143](https://clawhub.ai/user/jackchew7143)

### License/Terms of Use:

MIT-0

## Use Case:

People reviewing supported public video links can use the skill to retrieve spoken transcripts, on-screen text, summaries, and available engagement statistics.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The optional stdio MCP integration invokes unpinned mcp-remote through npx, which the security scan flagged as a supply-chain risk; scan coverage was partial because a local reference could not be resolved.

Mitigation: Use the documented Streamable HTTP MCP endpoint when supported. If stdio integration is needed, review and pin the mcp-remote package version, and resolve the missing local reference before relying on the partial scan.

## Reference(s):

- [LinkDigest documentation](https://linkdigest.dev/zh/docs?ref=skill-douyin-video-to-text)
- [LinkDigest privacy policy](https://linkdigest.dev/privacy)
- [LinkDigest OpenAPI specification](https://linkdigest.dev/openapi.json)
- [Open source MCP client and examples](https://github.com/jcaiagent7143-ui/linkdigest-mcp)
- [ClawHub skill release](https://clawhub.ai/jackchew7143/skills/douyin-video-to-text)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Markdown or JSON containing transcript text, on-screen text, summaries, and available video metadata]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Transcript timestamps are segment-level; on-screen text timestamps are approximate. Some details require an optional API key.]

## Skill Version(s):

1.0.4 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
