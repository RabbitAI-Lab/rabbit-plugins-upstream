## Description:

Routes TikTok Shop product-search requests through the official Gecho Bridge MCP workflow and returns product data, pricing, ratings, sales signals, and links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gecho-ai](https://clawhub.ai/user/gecho-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Ecommerce researchers, sellers, and agents use this skill to search TikTok Shop by keyword for product discovery and competitor research. It summarizes useful product fields, links, and saved structured results while relying on a user-controlled browser session.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow depends on Gecho Bridge, a Chrome extension, and a logged-in TikTok Shop session, which expands the trust boundary to tools that can read product pages available in that session.

Mitigation: Install and use the integration only after reviewing Gecho Bridge and the Chrome extension, and keep the browser session limited to the TikTok Shop pages needed for the task.

Risk: TikTok Shop may show login, captcha, region, cookie, or verification prompts that prevent complete results.

Mitigation: Have the user resolve platform prompts manually in Chrome before running the skill, and stop with the exact error if the tool fails or times out.

Risk: A full raw product-result dump can overwhelm the conversation or expose more session-derived data than needed.

Mitigation: Summarize only the most useful fields or the top 3 to 5 product results, and provide the saved path instead of pasting full raw JSON.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/gecho-ai/skills/tiktok-shop-search-zh-cn)
- [Gecho](https://gecho.ai/)
- [Gecho Bridge](https://github.com/gecho-ai/gecho-bridge)
- [Gecho Bridge README](https://github.com/gecho-ai/gecho-bridge/blob/main/README.md)
- [Gecho Chrome Extension](https://chromewebstore.google.com/detail/pjkaeenpekolahdbccjfenjcmanemlbj?utm_source=item-share-cb)
- [OpenClaw Configuration Video](https://www.youtube.com/watch?v=ggwY9hISHcQ)
- [Hermes Configuration Video](https://www.youtube.com/watch?v=zHKnuWnxt_c)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with concise summaries, links, saved-result paths, and inline shell command blocks when setup help is needed.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Successful runs summarize only the most useful fields or 3 to 5 product results rather than dumping full raw JSON.]

## Skill Version(s):

1.1.37 (source: server release evidence and artifact _meta.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
