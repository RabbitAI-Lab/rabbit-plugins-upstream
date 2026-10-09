## Description:

Combines up to eight product photos into a coordinated e-commerce image of a single model wearing the complete look.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce teams and creators use the skill to plan and generate coordinated product-look photos from separate clothing and accessory images.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product, model, or reference images and prompts may be sent to a selected cloud provider.

Mitigation: Choose an approved provider deliberately and avoid submitting private or sensitive images without authorization; use --doctor or --dry-run before generating.

Risk: Generated looks may omit products or change their colors, patterns, or layering.

Mitigation: Review each output against the source images and product list before publishing; regenerate or revise the prompt when details differ.

## Reference(s):

- [Image Fusion release on ClawHub](https://clawhub.ai/dlazyai/skills/image-fusion)
- [Provider CLI and data flow](references/provider-cli.md)
- [Model flags](references/model-flags.md)
- [dLazy CLI](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Image files]

**Output Format:** [Markdown instructions and generated JPEG images]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports up to eight product images and optional pose or model references; generated images can be saved locally.]

## Skill Version(s):

1.0.18 (source: frontmatter and ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
