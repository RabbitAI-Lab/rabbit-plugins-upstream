## Description:

基于图片 URL 在 8 个 Amazon 站点检索视觉相似商品，并返回 ASIN、标题、图片、价格、评分、评论数、品牌和可选 Keepa 数据。

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, researchers, and ecommerce operators use this skill to find visually similar Amazon listings across supported marketplaces for product discovery, competitor comparison, sourcing alternatives, and counterfeit investigation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uploads local images to obtain public URLs and may handle product images outside the local workspace.

Mitigation: Use only non-sensitive product images and confirm with the user before uploading any local file.

Risk: Authentication and billing flows may involve API keys, phone-based setup, credit balance checks, and payment orders.

Mitigation: Prefer self-service API-key setup through LinkFox, avoid asking an agent to handle phone numbers or SMS codes, and confirm paid or credit-consuming actions before continuing.

Risk: Custom LinkFox endpoint environment variables can redirect API calls away from the default service.

Mitigation: Avoid custom LinkFox endpoint variables unless the destination is explicitly trusted.

Risk: Search results, cached API data, and payment QR assets may be saved locally under a linkfox directory.

Mitigation: Review local output paths and avoid running the skill with sensitive images or confidential product data.

## Reference(s):

- [API reference](references/api.md)
- [Authentication and billing onboarding](references/onboarding.md)
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-amazon-search-by-image)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown summaries and tables, JSON response files, and shell commands for API use, upload, authentication, and billing flows.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Full API responses are saved locally under a linkfox session directory; large responses are summarized unless inline output is requested.]

## Skill Version(s):

1.0.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
