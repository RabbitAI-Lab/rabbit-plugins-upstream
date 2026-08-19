## Description:

通过 Gecho Bridge MCP 发起异步 TikTok 商品、趋势、竞品与内容洞察任务，并查询任务状态；需要安装 Gecho Chrome 扩展、保持有效的 TikTok 登录会话，并配置 Gecho Bridge MCP 服务。

This skill is ready for commercial/non-commercial use.

## Publisher:

[gecho-ai](https://clawhub.ai/user/gecho-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to route TikTok product opportunity, trend, competitor, and content-strategy research requests through the official Gecho Bridge MCP workflow. It also helps users check asynchronous insight job status and summarize completed results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on Gecho Bridge MCP, the Gecho Chrome extension, and a logged-in TikTok browser session, so insight tasks can fail when any required session or service is unavailable.

Mitigation: Confirm the MCP service is configured, the extension is logged in, and TikTok is open in an authenticated Chrome tab before starting an insight job.

Risk: Gecho's external bridge and extension can access TikTok session-visible data while performing research tasks.

Mitigation: Use the skill only when that data access is acceptable for the user's research context and stop on tool errors instead of attempting alternative scraping paths.

Risk: Optional save directories affect where generated research outputs are written.

Mitigation: Choose an absolute save directory deliberately, or omit the parameter and let Gecho use its default data location.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/gecho-ai/skills/tiktok-insight-zh-cn)
- [Gecho Website](https://gecho.ai/)
- [Gecho Bridge GitHub Repository](https://github.com/gecho-ai/gecho-bridge)
- [Gecho Bridge README](https://github.com/gecho-ai/gecho-bridge/blob/main/README.md)
- [Gecho Chrome Extension](https://chromewebstore.google.com/detail/pjkaeenpekolahdbccjfenjcmanemlbj?utm_source=item-share-cb)
- [OpenClaw Configuration Video](https://www.youtube.com/watch?v=ggwY9hISHcQ)
- [Hermes Configuration Video](https://www.youtube.com/watch?v=zHKnuWnxt_c)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and task status summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns Gecho insight job IDs, status summaries, setup guidance, and completed insight summaries when the external MCP workflow provides results.]

## Skill Version(s):

1.1.36 (source: evidence.release.version and artifact/_meta.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
