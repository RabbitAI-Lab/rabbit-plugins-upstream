## Description:

Search TikTok videos by keyword with the official Gecho Bridge MCP tool and return video metadata, creators, engagement metrics, and links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gecho-ai](https://clawhub.ai/user/gecho-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to search TikTok for a keyword or phrase, then receive a concise summary of matching videos with creators, engagement metrics, URLs, and saved result paths when available.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search queries and returned TikTok data flow through the configured Gecho Bridge MCP service.

Mitigation: Confirm the configured MCP service is trusted before installing or using the skill.

Risk: The optional save_dir parameter can store raw result JSON on disk.

Mitigation: Use save_dir only for directories where raw TikTok search result data is acceptable to retain.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/gecho-ai/skills/tiktok-video-search)
- [Gecho AI Publisher Profile](https://clawhub.ai/user/gecho-ai)

## Skill Output:

**Output Type(s):** [text, markdown, files]

**Output Format:** [Markdown summary with TikTok video metadata, URLs, engagement metrics, and optional local JSON result file paths.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses query as the required search term and save_dir as an optional absolute directory for raw result JSON.]

## Skill Version(s):

1.1.35 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
