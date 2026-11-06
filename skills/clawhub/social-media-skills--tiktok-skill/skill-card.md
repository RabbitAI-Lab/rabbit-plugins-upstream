## Description:

Create, check, preview, schedule, and publish TikTok video and photo posts from an agent, then review account analytics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[social-media-skills](https://clawhub.ai/user/social-media-skills)

### License/Terms of Use:

MIT

## Use Case:

External creators and social media teams use the skill to turn their own videos, photos, or ideas into TikTok posts, check them against account limits, and preview, schedule, or publish them after approval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unsafe file handling can overwrite unrelated files.

Mitigation: Use self-created plans in a sandbox without access to unrelated files, and keep backups of originals.

Risk: The fallback login method can expose an API key.

Mitigation: Prefer OAuth and avoid placing API keys in URLs.

Risk: Selected media is uploaded to WoopSocial and its storage provider.

Mitigation: Review the account, privacy, schedule, and media before approving publication; avoid uploading sensitive material unless its handling is acceptable.

## Reference(s):

- [TikTok posting specifications](references/tiktok-specs.md)
- [Post plan format](references/plan-json.md)
- [WoopSocial posting guide](references/woopsocial.md)
- [Writing guidance](references/writing.md)
- [WoopSocial TikTok MCP](https://woopsocial.com/social-media-mcp/tiktok-mcp?utm_source=tiktok-skill&utm_medium=skill)
- [WoopSocial MCP tools reference](https://docs.woopsocial.com/mcp/tools-reference)

## Skill Output:

**Output Type(s):** [Files, Text, JSON, Markdown]

**Output Format:** [MP4 and JPEG media, JSON plans and requests, Markdown previews and schedules, and post captions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Content and schedules are prepared per account; publishing requires explicit user approval.]

## Skill Version(s):

1.0.0 (source: SKILL.md frontmatter, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
