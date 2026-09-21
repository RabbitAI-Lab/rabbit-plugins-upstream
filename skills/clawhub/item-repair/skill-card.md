## Description:

Retouches ecommerce product photos by reducing wrinkles, straightening layout, evening lighting, and cleaning backgrounds while preserving the product's style, color, patterns, hardware, and structure.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce sellers, marketplace operators, and content teams use this skill to turn casual product photos into listing-ready images. It is especially suited to flat-lay garments or single-product images that need wrinkle removal, lighting cleanup, background purification, and prompt guidance that preserves product identity.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected product photos and prompts may be sent to dLazy or to another configured cloud provider.

Mitigation: Use only approved provider keys, pass explicit trusted image paths or URLs, and avoid private customer data or confidential product images unless that provider is approved for the data.

Risk: Image generation can incur provider costs, especially with high quality and batch settings.

Mitigation: Run the documented dry-run mode first to inspect the request and estimate cost before executing paid generation.

Risk: Retouching may unintentionally alter product structure, hide defects, or smooth important material texture.

Mitigation: Use the preservation prompts and compare output against the source image before publishing; do not use the skill to hide product damage or misrepresent the item.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/item-repair)
- [Provider CLI reference](references/provider-cli.md)
- [gpt-image-2 model flags](references/model-flags.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions, Files]

**Output Format:** [Markdown guidance with bash examples; generated JPEG image files when executed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports dry-run cost estimation, one to four same-product input images, high-quality image generation, batch fan-out, and saved local output paths.]

## Skill Version(s):

1.0.11 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
