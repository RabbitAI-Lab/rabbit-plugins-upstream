## Description:

通过官方 Gecho Bridge MCP 搜索 TikTok Shop 商品并获取已知商品详情。适用于商品发现、商品库调研、竞品比较、价格与销量信号分析，以及指定商品详情采集。

This skill is ready for commercial/non-commercial use.

## Publisher:

[gecho-ai](https://clawhub.ai/user/gecho-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, ecommerce researchers, and marketplace operators use this skill to route TikTok Shop product search and known-product detail requests through Gecho Bridge, then summarize product, price, rating, sales-signal, variant, review, link, and saved-file outputs from the authenticated browser session.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow depends on Gecho Bridge, the Gecho Chrome extension, and an authenticated TikTok Shop browser session.

Mitigation: Confirm those components are installed, logged in, and acceptable for the user's environment before using the skill.

Risk: Returned product data and saved JSON can contain marketplace research data from the user's authenticated session.

Mitigation: Treat saved files as session-derived research data and write them only to intended, access-controlled workspace directories.

Risk: Login walls, CAPTCHA, regional prompts, unavailable products, or tool failures can prevent reliable results.

Mitigation: Resolve browser prompts manually, stop on tool errors, and summarize only data returned by the official Gecho MCP tools.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/gecho-ai/skills/tiktok-shop-zh-cn)
- [Gecho website](https://gecho.ai/)
- [Gecho Bridge README](https://github.com/gecho-ai/gecho-bridge/blob/main/README.md)
- [Gecho Chrome extension](https://chromewebstore.google.com/detail/pjkaeenpekolahdbccjfenjcmanemlbj?utm_source=item-share-cb)
- [OpenClaw configuration video](https://www.youtube.com/watch?v=ggwY9hISHcQ)
- [Hermes configuration video](https://www.youtube.com/watch?v=zHKnuWnxt_c)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files]

**Output Format:** [Markdown summaries with inline shell commands and optional local JSON result paths]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are based on Gecho MCP tool results from the user's authenticated TikTok Shop browser session; the skill tells the agent not to paste complete raw JSON into chat.]

## Skill Version(s):

1.1.37 (source: evidence release and artifact _meta.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
