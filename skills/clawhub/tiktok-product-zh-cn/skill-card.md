## Description:

Uses the official Gecho Bridge MCP workflow to retrieve TikTok Shop product details such as title, price, SKU, description, sales, ratings, and reviews from a product URL or product ID.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gecho-ai](https://clawhub.ai/user/gecho-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and commerce researchers use this skill to route TikTok Shop product-detail requests through Gecho Bridge and summarize the most useful returned fields. It is intended for single-product collection when the user has configured Gecho Bridge, installed the Gecho Chrome extension, and logged in to the required browser sessions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow relies on a logged-in browser session and the Gecho Chrome extension to access TikTok Shop pages.

Mitigation: Confirm trust in Gecho Bridge and the extension before installation, keep credentials out of the skill conversation, and resolve login, captcha, region, or cookie prompts manually in Chrome.

Risk: Collected product data may be incomplete or unavailable when TikTok Shop blocks access or required sessions are not ready.

Mitigation: Use the skill only for product-detail collection, run one Gecho fetch task at a time, and report exact tool failures instead of retrying or switching to unofficial scraping.

Risk: Saved output paths can expose collected commerce data in an unintended location.

Mitigation: Review any save directory before use and provide only writable directories that are appropriate for the research task.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/gecho-ai/skills/tiktok-product-zh-cn)
- [Gecho Bridge README](https://github.com/gecho-ai/gecho-bridge/blob/main/README.md)
- [Gecho website](https://gecho.ai/)
- [Gecho Chrome extension](https://chromewebstore.google.com/detail/pjkaeenpekolahdbccjfenjcmanemlbj?utm_source=item-share-cb)
- [OpenClaw configuration video](https://www.youtube.com/watch?v=ggwY9hISHcQ)
- [Hermes configuration video](https://www.youtube.com/watch?v=zHKnuWnxt_c)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with concise summaries, setup commands, links, and saved-path guidance when available]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Summarizes only the most useful product fields instead of pasting full raw JSON.]

## Skill Version(s):

1.1.37 (source: server release evidence and artifact _meta.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
