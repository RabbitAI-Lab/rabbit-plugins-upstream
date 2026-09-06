## Description:

Generates on-model product photography by placing accessories such as shoes, bags, watches, glasses, hats, scarves, and jewelry onto a model reference image with natural placement, perspective, and shadows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, ecommerce operators, and creative production teams use this skill to create realistic accessory try-on product images from product photos and model reference images. It supports prompt guidance, parameter choices, dry-run cost checks, and generated image outputs for commercial catalog or merchandising workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product images, model/reference images, prompts, selected local files, or image URLs may be sent to the configured cloud image-generation provider.

Mitigation: Use trusted inputs, avoid sensitive or unauthorized images, review the configured provider, and run dry-run checks when appropriate before generation.

Risk: API keys are required for configured providers and may permit billable generation requests.

Mitigation: Use scoped, revocable credentials, store them through the documented provider configuration, and rotate or revoke keys when access is no longer needed.

Risk: On-model accessory composites could be misused to imply a person's endorsement or to alter a portrait beyond the intended product-placement workflow.

Mitigation: Use the skill only with authorized model/reference images and review outputs for faithful product placement without misleading identity or endorsement claims.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/wear-everything)
- [Provider CLI Reference](artifact/references/provider-cli.md)
- [gpt-image-2 Model Flags](artifact/references/model-flags.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with command examples and optional JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated commands can call cloud image-generation providers, upload image inputs, estimate credits with dry-run, and save resulting image files when executed.]

## Skill Version(s):

1.0.5 (source: server release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
