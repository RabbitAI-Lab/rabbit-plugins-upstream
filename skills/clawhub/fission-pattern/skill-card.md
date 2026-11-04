## Description:

一张商品图裂变成整套素材：根据商品图和卖点生成多角度、多场景的成套商品图片。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce sellers and content creators can turn one product reference image and its selling points into a coordinated set of product shots for listing galleries and detail pages.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reference images, prompts, and optional brand assets are sent to cloud services for image generation.

Mitigation: Avoid confidential assets and review each provider's privacy and retention terms before use.

Risk: Generating multiple images can incur service costs.

Mitigation: Choose the provider explicitly and use --dry-run to review the request and estimated cost before generation.

Risk: The external CLI, linked skills, and service retention practices were outside the supplied security inspection.

Mitigation: Use a reviewed CLI version and review linked tools and provider practices before use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/fission-pattern)
- [Provider CLI reference](references/provider-cli.md)
- [Model flags reference](references/model-flags.md)
- [dLazy CLI](https://github.com/dlazy-ai/cli)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Image files, Prompt text, Shell commands, Guidance]

**Output Format:** [Generated product images (typically JPEG) with Markdown guidance and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [A coordinated multi-image set with consistent product identity and varied angles, scenes, and compositions.]

## Skill Version(s):

1.0.29 (source: frontmatter, server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
