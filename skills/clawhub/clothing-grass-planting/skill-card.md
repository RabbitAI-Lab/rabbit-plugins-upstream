## Description:

同款穿搭换模特换场景做种草图，将穿搭图转换为社交平台风格的种草图。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators and ecommerce teams can use this skill to create lifestyle social-commerce images that retain an outfit while changing the model, pose, setting, and lighting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Input photos and prompts are sent to a cloud image provider, whose retention practices are not independently verified.

Mitigation: Choose the provider explicitly, avoid submitting sensitive photos or prompts, and review that provider's retention terms.

Risk: Batch generation can increase costs and create multiple files at the selected output paths.

Mitigation: Preview with --dry-run, check the batch size and output paths, and confirm costs before generating.

## Reference(s):

- [Provider setup and data flow](references/provider-cli.md)
- [Image model options](references/model-flags.md)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Images, Prompts, Shell commands, Guidance]

**Output Format:** [Generated image files (JPEG by default) and accompanying prompt or command text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Portrait social-media images; size and batch count can be configured.]

## Skill Version(s):

1.0.28 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
