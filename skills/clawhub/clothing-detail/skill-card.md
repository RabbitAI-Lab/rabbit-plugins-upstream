## Description:

Guides agents in creating photorealistic close-ups of garment details from product photos for e-commerce pages.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce teams and designers use this skill to prepare prompts and commands for close-up product images showing garment features such as collars, seams, and fabric texture.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected garment images and prompts are sent to the configured cloud image provider.

Mitigation: Use --dry-run to review requests, choose the provider explicitly when needed, and exclude private or unrelated local files.

Risk: Generated close-ups can depict garment details that are not visible in the source photo.

Mitigation: Start with a clear source image and check the result against the actual garment before publishing.

## Reference(s):

- [Clothing Detail release on ClawHub](https://clawhub.ai/dlazyai/skills/clothing-detail)
- [Provider CLI guide](artifact/references/provider-cli.md)
- [Image model options](artifact/references/model-flags.md)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Image files]

**Output Format:** [Markdown guidance and commands; generated JPEG images]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Square or portrait images; provider usage may incur charges.]

## Skill Version(s):

1.0.17 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
