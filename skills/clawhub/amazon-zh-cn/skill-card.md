## Description:

通过官方 Gecho Bridge MCP 搜索 Amazon 商品、获取已知商品详情并采集商品评论。适用于市场发现、商品库调研、商品比较、评论分析和 ASIN 级研究。

This skill is ready for commercial/non-commercial use.

## Publisher:

[gecho-ai](https://clawhub.ai/user/gecho-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce researchers, sellers, and agent users use this skill to route Amazon keyword search, product detail lookup, and review collection requests through Gecho Bridge. It supports market discovery, product comparison, ASIN-level research, and concise summaries of returned product and review data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on Gecho Bridge, the Gecho Chrome extension, and a logged-in Amazon browser session; missing login state, challenges, region prompts, or rate limits may cause workflows to fail.

Mitigation: Confirm the user is comfortable using Gecho Bridge and its Chrome extension with a logged-in Amazon session, and have the user resolve Amazon login, captcha, region, cookie, or rate-limit prompts manually before retrying.

Risk: Product and review research results may be written to local JSON files when save_dir is used.

Mitigation: Use save_dir only for user-approved directories and handle saved Amazon product or review data according to the user's storage and sharing requirements.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/gecho-ai/skills/amazon-zh-cn)
- [Gecho Bridge README](https://github.com/gecho-ai/gecho-bridge/blob/main/README.md)
- [Gecho Bridge GitHub Repository](https://github.com/gecho-ai/gecho-bridge)
- [Gecho Chrome Extension](https://chromewebstore.google.com/detail/pjkaeenpekolahdbccjfenjcmanemlbj?utm_source=item-share-cb)
- [Gecho Website](https://gecho.ai/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance and summaries with optional shell command blocks and local JSON result paths.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can direct official Gecho MCP tools to save Amazon product and review research results as local JSON files when an approved save_dir is provided.]

## Skill Version(s):

1.1.37 (source: server release evidence and artifact _meta.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
