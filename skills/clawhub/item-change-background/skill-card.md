## Description:

商品换背景。白底商品图 -> 逼真场景图，光影与投影匹配新环境。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and ecommerce content teams use this skill to turn plain product photos into photorealistic lifestyle scene images while preserving product shape, color, material, and logo. It supports text-described scenes or an uploaded background image and emphasizes grounded shadows, matched light direction, and plausible reflections.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Untrusted image URLs or provider endpoint overrides could expose source images or API keys.

Mitigation: Use trusted local image files when possible, avoid workflows where untrusted users control image URLs or environment variables, keep provider endpoints official, and use scoped, rotatable keys with spending limits.

Risk: Generated lifestyle scenes may alter product details or imply misleading product capabilities.

Mitigation: Review outputs for product fidelity, logo preservation, grounded shadows, matched lighting, and scene claims before publication.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/item-change-background)
- [gpt-image-2 Parameter Reference](references/model-flags.md)
- [Provider CLI Reference](references/provider-cli.md)
- [dLazy](https://dlazy.com)
- [dLazy CLI Repository](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, code, files]

**Output Format:** [Markdown guidance with inline bash commands, optional JSON command output, and generated image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Typical generated assets are JPEG product-scene images saved to a user-selected output path; dry-run mode can report planned requests and estimated credits without generation.]

## Skill Version(s):

1.0.8 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
