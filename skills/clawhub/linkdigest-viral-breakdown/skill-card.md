## Description:

Analyzes a single Douyin, Xiaohongshu, TikTok, YouTube, or Bilibili post into hooks, timed beats, title and cover patterns, calls to action, and reusable structures, checking quoted text against retrieved source text.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jackchew7143](https://clawhub.ai/user/jackchew7143)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, content strategists, and researchers use the skill to study the structure of a single public social post and prepare a structurally informed remix. It does not assess an entire account or predict performance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ClawScan reports that the keyless summary path still sends submitted content to LinkDigest.

Mitigation: Review LinkDigest's privacy policy and submit only links or share text you are comfortable sending to the service; avoid private or sensitive content.

Risk: ClawScan flags an optional unpinned package command in the setup guidance.

Mitigation: Review the package and command before installing; use a verified, pinned package version when appropriate.

Risk: ClawScan marks the skill suspicious in part because of a reported undisclosed translation feature; its analysis is partial and some references could not be resolved.

Mitigation: Review the translation behavior and inspect the skill and unresolved references before deployment.

## Reference(s):

- [LinkDigest documentation](https://linkdigest.dev/zh/docs?ref=skill-linkdigest-viral-breakdown)
- [LinkDigest privacy policy](https://linkdigest.dev/privacy)
- [LinkDigest OpenAPI specification](https://linkdigest.dev/openapi.json)
- [LinkDigest remote MCP endpoint](https://linkdigest.dev/mcp)
- [LinkDigest MCP client and integration examples (reference in skill text; not release provenance)](https://github.com/jcaiagent7143-ui/linkdigest-mcp)

## Skill Output:

**Output Type(s):** [Analysis, Text, Markdown, JSON, Guidance]

**Output Format:** [Markdown or JSON containing a structured single-post breakdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include source-checked quotes, approximate timed beats, reusable templates, and platform engagement data when available. Full output requires LINKDIGEST_API_KEY; submitted links or share text are sent to LinkDigest.]

## Skill Version(s):

1.2.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
