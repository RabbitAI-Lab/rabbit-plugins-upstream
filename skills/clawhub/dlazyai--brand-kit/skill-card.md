## Description:

店铺品牌视觉锁定。一份 brand.yaml 定义模特、色温、构图、留白与文案语气，所有生图技能读它，保证跨 SKU 视觉统一。当用户说「统一风格」「同一个模特」「店铺调性」「品牌规范」「几百个 SKU 看起来像一家店」时使用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

电商店铺运营者和商品内容团队可用一份可复用的品牌规范统一不同 SKU 的模特、色调、构图和文案风格，并将规范用于图像生成流程。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generation requests may send prompts and reference images to external providers.

Mitigation: Review the selected provider's data handling before use; do not send sensitive images or product information unless approved.

Risk: Provider access uses API credentials, including credentials supplied through environment variables.

Mitigation: Use dedicated credentials, keep keys out of prompts and brand files, and rotate exposed keys.

Risk: The security assessment reports a possible configuration overwrite and partial inspection of some files.

Mitigation: Review output paths and inspect the files before use; back up configuration that may be affected.

## Reference(s):

- [brand-schema.md](references/brand-schema.md)
- [provider-cli.md](references/provider-cli.md)

## Skill Output:

**Output Type(s):** [Configuration, Shell commands, Prompt text, Guidance]

**Output Format:** [YAML configuration and Markdown guidance with shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Brand settings can be appended to image-generation prompts; commands may save generated image files.]

## Skill Version(s):

1.0.30 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
