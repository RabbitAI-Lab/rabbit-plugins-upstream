## Description:

Retouches casual product photos into listing-ready images by reducing random wrinkles, straightening layout, evening lighting, and cleaning the background while preserving style, color, patterns, hardware, and structure.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, ecommerce operators, and agents use this skill to prepare product photos for listings by generating retouching prompts and commands that preserve product identity while improving layout, lighting, and background cleanliness.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product photos, prompts, and optional brand-reference assets may be uploaded to dLazy or a selected third-party provider.

Mitigation: Use the skill only for user-confirmed product-photo retouching, avoid sensitive or unreleased imagery unless provider terms allow it, and use dry-run or explicit provider settings when auditing data flow.

Risk: Image edits may unintentionally alter product structure, color, defects, or other listing-relevant details.

Mitigation: Compare the generated result with the source images before publication, preserve product identity in prompts, and do not use retouching to hide holes, stains, damage, or other material defects.

## Reference(s):

- [Item Repair skill page](https://clawhub.ai/dlazyai/skills/item-repair)
- [Provider CLI reference](references/provider-cli.md)
- [gpt-image-2 model flags](references/model-flags.md)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [Material enhancement companion skill](https://github.com/dlazy-ai/ecommerce-skills/blob/main/skills/material-enhancement/skill.md)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, files]

**Output Format:** [Markdown guidance with bash commands and generated image file paths or URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses 1-4 product images with prompt, size, quality, batch, provider, and save-path options; outputs are typically saved JPEG files.]

## Skill Version(s):

1.0.13 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
