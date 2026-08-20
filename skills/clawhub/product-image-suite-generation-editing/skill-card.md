## Description:

用 AI Hive Nano Banana Pro 为同一 SKU 生成和编辑可审核的商品图片套组，把白底主图、场景主图、卖点图、细节图、尺寸图、对比图、生活方式图与本地化图片纳入同一套商品事实和视觉规则。

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce sellers, product photographers, and brand teams use this skill to create consistent SKU image suites for marketplace listings, PDP assets, product cards, and localized promotional visuals. The workflow keeps product facts, reference-image roles, approved claims, and channel-safe layout constraints visible for human review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reference product images selected by the user are uploaded to AI Hive during render mode.

Mitigation: Use only authorized reference images and run brief mode first when you want to inspect the generated prompt without uploading images.

Risk: Generated ecommerce images can misstate product facts, claims, measurements, or channel-specific requirements if not reviewed.

Mitigation: Compare outputs against source images, SKU records, approved claim records, measurement records, and current marketplace rules before publication.

Risk: API credentials are required for generation.

Mitigation: Provide credentials through the documented API key mechanisms and avoid committing real keys in configuration examples or shared artifacts.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/product-image-suite-generation-editing)
- [Publisher profile](https://clawhub.ai/user/wubin1836)
- [AI Hive API endpoint](https://ai-hive.iclip.cn/api)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Files]

**Output Format:** [Markdown guidance with bash commands, generated prompts, JSON task status, and downloaded PNG image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Render mode uploads authorized reference images to AI Hive and can save generated PNG outputs locally; brief mode validates inputs and prints the composed prompt without upload or generation.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
