## Description:

Retouches product photos into listing-ready images by reducing random wrinkles, straightening layout, evening lighting, and cleaning backgrounds while preserving product structure and color.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce sellers, catalog operators, and agents use this skill to prepare product photos for listings by producing retouching prompts and generation commands that preserve the original product while improving presentation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected product photos, prompts, and supplied image URLs may be sent to the configured cloud generation provider.

Mitigation: Use explicit local files or trusted URLs, run dry-run checks before paid execution, and avoid confidential images or internal URLs unless that provider transfer is acceptable.

Risk: Image retouching can unintentionally alter product structure, color, hardware, structural folds, texture, or visible defects.

Mitigation: Use preservation prompts, avoid removing actual defects, and compare source and output images before using the result in a listing.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/item-repair)
- [Provider CLI reference](artifact/references/provider-cli.md)
- [gpt-image-2 model flags](artifact/references/model-flags.md)
- [dLazy CLI](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration, files]

**Output Format:** [Markdown guidance with bash commands, optional JSON command output, and generated image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports dry-run previews, one to four input images for the same product, and saved JPEG outputs or provider-hosted asset URLs.]

## Skill Version(s):

1.0.4 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
