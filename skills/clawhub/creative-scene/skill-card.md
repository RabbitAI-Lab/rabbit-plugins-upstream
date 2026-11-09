## Description:

从零创意生图，也可定向改模特、姿势、搭配。一句描述（可选参考图）→ 图。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators and ecommerce content teams use this skill to create images from text prompts or revise a reference image's model, pose, or outfit.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and reference images may be sent to an external image-generation provider.

Mitigation: Before use, review the selected provider's data handling and avoid sending prompts or images that should remain private.

Risk: The security review is incomplete: only 55.6% of components were fully scanned, and scanners raised privacy, tool-scope, and purpose-mismatch concerns.

Mitigation: Treat this as a review warning, inspect the skill and its provider access before installation, and confirm that its observed behavior matches the intended image-generation use.

## Reference(s):

- [Provider CLI reference](references/provider-cli.md)
- [Image model flags](references/model-flags.md)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Images, Guidance, Shell commands]

**Output Format:** [Generated image files, prompt guidance, and shell commands]

**Output Parameters:** [1D (prompt with optional reference images)]

**Other Properties Related to Output:** [Image aspect ratio, size, and batch count are configurable.]

## Skill Version(s):

1.0.30 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
