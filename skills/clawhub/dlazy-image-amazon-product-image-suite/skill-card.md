## Description:

A professional product image generation skill purpose-built for the Amazon e-commerce platform.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce sellers and creative teams use this skill to plan and generate Amazon product listing images, including a main image, secondary images, and A+ content modules.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill documents a CLI login flow that stores an API key in the local dLazy configuration; the security scan reports a login finding with incomplete coverage of referenced material.

Mitigation: Review the CLI authentication behavior before logging in, use credentials only for the intended account, and rotate or revoke a key if needed.

Risk: The skill says prompts and local image, video, or audio files supplied for generation are sent to dLazy hosted services for processing or storage.

Mitigation: Only submit prompts and media that are authorized for cloud processing, and avoid including sensitive files.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/dlazyai/skills/dlazy-image-amazon-product-image-suite)
- [dLazy website](https://dlazy.com)
- [dLazy CLI package on npm](https://www.npmjs.com/package/@dlazy/cli)
- [CLI project link listed in skill metadata](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Images, Text, Markdown]

**Output Format:** [Generated product image assets or hosted image URLs, with a Markdown checklist and delivery status.]

**Output Parameters:** [Variable image count and aspect ratios, selected for the requested Amazon listing scope.]

**Other Properties Related to Output:** [The documented workflow generates the main image first, then secondary images and A+ modules as requested.]

## Skill Version(s):

1.3.41 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
