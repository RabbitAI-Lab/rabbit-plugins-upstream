## Description:

通过 Gecho Bridge MCP 按关键词搜索 TikTok 视频，返回视频元数据、创作者、互动指标和链接。需要安装 Gecho Chrome 扩展、保持有效的 TikTok 登录会话，并配置 Gecho Bridge MCP 服务。

This skill is ready for commercial/non-commercial use.

## Publisher:

[gecho-ai](https://clawhub.ai/user/gecho-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to configure Gecho Bridge MCP, search TikTok by keyword, collect video metadata and creator signals, and receive concise result summaries with saved local JSON paths when available.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow depends on Gecho Bridge, the Gecho Chrome extension, a logged-in Gecho account, and a logged-in TikTok browser session; missing sessions, login walls, CAPTCHA, or extension issues can prevent collection.

Mitigation: Confirm the required MCP configuration, extension login, and active TikTok browser session before running; stop after tool errors and report the exact failure instead of retrying automatically.

Risk: Complete TikTok search results may be saved locally as JSON and can include sensitive business, research, or personal context.

Mitigation: Choose an appropriate save directory, avoid exposing raw JSON in chat, and delete or protect saved result files when they contain sensitive context.

Risk: Runtime behavior is delegated to the external Gecho Bridge and Chrome extension.

Mitigation: Review Gecho Bridge and the Chrome extension separately before use in sensitive or controlled environments.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/gecho-ai/skills/tiktok-video-search-zh-cn)
- [Gecho website](https://gecho.ai/)
- [Gecho Bridge README](https://github.com/gecho-ai/gecho-bridge/blob/main/README.md)
- [Gecho Chrome extension](https://chromewebstore.google.com/detail/pjkaeenpekolahdbccjfenjcmanemlbj?utm_source=item-share-cb)
- [OpenClaw configuration video](https://www.youtube.com/watch?v=ggwY9hISHcQ)
- [Hermes configuration video](https://www.youtube.com/watch?v=zHKnuWnxt_c)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, json, guidance]

**Output Format:** [Markdown responses with shell command blocks, concise result summaries, and references to locally saved JSON files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Summarizes only the first 3 to 5 TikTok results and avoids pasting complete raw JSON into the conversation.]

## Skill Version(s):

1.1.37 (source: server release metadata and artifact _meta.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
