## Description:

平铺图转隐形模特立体图。平铺图 → 有体积感与版型的立体展示图。当用户说「转 3D」「立体图」「隐形模特」「把衣服撑起来」时使用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce creative teams and developers use this skill to convert flat-lay garment images into ghost-mannequin product images with visible garment volume, preserved material details, and no visible person or mannequin.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Garment images, prompts, and generated outputs may be sent to dLazy or another configured cloud provider.

Mitigation: Use only provider-approved catalog assets, confirm the selected backend with --dry-run before execution, and avoid confidential images unless that provider is approved.

Risk: Unsuitable inputs such as folded garments, heavy wrinkles, people, or multi-item outfits can produce distorted product images.

Mitigation: Use a single flat-lay garment image with clear boundaries, adequate resolution, and the prompt constraints that preserve color, construction, pattern placement, and proportions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/to-3d)
- [Provider CLI reference](references/provider-cli.md)
- [gpt-image-2 model flags](references/model-flags.md)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Files]

**Output Format:** [Markdown guidance with inline shell commands and generated image files saved locally]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return local image paths, generated asset URLs, dry-run payloads, estimated credits, and provider execution metadata.]

## Skill Version(s):

1.0.12 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
