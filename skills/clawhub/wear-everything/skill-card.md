## Description:

Creates photorealistic on-model commercial images by placing shoes, bags, watches, glasses, hats, scarves, jewelry, and other accessories from product photos onto a model reference while preserving placement, perspective, shadows, and product details.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External e-commerce sellers, creative operators, and developers use this skill to produce accessory-on-model product imagery from product photos and model reference images. It helps generate candidate JPEG outputs and command workflows for shoes, bags, eyewear, watches, hats, scarves, jewelry, and similar accessories.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product photos, model/reference images, and prompts may be sent to the selected image provider.

Mitigation: Use --dry-run first, choose the provider intentionally, and avoid private or sensitive photos unless that provider's terms are acceptable.

Risk: Generated accessory-on-model imagery could imply a person is wearing or endorsing a product.

Mitigation: Use only authorized model/reference images and do not use the workflow to forge personal endorsements.

Risk: Generated images may contain inaccurate placement, scale, reflections, shadows, duplicate accessories, or unintended face and background changes.

Mitigation: Review outputs before use and regenerate with stronger placement, scale, reflection, and unchanged-region constraints when needed.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/wear-everything)
- [Provider CLI Reference](references/provider-cli.md)
- [gpt-image-2 Parameter Reference](references/model-flags.md)
- [Brand Configuration Example](examples/brand.yaml)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Code, Files]

**Output Format:** [Markdown guidance with bash commands and JSON-capable CLI output; executed workflows save JPEG image files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses product and model/reference images as inputs; image data may be sent to the intentionally selected image provider.]

## Skill Version(s):

1.0.13 (source: server release and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
