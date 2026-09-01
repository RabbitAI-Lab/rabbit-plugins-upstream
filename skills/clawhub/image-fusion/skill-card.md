## Description:

多单品融合成一整套 Look。最多 8 张单品图 → 同一模特身上的完整搭配商拍图，每件单品保真。当用户说「多件搭配」「融图」「组一套 look」「搭配图」「几件衣服合成一张」时使用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and ecommerce operators use this skill to combine up to eight product images into a complete outfit image on one model for catalog or storefront imagery. Developers and agents can use its prompt templates and commands to prepare repeatable image-fusion runs with consistent styling.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and supplied images may be sent to dLazy or another configured generation provider.

Mitigation: Use the skill only with material approved for the selected provider, avoid sensitive images, and confirm provider configuration before execution.

Risk: The bundled runner can fetch arbitrary URLs and supports generation tasks beyond image-fusion.

Mitigation: Run with --dry-run first, prefer vetted local image files, and invoke only the image-fusion task unless the extra behavior is intentional.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/image-fusion)
- [Provider CLI reference](references/provider-cli.md)
- [seedream-5.0 model flags](references/model-flags.md)
- [dLazy product site](https://dlazy.com)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Files]

**Output Format:** [Markdown guidance with inline shell commands and generated image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports dry-run cost checks, batched image generation, local output paths, and optional brand configuration.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
