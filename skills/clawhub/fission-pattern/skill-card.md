## Description:

Turns one ecommerce product image plus selling points into a coherent set of multi-angle, multi-scene product images for storefront main images and detail pages.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce operators, designers, and agent workflows use this skill to expand a single product or model image into a consistent set of product, lifestyle, macro, and comparison shots. It helps prepare image-generation prompts and commands while preserving product identity across the set.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product images, prompts, and optional brand reference images may be sent to the configured third-party image-generation provider.

Mitigation: Confirm the selected provider and data handling expectations before use, and avoid submitting sensitive or unreleased product assets unless the provider is approved.

Risk: Generated scenes can drift from the original product or imply features that are not present.

Mitigation: Reuse a precise product-fidelity prompt segment, review the resulting set side by side, and rerun individual images that alter shape, color, material, structure, or claims.

Risk: Running image generation can incur cost or fail because credentials, CLI installation, or credits are missing.

Mitigation: Use dry-run for request and cost checks, prefer pinned and trusted CLI installs, and verify provider credentials before batch generation.

## Reference(s):

- [Provider CLI Reference](references/provider-cli.md)
- [gpt-image-2 Model Flags](references/model-flags.md)
- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/fission-pattern)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Files, Guidance]

**Output Format:** [Markdown guidance with bash commands; generated image assets are saved as files such as JPEG outputs.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses one or more reference images, a reusable product-fidelity prompt segment, and per-shot camera or scene variations.]

## Skill Version(s):

1.0.13 (source: evidence release and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
