## Description:

Creates a coordinated set of e-commerce product images from one reference photo and product selling points.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce sellers and creative teams use the skill to plan and generate consistent product listing and detail-page images from a product photo and selling points.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product photos, reference images, and prompts are sent to the selected image-generation provider.

Mitigation: Use the skill only when you are comfortable sending those materials to the selected provider.

Risk: Image cleanup or watermark removal may modify material the user is not authorized to alter.

Mitigation: Use cleanup or watermark-removal guidance only on images you own or are authorized to modify.

Risk: Provider credentials may grant access to paid image-generation services.

Mitigation: Keep provider API keys scoped and revocable.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/fission-pattern)
- [Provider CLI reference](references/provider-cli.md)
- [Image model options](references/model-flags.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Images]

**Output Format:** [Markdown instructions and shell commands; generated JPEG product images when executed]

**Output Parameters:** [1D instructions; multiple image files]

**Other Properties Related to Output:** [Uses a shared product description across varied angles and scenes; image outputs are saved locally.]

## Skill Version(s):

1.0.23 (source: frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
