## Description:

Separates foregrounds from image backgrounds using the dLazy cloud service and returns a transparent-background image URL.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Designers, creators, and developers use this skill to remove image backgrounds for product photos, portraits, and composites.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected local images may be uploaded to dLazy, and generated results are hosted there.

Mitigation: Confirm the images are appropriate to share with the dLazy cloud service before submitting them.

Risk: Authentication may save an API key in local CLI configuration.

Mitigation: Protect the local configuration or use the per-invocation DLAZY_API_KEY environment variable.

Risk: The current example uses --prompt rather than the documented image input flag.

Mitigation: Use --image for image input and check dlazy imageseg -h before running the example.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-imageseg)
- [dLazy CLI repository (metadata link)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown guidance and JSON image-result URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Transparent-background image URL; optional local download.]

## Skill Version(s):

1.3.28 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
