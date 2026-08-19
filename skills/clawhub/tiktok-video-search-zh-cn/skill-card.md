## Description:

通过 Gecho Bridge MCP 按关键词搜索 TikTok 视频，返回视频元数据、创作者、互动指标和链接。需要安装 Gecho Chrome 扩展、保持有效的 TikTok 登录会话，并配置 Gecho Bridge MCP 服务。

This skill is ready for commercial/non-commercial use.

## Publisher:

[gecho-ai](https://clawhub.ai/user/gecho-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to route TikTok keyword video search requests to the official Gecho Bridge MCP workflow, collect structured video metadata, discover creators, and summarize useful results without pasting full raw JSON into the conversation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on Gecho Bridge, the Gecho Chrome extension, and a logged-in TikTok browser session.

Mitigation: Confirm those external components and session requirements are acceptable before use, and stop on tool errors, timeouts, login walls, or CAPTCHA prompts.

Risk: Saved TikTok search JSON may contain sensitive research data, creator metadata, or links.

Mitigation: Choose save directories deliberately, avoid pasting full raw JSON into conversation, and share only the concise result summaries needed for the task.

## Reference(s):

- [Gecho website](https://gecho.ai/)
- [Gecho Bridge GitHub repository](https://github.com/gecho-ai/gecho-bridge)
- [Gecho Bridge README](https://github.com/gecho-ai/gecho-bridge/blob/main/README.md)
- [Gecho Chrome extension](https://chromewebstore.google.com/detail/pjkaeenpekolahdbccjfenjcmanemlbj?utm_source=item-share-cb)
- [OpenClaw + TikTok configuration video](https://www.youtube.com/watch?v=ggwY9hISHcQ)
- [Hermes + TikTok configuration video](https://www.youtube.com/watch?v=zHKnuWnxt_c)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and concise structured summaries of TikTok video metadata]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May summarize the first 3 to 5 returned videos and include a saved JSON file path when the Gecho MCP tool reports one.]

## Skill Version(s):

1.1.36 (source: server release evidence and artifact _meta.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
