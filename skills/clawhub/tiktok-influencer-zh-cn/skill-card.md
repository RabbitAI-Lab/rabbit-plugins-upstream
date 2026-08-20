## Description:

通过 Gecho Bridge MCP 采集 TikTok 创作者的公开视频，返回视频元数据、文案、互动指标、发布时间和链接，并要求安装 Gecho Chrome 扩展、保持有效的 TikTok 登录会话、配置 Gecho Bridge MCP 服务。

This skill is ready for commercial/non-commercial use.

## Publisher:

[gecho-ai](https://clawhub.ai/user/gecho-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Social media researchers, marketers, and creator analysts use this skill to route TikTok creator-video collection requests through Gecho Bridge MCP and summarize public video metadata, captions, engagement metrics, publish times, links, and local JSON exports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow relies on Gecho MCP, the Gecho Chrome extension, and a logged-in TikTok browser session.

Mitigation: Install only if comfortable with that browser-session workflow, review Gecho extension and package behavior before enabling them, and keep TikTok verification steps manual.

Risk: TikTok login, verification, region, cookie, or page-blocking prompts can stop data collection.

Mitigation: Resolve platform prompts manually in Chrome before running the tool and stop on tool errors rather than retrying with unofficial scraping or browser automation.

Risk: Creator-video data can be exported to a local directory.

Mitigation: Choose a save directory appropriate for exported creator-video data and avoid exposing unnecessary local paths or files.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/gecho-ai/skills/tiktok-influencer-zh-cn)
- [Gecho Bridge README](https://github.com/gecho-ai/gecho-bridge/blob/main/README.md)
- [Gecho Chrome Extension](https://chromewebstore.google.com/detail/pjkaeenpekolahdbccjfenjcmanemlbj?utm_source=item-share-cb)
- [Gecho official site](https://gecho.ai/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, JSON]

**Output Format:** [Markdown guidance with shell command blocks and concise JSON-result summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Successful runs summarize only the most useful fields or the first 3 to 5 videos and may include a local saved JSON path when available.]

## Skill Version(s):

1.1.36 (source: server release evidence and artifact _meta.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
