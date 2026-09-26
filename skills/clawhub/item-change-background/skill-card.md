## Description:

商品换背景。白底商品图 → 逼真场景图，光影与投影匹配新环境。当用户说「换背景」「加场景」「白底转场景」「放到桌面上」时使用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce and creative production teams use this skill to turn plain-background product images into photorealistic lifestyle scene images while preserving product shape, color, material, and logo details. Agents use it to prepare prompts, provider settings, and generation commands for product background replacement workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product images, background references, and prompts may be sent to the configured image-generation provider.

Mitigation: Check which provider will be selected and use only providers approved for the product assets being processed.

Risk: Generation commands can perform paid remote image-generation work and save outputs locally.

Mitigation: Use doctor or dry-run commands before paid generation and confirm output paths before running batch jobs.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/dlazyai/skills/item-change-background)
- [Provider CLI reference](references/provider-cli.md)
- [gpt-image-2 parameter reference](references/model-flags.md)
- [dLazy CLI](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, files]

**Output Format:** [Markdown guidance with bash command examples and locally saved image outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated outputs are saved as image files; typical defaults use JPEG with 1024x1024 or 1024x1536 sizing and optional batch variants.]

## Skill Version(s):

1.0.13 (source: frontmatter and server evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
