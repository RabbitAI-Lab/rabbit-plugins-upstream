## Description:

Generates conversion-oriented e-commerce main product images with readable Chinese selling-point copy from a product image and concise feature or promotion inputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External e-commerce operators, designers, and agent developers use this skill to turn product photos and verified selling points into square or vertical marketplace main images with concise Chinese copy, category-aware layout, and promotional badges.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local image paths or remote image URLs can be forwarded to external generation providers.

Mitigation: Use only trusted, explicitly selected image inputs; avoid confidential product assets unless the provider data flow is approved; prefer a sandboxed workspace.

Risk: Generated marketing copy or promotional badges can create unsupported product claims or false offers.

Mitigation: Verify product functions and promotions before generation, keep copy concise, and avoid absolute claims such as best, first, or national-level.

Risk: Generated images can alter product appearance or render Chinese text incorrectly.

Mitigation: Compare the output against the source product image, generate batches when appropriate, and inspect a 200 x 200 thumbnail for text legibility before publication.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/item-selling-point)
- [Model flags](references/model-flags.md)
- [Provider CLI reference](references/provider-cli.md)
- [dLazy CLI](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, files]

**Output Format:** [Markdown guidance with bash commands and generated image files saved to disk]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Prompts target 1:1 or 3:4 e-commerce main images, usually at 2k resolution with batch generation for selecting legible Chinese typography.]

## Skill Version(s):

1.0.8 (source: server release and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
