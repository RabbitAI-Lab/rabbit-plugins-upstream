## Description:

使用 GPT Image 2 生成可上架的产品图与商品摄影套图，包括白底主图、场景图、材质细节、尺寸留白、使用步骤、包装清单和SKU系列。

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External merchants, ecommerce operators, and listing teams use this skill to generate product-photo prompts and commands for white-background main images, usage scenes, material details, package contents, and SKU color variants from approved product references.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends selected product reference images and prompts to the external AI Hive service.

Mitigation: Use only source materials approved for external processing and avoid uploading confidential or restricted product assets unless the service is approved for that data.

Risk: Generated product images may misstate regulated or precise product facts such as certifications, dimensions, ingredients, or medical and beauty claims.

Mitigation: Use approved source materials for those claims, add them in post-production when needed, and require human review before publication.

Risk: The AI Hive API key may be stored locally or provided through the environment.

Mitigation: Store the key in the documented local configuration or environment variable with restricted access and rotate it if exposure is suspected.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/gpt-image-2-product-image)
- [ClawHub publisher profile](https://clawhub.ai/user/wubin1836)
- [AI Hive API endpoint](https://ai-hive.iclip.cn/api)
- [AI Hive API key setup](https://ai-hive.iclip.cn/chat)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline bash code blocks and local configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces prompts and commands that call AI Hive, upload selected reference images, poll generation tasks, and save generated image files to the configured output directory.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
