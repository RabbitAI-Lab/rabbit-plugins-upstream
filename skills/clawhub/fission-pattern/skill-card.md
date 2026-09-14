## Description:

Generates a cohesive e-commerce image set from one product image and selling points, covering multiple angles, scenes, and detail shots while preserving product identity.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, marketers, and developers use this skill to turn a single product or outfit image plus selling points into a set of product, lifestyle, macro, and comparison images for e-commerce listings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product images, prompts, and provider credentials may be sent to configurable external AI services.

Mitigation: Install only when that data flow is acceptable; use images you own or are licensed to modify, and verify provider-related environment variables before running.

Risk: The scripts can fetch user-provided web image URLs.

Mitigation: Prefer local files or trusted public HTTPS URLs, and avoid private network or localhost URLs.

Risk: Generated product imagery may drift from the source product or imply unsupported selling points.

Mitigation: Review each generated image before publication and keep the prompt's product-fidelity and no-false-claims constraints intact.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/fission-pattern)
- [Provider CLI Reference](references/provider-cli.md)
- [gpt-image-2 Model Flags](references/model-flags.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Generated image files]

**Output Format:** [Markdown guidance with bash command examples and optional JSON command output; generated assets are saved image files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses one reference product image across multiple prompts; default task settings target 1024x1536 JPEG output at medium quality.]

## Skill Version(s):

1.0.9 (source: SKILL.md frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
