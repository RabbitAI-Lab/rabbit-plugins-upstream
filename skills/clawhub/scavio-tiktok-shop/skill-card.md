## Description: <br>
Search TikTok Shop products with exact prices, read product details, reviews, the category tree, category and seller catalogs, and resolve any TikTok Shop link to an id. 8 endpoints, all 1 credit. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[scavio-ai](https://clawhub.ai/user/scavio-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, agents, and e-commerce researchers use this skill to query TikTok Shop product, review, category, and seller catalog data through Scavio's structured API. It supports price research, competitor catalog tracking, review mining, and TikTok Shop URL resolution. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Using this skill spends Scavio credits for TikTok Shop lookups. <br>
Mitigation: Confirm that the user intends to use the configured Scavio account before making calls, and avoid unnecessary pagination or repeated detail requests. <br>
Risk: TikTok Shop URLs or lookup targets are processed by Scavio's API. <br>
Mitigation: Avoid sending private or sensitive TikTok links unless the user explicitly intends them to be processed by Scavio. <br>
Risk: Some TikTok Shop product detail calls return normal 404 responses and product detail does not return exact prices. <br>
Mitigation: Treat 404 product-detail responses as expected, use listing endpoints for exact prices, and fall back to reviews only when useful. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/scavio-ai/skills/scavio-tiktok-shop) <br>
- [Scavio TikTok Shop API documentation](https://scavio.dev/docs/tiktok-shop-search) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, code, configuration, text] <br>
**Output Format:** [Markdown guidance with JSON request and response examples plus shell and Python snippets.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires SCAVIO_API_KEY and uses Scavio API credits for TikTok Shop lookups.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
