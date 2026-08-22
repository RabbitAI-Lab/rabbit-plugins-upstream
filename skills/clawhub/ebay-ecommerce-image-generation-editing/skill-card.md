## Description:

Create and edit eBay listing images for new, used, refurbished, parts and collectible items, including condition disclosure, defects, identifiers, included accessories and scale; supports eBay商品图、二手商品、翻新机、藏品、配件清单、瑕疵展示、序列号处理、汽配兼容、跨境Listing, and AI Hive reference editing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, listing operators, and agent developers use this skill to generate and edit eBay product images that preserve exact-item condition evidence, defects, accessories, identifiers, and scale for new, used, refurbished, parts, and collectible listings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected product photos are uploaded to AI Hive/Object Storage for image generation or editing.

Mitigation: Upload only photos intended for processing, and redact private identifiers before upload unless they are necessary for the listing evidence.

Risk: The AI Hive API key may be stored locally in the user's home directory.

Mitigation: Protect local configuration files, prefer scoped keys where available, and rotate or remove keys that are no longer needed.

Risk: Generated listing imagery can misrepresent the exact sale item if defects, missing parts, authenticity, grade, warranty, or test results are altered.

Mitigation: Review each output against the source item photos and current eBay category/image policies before publishing.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/wubin1836/skills/ebay-ecommerce-image-generation-editing)
- [Publisher Profile](https://clawhub.ai/user/wubin1836)
- [AI Hive API](https://ai-hive.iclip.cn/api)
- [AI Hive API Access](https://ai-hive.iclip.cn/chat)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance with bash commands, JSON/API responses, and generated image files downloaded by the helper script.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated outputs depend on user prompts, reference images, AI Hive model routing, and task completion status.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
