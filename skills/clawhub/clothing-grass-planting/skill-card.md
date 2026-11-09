## Description:

Turns outfit photos into social-commerce lifestyle images by keeping the clothing as the focus while changing the model, pose, or scene.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Content creators and ecommerce teams use it to make lifestyle images for social posts from outfit photos, optionally following a separate model or scene reference.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Outfit and reference photos may be sent to external image services.

Mitigation: Use only photos you are authorized to share, and review the selected provider's data handling before sending them.

Risk: The security review reports incomplete inspection of some scripts and references.

Mitigation: Review the skill and its scripts before installation, including how the selected provider handles images.

Risk: Generated images could be presented as a real person's endorsement or experience.

Mitigation: Do not use outputs to imply real-person endorsement or actual product experience.

## Reference(s):

- [Provider CLI and data flow](references/provider-cli.md)
- [Image model parameters](references/model-flags.md)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Images, Shell commands, Guidance]

**Output Format:** [Generated lifestyle images (typically JPEG) with Markdown guidance and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Typically 1024×1536; accepts an outfit image and an optional model or scene reference.]

## Skill Version(s):

1.0.29 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
