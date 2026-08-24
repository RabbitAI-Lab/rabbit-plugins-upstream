## Description:

Searches TikTok Shop products and retrieves known product details through official Gecho Bridge MCP tools for product discovery, catalog research, competitor comparison, pricing, sales signals, and item-level detail.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gecho-ai](https://clawhub.ai/user/gecho-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce researchers, sellers, and developers use this skill to discover TikTok Shop products and inspect known product listings. It supports catalog research, competitor comparison, pricing review, sales-signal analysis, and item-level detail from a logged-in TikTok Shop browser session.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on Gecho MCP tools, the Gecho Chrome extension, and a logged-in TikTok Shop browser session.

Mitigation: Install and use it only when that account/session dependency is acceptable, and resolve login walls, CAPTCHA, verification prompts, or unavailable listings manually in Chrome before retrying.

Risk: Saved JSON results may contain proprietary product, competitor, pricing, or sales-signal research data.

Mitigation: Save results only in a workspace or directory suitable for that data, and delete retained files when they are no longer needed.

Risk: Unavailable or blocked TikTok Shop pages can lead to incomplete research output.

Mitigation: Report the page state or tool error exactly and avoid inventing missing product details, prices, ratings, reviews, or links.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/gecho-ai/skills/tiktok-shop)
- [Gecho Website](https://gecho.ai/)
- [Gecho Bridge README](https://github.com/gecho-ai/gecho-bridge/blob/main/README.md)
- [Gecho Chrome Extension](https://chromewebstore.google.com/detail/pjkaeenpekolahdbccjfenjcmanemlbj?utm_source=item-share-cb)
- [OpenClaw Setup Video](https://www.youtube.com/watch?v=ggwY9hISHcQ)
- [Hermes Setup Video](https://www.youtube.com/watch?v=zHKnuWnxt_c)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Files]

**Output Format:** [Markdown guidance with inline shell commands and optional local JSON result files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Successful research responses summarize returned TikTok Shop product data and include saved local result paths when available.]

## Skill Version(s):

1.1.37 (source: server release metadata and artifact _meta.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
