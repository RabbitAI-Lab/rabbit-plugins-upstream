## Description:

已有模特图换模特、换背景。一张模特图 → 多人群多场景版本，商品本身不变。当用户说「换模特」「换背景」「换人种」「一图多版」「同一件衣服换个人」时使用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce teams and developers use this skill to create alternate model or background versions of existing apparel photos while preserving the product. It guides image-editing requests through a selected provider and saves generated images to chosen paths.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Cloud image providers process uploaded photos under provider-specific privacy terms, and requests may incur charges.

Mitigation: Use only photos you are authorized to process, review the selected provider's privacy terms, choose the provider explicitly, and preview with --dry-run before execution.

Risk: A model-only example may also change the background when the intended result is to preserve it.

Mitigation: When the background must remain unchanged, explicitly instruct the provider to preserve it and save the result to a new path.

## Reference(s):

- [Provider CLI Reference](references/provider-cli.md)
- [Model Flags Reference](references/model-flags.md)
- [dLazy CLI Source](https://github.com/dlazy-ai/cli)
- [Related E-commerce Skills](https://github.com/dlazy-ai/ecommerce-skills)

## Skill Output:

**Output Type(s):** [Files, Shell commands, Guidance]

**Output Format:** [JPEG, PNG, or WebP images with Markdown instructions and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated image variants are saved to caller-selected paths; provider, image size, quality, format, and batch count are configurable.]

## Skill Version(s):

1.0.24 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
