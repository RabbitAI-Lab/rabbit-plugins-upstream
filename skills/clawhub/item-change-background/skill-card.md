## Description:

Helps agents turn plain-background product images into photorealistic lifestyle scenes while preserving the product's shape, color, material, and logo.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External commerce teams, designers, and developers use this skill to prepare product-image background replacement prompts and commands for realistic storefront or lifestyle imagery. It supports text-described scenes and uploaded background images while emphasizing grounded shadows, consistent lighting, and faithful product details.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unsafe image inputs can cause arbitrary local files or fetched URLs to be sent to external image providers.

Mitigation: Use only trusted product-image and background paths, avoid private or internal URLs, and run the skill from a constrained project directory.

Risk: Prompts, selected images, and generated outputs may be processed by configured third-party providers.

Mitigation: Use provider credentials and image assets that are approved for this workflow, and avoid sensitive or confidential product materials unless provider use is acceptable.

Risk: Paid image generation can incur cost or consume credits.

Mitigation: Use dry-run mode to inspect requests and estimated cost before running paid generation.

Risk: Generated product scenes can become misleading if the scene implies unsupported product properties or use cases.

Mitigation: Review final images for truthful product placement and avoid scenes that imply capabilities not present in the original product.

## Reference(s):

- [Provider CLI reference](references/provider-cli.md)
- [gpt-image-2 parameter reference](references/model-flags.md)
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/item-change-background)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with prompt templates, command examples, and configuration notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands may invoke configured image providers and save generated image files such as JPEG outputs.]

## Skill Version(s):

1.0.9 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
