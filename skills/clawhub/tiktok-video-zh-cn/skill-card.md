## Description:

通过官方 Gecho Bridge MCP 获取指定 TikTok 视频详情、评论和回复。用户提供 TikTok 视频详情页 URL，并希望查看单条视频数据或评论时使用；关键词找视频使用 tiktok-video-search。

This skill is ready for commercial/non-commercial use.

## Publisher:

[gecho-ai](https://clawhub.ai/user/gecho-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to route a known TikTok video URL to Gecho's MCP workflow for video metadata, comments, replies, and optional saved JSON results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on Gecho's Chrome extension, Gecho Bridge MCP, and a logged-in TikTok browser session.

Mitigation: Install only if comfortable using those external Gecho components with the relevant browser profile and TikTok account, and review those components separately for sensitive use.

Risk: TikTok login walls, captchas, private or deleted videos, regional prompts, or unavailable pages can block collection.

Mitigation: Resolve browser prompts manually before retrying, and report blocked or unavailable page states instead of fabricating video details or comments.

Risk: Collected comments, replies, and saved JSON may include account-session-visible data.

Mitigation: Limit collection to the requested video, keep outputs concise in chat, and review saved files before sharing them outside the trusted environment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/gecho-ai/skills/tiktok-video-zh-cn)
- [Gecho website](https://gecho.ai/)
- [Gecho Bridge README](https://github.com/gecho-ai/gecho-bridge/blob/main/README.md)
- [Gecho Chrome extension](https://chromewebstore.google.com/detail/pjkaeenpekolahdbccjfenjcmanemlbj?utm_source=item-share-cb)
- [OpenClaw + TikTok configuration video](https://www.youtube.com/watch?v=ggwY9hISHcQ)
- [Hermes + TikTok configuration video](https://www.youtube.com/watch?v=zHKnuWnxt_c)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and optional local JSON file paths]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Summarizes available TikTok video fields and representative comments without pasting full raw JSON into the conversation.]

## Skill Version(s):

1.1.37 (source: server release evidence and artifact _meta.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
