## Description:

通过 Gecho Bridge MCP 搜索 TikTok 视频、采集创作者视频、获取指定视频详情与评论，并开展商品、趋势、竞品与内容洞察；使用前需要安装 Gecho Chrome 扩展、保持有效的 TikTok 登录会话，并配置 Gecho Bridge MCP 服务。

This skill is ready for commercial/non-commercial use.

## Publisher:

[gecho-ai](https://clawhub.ai/user/gecho-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, marketers, and developers use this skill to research TikTok videos, creators, comments, product opportunities, trends, competitors, and content ideas through Gecho Bridge MCP. It helps agents route TikTok search, video-detail collection, creator-video collection, async insight jobs, and insight-status checks to the official Gecho MCP tools.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill connects Gecho to a logged-in TikTok browser session and can collect TikTok metadata, comments, replies, and insight outputs.

Mitigation: Install only if that data flow is acceptable, keep Gecho and TikTok sessions under user control, and review the Gecho MCP package and Chrome extension before use.

Risk: Collected TikTok results and insight outputs may be stored locally as JSON files.

Mitigation: Choose an appropriate save directory, limit access to exported files, and delete exports when they are no longer needed.

Risk: TikTok login walls, CAPTCHA, private videos, deleted videos, or browser-session failures can prevent reliable collection.

Mitigation: Report the exact tool or page failure, avoid retrying automatically in the same turn, and do not fabricate missing video, comment, or insight data.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/gecho-ai/skills/tiktok-search-zh-cn)
- [Gecho](https://gecho.ai/)
- [Gecho Bridge README](https://github.com/gecho-ai/gecho-bridge/blob/main/README.md)
- [Gecho Chrome Extension](https://chromewebstore.google.com/detail/pjkaeenpekolahdbccjfenjcmanemlbj?utm_source=item-share-cb)
- [OpenClaw Configuration Video](https://www.youtube.com/watch?v=ggwY9hISHcQ)
- [Hermes Configuration Video](https://www.youtube.com/watch?v=zHKnuWnxt_c)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown summaries with optional JSON metadata, saved file paths, job IDs, and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce local JSON result files and asynchronous insight job IDs through Gecho MCP tools.]

## Skill Version(s):

1.1.37 (source: server release evidence and artifact/_meta.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
