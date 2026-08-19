## Description:

用 AI Hive Nano Banana Pro 把已授权商品图换成白底、生活方式、节日、门店或广告场景，同时锁定商品轮廓、结构、材质、Logo 与比例，并明确相机透视、光线、接触阴影、反射和遮挡关系。

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce sellers, photographers, and brand teams use this skill to generate commercial product background replacements and scene composites for marketplace, social commerce, listing, and advertising assets while preserving product identity details.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected product and background images, prompts, and task metadata are sent to AI Hive.

Mitigation: Use only approved, non-sensitive, properly licensed images and review the preview command before submitting a generation task.

Risk: The skill stores an AI Hive API key for local CLI use when auth is run.

Mitigation: Store the API key only on trusted machines and prefer environment-based credentials when appropriate.

Risk: Generated commercial composites may alter visual context around products or people.

Mitigation: Compare outputs against the original product references, verify labels and logos, and confirm any hand or model imagery is authorized before publication.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/product-background-replacement-commercial)
- [AI Hive API endpoint referenced by the artifact](https://ai-hive.iclip.cn/api)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance with bash command examples; CLI preview text, JSON task status, and generated PNG files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uploads selected product and background images to AI Hive and saves completed image results locally by default.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
