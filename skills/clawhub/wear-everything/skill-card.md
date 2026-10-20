## Description:

Turns product photos of shoes, bags, and accessories into realistic images of a person wearing or carrying them using a model reference image.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Merchants and creative teams use product and model reference images to create on-model ecommerce photos of shoes, bags, eyewear, jewelry, and other accessories.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Cloud image providers receive submitted prompts and product or model images.

Mitigation: Submit only images and prompts you are authorized to share with the selected provider.

Risk: The bundled helper can invoke unrelated tasks, including watermark removal.

Mitigation: Review the helper before installation; use the documented wear-everything task and avoid watermark removal without a legitimate, rights-cleared purpose.

Risk: Generated images may change a product or a person's appearance or imply an endorsement.

Mitigation: Check product fidelity and model likeness before publishing; do not fabricate another person's endorsement.

## Reference(s):

- [ClawHub release](https://clawhub.ai/dlazyai/skills/wear-everything)
- [Provider and authentication guide](artifact/references/provider-cli.md)
- [Image generation options](artifact/references/model-flags.md)

## Skill Output:

**Output Type(s):** [Image files, Shell commands, Guidance]

**Output Format:** [JPEG images with Markdown instructions and command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports multiple product views and reference images; results require visual review for placement and product fidelity.]

## Skill Version(s):

1.0.24 (source: frontmatter and ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
