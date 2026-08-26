## Description:

通过 Gecho Bridge MCP 发起异步 TikTok 商品、趋势、竞品与内容洞察任务，并查询任务状态。需要安装 Gecho Chrome 扩展、保持有效的 TikTok 登录会话，并配置 Gecho Bridge MCP 服务。

This skill is ready for commercial/non-commercial use.

## Publisher:

[gecho-ai](https://clawhub.ai/user/gecho-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and operators use this skill to start and check asynchronous TikTok product, trend, competitor, and content insight tasks through Gecho Bridge MCP. It is intended for market opportunity analysis, trend discovery, competitor research, and content strategy workflows that rely on the user's configured Gecho Chrome extension and logged-in TikTok browser session.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow relies on a third-party Gecho Chrome extension and MCP bridge that can use the TikTok data visible in the user's logged-in browser session.

Mitigation: Install and use the skill only after reviewing and accepting the Gecho extension, MCP package, and browser-session permissions; avoid using it with TikTok sessions containing data that should not be shared with Gecho.

Risk: TikTok insight tasks can fail or return incomplete results when the Gecho extension, Gecho account, TikTok login, browser tab, or MCP bridge is not ready.

Mitigation: Complete the documented setup first: install Node.js, configure Gecho Bridge MCP, install and log into the Gecho Chrome extension, and keep a logged-in TikTok browser tab open during use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/gecho-ai/skills/tiktok-insight-zh-cn)
- [Gecho website](https://gecho.ai/)
- [Gecho Bridge README](https://github.com/gecho-ai/gecho-bridge/blob/main/README.md)
- [Gecho Chrome extension](https://chromewebstore.google.com/detail/pjkaeenpekolahdbccjfenjcmanemlbj?utm_source=item-share-cb)
- [OpenClaw configuration video](https://www.youtube.com/watch?v=ggwY9hISHcQ)
- [Hermes configuration video](https://www.youtube.com/watch?v=zHKnuWnxt_c)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown responses with inline shell commands and MCP tool-routing guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return a jobId for asynchronous insight tasks, status updates for existing jobs, or summarized insight results when the Gecho MCP tool returns completed data.]

## Skill Version(s):

1.1.37 (source: server release metadata and artifact _meta.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
