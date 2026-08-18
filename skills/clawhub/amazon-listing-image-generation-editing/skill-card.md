## Description:

使用 Nano Banana Pro 规划和生成 Amazon Listing 图片栈，包括主图、功能证据、尺寸、生活方式、使用步骤与包装清单，并保持 ASIN/SKU 事实一致。

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

Amazon sellers, marketplace operators, and listing content teams use this skill to plan and generate product image stacks for Amazon Listing and A+ content while keeping visuals tied to ASIN/SKU facts, product references, and site policy review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Listing prompts and provided product images are sent to the external AI Hive service.

Mitigation: Use the skill only with product material approved for AI Hive processing, and avoid confidential product data unless the service is approved for that data.

Risk: Generated listing images may drift from real ASIN/SKU facts or current Amazon policy.

Mitigation: Review each generated image against the real product record, supporting evidence, and current Amazon Seller Central policy before publishing.

Risk: API keys are required for authenticated calls and may be stored locally.

Mitigation: Use a dedicated AI Hive API key where possible, prefer environment-based credentials for automation, and keep local configuration files restricted.

## Reference(s):

- [AI Hive API endpoint](https://ai-hive.iclip.cn/api)
- [AI Hive API key setup](https://ai-hive.iclip.cn/chat)
- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/amazon-listing-image-generation-editing)
- [Publisher profile](https://clawhub.ai/user/wubin1836)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Code, Files]

**Output Format:** [Markdown guidance with bash commands, JSON configuration, and generated image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated tasks can download PNG image results to a local output directory; task status can also be returned as JSON.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
