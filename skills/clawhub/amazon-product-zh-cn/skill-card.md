## Description:

通过官方 Gecho Bridge MCP 获取完整的 Amazon 商品详情，包括标题、价格、变体、规格、描述、评分和链接。用户提供 Amazon 商品 URL 或 ASIN 时使用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[gecho-ai](https://clawhub.ai/user/gecho-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and ecommerce researchers use this skill to collect structured Amazon product details from a provided product URL or ASIN through the official Gecho Bridge MCP workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow depends on Gecho Bridge and a Chrome extension connected to a logged-in Amazon browser session.

Mitigation: Confirm the user is comfortable with that browser-session dependency before use and keep the workflow limited to product detail collection.

Risk: A user-provided save directory can write collected results to local storage.

Mitigation: Review the save directory before running the tool and use a path intended for product research output.

Risk: Amazon pages may include private account, payment, order, login, verification, region, or cookie-consent content.

Mitigation: Avoid running the workflow on pages containing private account, payment, or order information, and ask the user to resolve login or verification prompts manually in Chrome.

## Reference(s):

- [Gecho](https://gecho.ai/)
- [Gecho Bridge GitHub](https://github.com/gecho-ai/gecho-bridge)
- [Gecho Bridge README](https://github.com/gecho-ai/gecho-bridge/blob/main/README.md)
- [Gecho Chrome Extension](https://chromewebstore.google.com/detail/pjkaeenpekolahdbccjfenjcmanemlbj?utm_source=item-share-cb)
- [OpenClaw Configuration Video](https://www.youtube.com/watch?v=ggwY9hISHcQ)
- [Hermes Configuration Video](https://www.youtube.com/watch?v=zHKnuWnxt_c)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with concise summaries and inline shell command blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Summarizes the most useful product fields and reports saved output paths when the Gecho MCP tool returns them.]

## Skill Version(s):

1.1.37 (source: server release evidence and artifact/_meta.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
