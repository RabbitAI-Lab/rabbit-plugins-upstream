## Description:

材质质感增强与纹理重建。糊掉的图 + 高清商品图 → 纹理清晰可信的图。当用户说「增强质感」「图糊了」「补纹理」「提清晰度」时使用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, ecommerce creative teams, and developers use this skill to improve clothing material texture in product images while preserving the model, pose, background, garment shape, and color. It guides an agent through prompt construction and cloud image-editing commands using an original image plus a high-resolution product reference.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow may send prompts and supplied product or model images to dLazy or another configured image provider.

Mitigation: Use only providers approved for the workflow, avoid confidential imagery unless that provider is approved, and review provider data handling before execution.

Risk: Image generation can consume paid credits or provider quota.

Mitigation: Run with --dry-run first to inspect the selected provider, request payload, and estimated cost before executing paid generation.

Risk: Using a mismatched or low-quality product reference can transfer the wrong material texture or fail to preserve the intended garment.

Mitigation: Confirm the original and high-resolution product image are the same item, meet the documented size and resolution constraints, and compare outputs against the source image before use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/material-enhancement)
- [Provider CLI reference](references/provider-cli.md)
- [gpt-image-2 parameter list](references/model-flags.md)
- [dLazy](https://dlazy.com)
- [dLazy CLI](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration, files]

**Output Format:** [Markdown guidance with bash commands and saved image file outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports dry-run inspection, provider selection, high-quality JPEG image editing, optional batch generation, and local output paths.]

## Skill Version(s):

1.0.10 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
