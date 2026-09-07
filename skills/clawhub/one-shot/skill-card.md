## Description:

Guides agents to turn an existing ecommerce model or mannequin photo into variants with a replaced model, background, or both while keeping the garment unchanged.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce operators and creative production teams use this skill to generate market-specific model and background variants from an existing apparel photo while preserving the product's color, cut, logo placement, folds, and framing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and source images may be sent to the selected image provider.

Mitigation: Use only images and prompts approved for the chosen provider, and avoid sensitive or confidential source imagery unless the provider is approved for that data.

Risk: Helper code can fetch arbitrary image URLs, which may expose protected internal services if used in a sensitive network environment.

Mitigation: Prefer local image files or trusted public image URLs, and avoid running the skill in environments with access to sensitive internal web services.

Risk: A configurable Ark endpoint could receive the Ark API key if ARK_BASE_URL is set to an untrusted endpoint.

Mitigation: Leave ARK_BASE_URL unset or set it only to a trusted HTTPS endpoint controlled by the user or organization.

Risk: Model and background replacement could be misused to imply a real person's endorsement or identity use.

Mitigation: Use authorized model imagery only, do not target specific real people without rights, and do not create fake endorsements.

Risk: The bundled task list includes watermark-removal behavior that may be inappropriate for unauthorized images.

Mitigation: Use watermark-removal functionality only for images the user is authorized to edit.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/one-shot)
- [Provider CLI Reference](references/provider-cli.md)
- [gpt-image-2 Parameter Reference](references/model-flags.md)
- [dLazy CLI Source](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Files]

**Output Format:** [Markdown guidance with bash command examples and image generation parameters; executed commands can save image files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses one source model or mannequin image, optional pose or model-face references, and provider-specific image generation settings.]

## Skill Version(s):

1.0.6 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
