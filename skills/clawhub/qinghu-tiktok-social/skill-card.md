## Description:

青虎AI TikTok 社媒运营：监控 TikTok 行业热门话题与视频榜单，按关键词搜索高赞内容，批量查视频详情并读评论，拆解脚本结构、播放爆发力与互动亮点，持续为短视频创作提供选题与拍摄灵感。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and content operators use this skill to research TikTok topics, trend signals, competitor activity, audience comments, and content calendar ideas from Qinghu data interfaces.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access a Qinghu API token and make external API calls for TikTok research.

Mitigation: Use a scoped token where possible, provide credentials only in trusted environments, and monitor paid-tool authorization prompts.

Risk: The skill may automatically export larger datasets to local files that contain sensitive business research.

Mitigation: Review, retain, or delete exported and cached files according to the user's data-handling requirements.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-tiktok-social)
- [Qinghu MCP API endpoint](https://www.iqinghu.com/api/desktop/qh/mcp)
- [Qinghu API key dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Files, Guidance]

**Output Format:** [Markdown responses with optional JSON-RPC examples, shell/API commands, and exported table files for larger result sets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Summaries emphasize topic recommendations, trend rankings, competitor account updates, audience-comment insights, source period, region, and Qinghu point usage when paid calls are made.]

## Skill Version(s):

0.1.0 (source: evidence.release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
