## Description:

从任意图提取干净商品平铺图。真人图 / 街拍图 → 白底平铺商品图。当用户说「提取衣服」「扒图」「转平铺」「抠成商品图」「从买家秀提取」时使用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce sellers and creative teams use this skill to turn a photo of a person wearing clothing into a clean, white-background flat-lay image of a selected garment. It can also prepare garment images as inputs for related product-visual workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Personal or confidential source photos may be sent to external image providers.

Mitigation: Review the privacy implications before use and avoid submitting photos unless their use with the configured provider is appropriate.

Risk: The security review reports broader text and video generation capabilities than clothing extraction and says some referenced content was only partially inspected.

Mitigation: Review the reported capabilities and unresolved content before installing or using the skill.

## Reference(s):

- [Provider and data-flow reference](references/provider-cli.md)
- [Image model flags](references/model-flags.md)
- [Related flat-lay skill](https://github.com/dlazy-ai/ecommerce-skills/blob/main/skills/flat-lay/skill.md)
- [Related to-3d skill](https://github.com/dlazy-ai/ecommerce-skills/blob/main/skills/to-3d/skill.md)
- [Related fabric-on-body skill](https://github.com/dlazy-ai/ecommerce-skills/blob/main/skills/fabric-on-body/skill.md)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Images, Shell commands, Image-generation guidance]

**Output Format:** [JPEG or PNG image files, with prompts and invocation examples in Markdown and shell code blocks]

**Output Parameters:** [Single selected garment per generation request; optional batch of 2–3 variants]

**Other Properties Related to Output:** [Typically a 1024×1024 square flat-lay on a white background. Details hidden by occlusion may be inferred and should be manually checked.]

## Skill Version(s):

1.0.36 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
