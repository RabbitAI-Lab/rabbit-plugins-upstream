## Description:

Creates social-commerce fashion seeding images by preserving an outfit while changing the model, pose, scene, lighting, and camera style.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and ecommerce content teams use this skill to guide agents in generating lifestyle fashion marketing images from outfit photos and optional model or scene references. It is intended for social-commerce content where garment details should stay faithful while the person, pose, background, and lighting change.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated images may copy a reference person's identity or imply that a real person wore or endorsed a product without consent.

Mitigation: Use only outfit and model/reference photos that the user owns or has permission to use, and avoid real-person likeness transfer or endorsement claims without explicit consent.

Risk: Prompts and images may be uploaded to the configured cloud image provider during generation.

Mitigation: Check the selected provider, credentials, and data-handling requirements before processing personal photos or commercially sensitive images.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/clothing-grass-planting)
- [Provider CLI reference](references/provider-cli.md)
- [gpt-image-2 model flags](references/model-flags.md)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Files]

**Output Format:** [Markdown guidance with bash command examples and generated image file paths]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill commonly produces prompts and commands for image generation workflows that save JPEG image outputs.]

## Skill Version(s):

1.0.3 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
