## Description:

通过官方 Gecho Bridge MCP 按关键词搜索公开的 X（Twitter）帖子，返回帖子文本、作者、互动数据和链接。

This skill is ready for commercial/non-commercial use.

## Publisher:

[gecho-ai](https://clawhub.ai/user/gecho-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to route X/Twitter keyword research or monitoring requests through the official Gecho Bridge MCP workflow and summarize representative public posts, authors, engagement data, and links.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The Gecho MCP bridge and Chrome extension can access X/Twitter content available in the user's logged-in browser session.

Mitigation: Install and use the skill only when comfortable with that browser-session access, and keep platform prompts and account login steps under user control.

Risk: The workflow will not run if Gecho Bridge MCP, the Chrome extension, the Gecho account session, or the X/Twitter browser session is missing.

Mitigation: Configure the Gecho Bridge MCP service, install and log into the Chrome extension, and keep a logged-in X/Twitter tab open before running the skill.

Risk: Login walls, captchas, region prompts, cookie prompts, timeouts, or blocked pages can stop or limit collection.

Mitigation: Have the user resolve browser prompts manually, stop on tool errors or empty results, and report the exact failure instead of retrying or switching to unofficial scraping.

## Reference(s):

- [Gecho website](https://gecho.ai/)
- [Gecho Bridge GitHub repository](https://github.com/gecho-ai/gecho-bridge)
- [Gecho Bridge README](https://github.com/gecho-ai/gecho-bridge/blob/main/README.md)
- [Gecho Chrome extension](https://chromewebstore.google.com/detail/pjkaeenpekolahdbccjfenjcmanemlbj?utm_source=item-share-cb)
- [OpenClaw configuration video](https://www.youtube.com/watch?v=ggwY9hISHcQ)
- [Hermes configuration video](https://www.youtube.com/watch?v=zHKnuWnxt_c)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with summarized X/Twitter post data, links, setup commands, and troubleshooting guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Successful runs summarize the most useful fields or 3 to 5 representative results and may include a saved local results path.]

## Skill Version(s):

1.1.37 (source: ClawHub release evidence and artifact/_meta.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
