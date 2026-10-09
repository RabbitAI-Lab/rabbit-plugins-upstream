## Description:

Turns one product reference image and its selling points into a coordinated set of e-commerce images with varied angles and scenes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce sellers and creative teams use a single product photo and stated selling points to plan and generate coordinated hero, lifestyle, detail, and comparison images for listings or product pages.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product prompts and reference images are sent to the selected external image provider or dLazy.

Mitigation: Use only images you are comfortable sharing with that provider and check its data handling before running.

Risk: Generating multiple images may incur unexpected request costs or overwrite assets at chosen paths.

Mitigation: Run dry-run to review requests and estimated cost, then choose explicit output paths.

Risk: Generated images may drift from the original product or imply unsupported claims; watermark-removal guidance can affect rights-managed content.

Mitigation: Review the complete set against the source product and claims, and edit watermarks only on content you own or have permission to modify.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/fission-pattern)
- [Image model options](references/model-flags.md)
- [Provider setup and data flow](references/provider-cli.md)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Image files]

**Output Format:** [Markdown guidance and commands; generated images saved as JPEG files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generates a coordinated multi-image set, typically five listing images; image generation uses a selected external provider.]

## Skill Version(s):

1.0.18 (source: release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
