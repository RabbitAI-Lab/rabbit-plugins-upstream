## Description:

Creates ecommerce product image sets from one product image and selling-point guidance, keeping the product visually consistent across multiple angles, scenes, and compositions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce operators, creative production teams, and agent workflows use this skill to turn one product reference image into a coordinated set of product listing and detail-page images. It provides prompt patterns, command examples, and quality checks for consistent product identity across a generated image set.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product images and prompts may be sent to dlazy or another configured cloud image provider.

Mitigation: Use only product images and prompts that are acceptable for the selected provider, and review provider data handling before using the skill with sensitive assets.

Risk: Generated ecommerce images may drift from the actual product or imply unsupported features.

Mitigation: Compare the full generated set against the reference product image and selling points before publication, rerunning any image that changes shape, color, material, structure, or claims.

Risk: Local CLI execution depends on trusted installation and credential handling.

Mitigation: Install the dlazy CLI from a trusted source, store API keys through the documented configuration path or environment variables, and rotate credentials if exposed.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/fission-pattern)
- [Provider CLI Reference](references/provider-cli.md)
- [gpt-image-2 Model Flags](references/model-flags.md)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with prompt templates, inline shell commands, and optional JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides generation of JPEG ecommerce image files through cloud image providers; users should review generated images for product fidelity before publication.]

## Skill Version(s):

1.0.4 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
