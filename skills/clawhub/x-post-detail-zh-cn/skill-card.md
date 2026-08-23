## Description:

通过官方 Gecho Bridge MCP 获取一条 X（Twitter）帖子及其回复。用户提供 X 帖子 URL，并需要正文、作者、互动数据或评论时使用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[gecho-ai](https://clawhub.ai/user/gecho-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, researchers, and social-media analysts use this skill to collect the visible details and available replies for a specific X/Twitter post through Gecho Bridge MCP, then receive a concise summary and saved-result path when available.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow can access X/Twitter content visible to the user's logged-in Chrome browser session through Gecho Bridge and the Chrome extension.

Mitigation: Use it only with accounts and browser sessions where this access is acceptable, and review Gecho provider documentation before installation.

Risk: Collected results may be saved to local directories selected during the workflow.

Mitigation: Save only to intended directories with appropriate permissions and avoid using broad or sensitive output locations.

Risk: Platform prompts such as login, captcha, region, or cookie notices can block or limit collection.

Mitigation: Resolve platform prompts manually in Chrome before retrying, and stop on tool errors or empty results instead of using alternate scraping methods.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/gecho-ai/skills/x-post-detail-zh-cn)
- [Gecho website](https://gecho.ai/)
- [Gecho Bridge GitHub repository](https://github.com/gecho-ai/gecho-bridge)
- [Gecho Bridge README](https://github.com/gecho-ai/gecho-bridge/blob/main/README.md)
- [Gecho Chrome extension](https://chromewebstore.google.com/detail/pjkaeenpekolahdbccjfenjcmanemlbj?utm_source=item-share-cb)
- [OpenClaw configuration video](https://www.youtube.com/watch?v=ggwY9hISHcQ)
- [Hermes configuration video](https://www.youtube.com/watch?v=zHKnuWnxt_c)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown text with concise summaries, setup commands, and saved-result paths when available]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Successful runs should show only the most useful fields or 3 to 5 results and should not paste full raw JSON into the conversation.]

## Skill Version(s):

1.1.37 (source: server release evidence and artifact _meta.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
