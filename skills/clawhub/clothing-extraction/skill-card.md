## Description:

从任意图提取干净商品平铺图。真人图 / 街拍图 → 白底平铺商品图。当用户说「提取衣服」「扒图」「转平铺」「抠成商品图」「从买家秀提取」时使用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External e-commerce sellers and image editors use the skill to turn model, street-style, or customer photos into clean flat-lay product images.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The reported workflow sends source photos to external image services, which may expose personal or third-party image data.

Mitigation: Get authorization before using personal or third-party photos and review the selected provider's privacy terms.

Risk: Analysis of some files was incomplete, so the scan cannot establish that all portions are safe.

Mitigation: Review uninspected files and confirm the runtime permissions before installing or using the skill.

## Reference(s):

- [Provider CLI reference](references/provider-cli.md)
- [gpt-image-2 model flags](references/model-flags.md)
- [Related flat-lay skill](https://github.com/dlazy-ai/ecommerce-skills/blob/main/skills/flat-lay/skill.md)
- [Related to-3d skill](https://github.com/dlazy-ai/ecommerce-skills/blob/main/skills/to-3d/skill.md)
- [Related fabric-on-body skill](https://github.com/dlazy-ai/ecommerce-skills/blob/main/skills/fabric-on-body/skill.md)

## Skill Output:

**Output Type(s):** [Files (generated product images), Guidance, Shell commands]

**Output Format:** [JPEG or PNG flat-lay product images, with Markdown instructions and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Image appearance depends on source quality; details hidden by occlusion may be inferred and should be checked.]

## Skill Version(s):

1.0.35 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
