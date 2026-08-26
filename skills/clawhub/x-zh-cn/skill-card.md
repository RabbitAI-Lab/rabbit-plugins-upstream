## Description:

通过官方 Gecho Bridge MCP 搜索 X（Twitter）帖子，并获取已知帖子的详情和回复。适用于关键词监测、帖子研究、作者信息、互动信号和回复分析。

This skill is ready for commercial/non-commercial use.

## Publisher:

[gecho-ai](https://clawhub.ai/user/gecho-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to route X/Twitter keyword searches and post-detail requests through Gecho Bridge for social listening, content research, interaction analysis, and reply summaries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow reads X content available in the user's logged-in browser session and may save returned search or post data as local JSON files.

Mitigation: Use the skill only with an intended browser profile and choose a controlled save directory when local JSON output is requested.

Risk: Searches or post lookups can fail when Gecho Bridge, the Chrome extension, Gecho login, X login, or the browser page state is not ready.

Mitigation: Complete the documented setup, keep Chrome logged into Gecho and X, and manually resolve login walls, verification prompts, rate limits, or unavailable posts before retrying.

Risk: Returned social-media data may be partial because replies, deleted posts, protected accounts, regional restrictions, or page blocks can limit what the tool can access.

Mitigation: Summarize only tool-returned content, report unavailable states directly, and avoid fabricating missing authors, interactions, replies, or links.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/gecho-ai/skills/x-zh-cn)
- [Gecho Bridge README](https://github.com/gecho-ai/gecho-bridge/blob/main/README.md)
- [Gecho Bridge GitHub Repository](https://github.com/gecho-ai/gecho-bridge)
- [Gecho Chrome Extension](https://chromewebstore.google.com/detail/pjkaeenpekolahdbccjfenjcmanemlbj?utm_source=item-share-cb)
- [Gecho Website](https://gecho.ai/)
- [OpenClaw Configuration Video](https://www.youtube.com/watch?v=ggwY9hISHcQ)
- [Hermes Configuration Video](https://www.youtube.com/watch?v=zHKnuWnxt_c)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance, JSON files]

**Output Format:** [Markdown responses with inline shell commands and optional local JSON result files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Routes work through the x_search and x_post_detail MCP tools, runs Gecho tasks serially, and summarizes returned data without pasting full raw JSON.]

## Skill Version(s):

1.1.37 (source: server release metadata and artifact _meta.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
