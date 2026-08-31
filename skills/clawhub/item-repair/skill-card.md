## Description:

Retouches ecommerce product photos into listing-ready images by reducing random wrinkles, straightening layout, evening lighting, and cleaning backgrounds while preserving product style, color, materials, and structure.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce operators, creative teams, and agent users use this skill to prepare product photos for storefront listings by generating retouching prompts and image-generation commands for item repair workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected product photos, prompts, and provider credentials may be sent to cloud image services during generation.

Mitigation: Use only approved provider accounts and credentials, avoid sensitive or embargoed product images, and review the provider data flow before execution.

Risk: Ambiguous requests for general photo fixing may trigger ecommerce product retouching outside the user's intent.

Mitigation: Confirm the user wants product-photo repair before running the workflow, especially when the request does not clearly mention ecommerce listing images.

Risk: Retouching can unintentionally hide product defects or alter truthful product presentation.

Mitigation: Preserve real damage, stains, material texture, structure, color, logos, and hardware positions; use prompts that prohibit removing product defects.

Risk: Cloud generation can consume credits or run with an unintended payload.

Mitigation: Use dry-run mode to inspect payloads and estimated cost before paid generation when checking setup, routing, or batch behavior.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/item-repair)
- [Provider CLI reference](artifact/references/provider-cli.md)
- [gpt-image-2 model flags](artifact/references/model-flags.md)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance, Image files]

**Output Format:** [Markdown guidance with inline shell commands and generated image file paths or URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The documented workflow can dry-run requests, estimate credits, upload selected product images to cloud providers, and save generated JPEG outputs.]

## Skill Version(s):

1.0.3 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
