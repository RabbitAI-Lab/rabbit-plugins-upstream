## Description:

Generates images with Kling o1 from text prompts or reference images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

People and agents creating or editing images can use text prompts and optional reference images to request Kling o1 image generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and reference images are sent to dLazy for cloud generation; local reference files are uploaded to its media storage.

Mitigation: Only submit prompts and images you are comfortable sending to dLazy.

Risk: Login stores an API key in the local CLI configuration.

Mitigation: Protect the local account and revoke or rotate the key from the dLazy dashboard if needed.

Risk: The skill depends on an external CLI package.

Mitigation: Review the pinned CLI package before installing it.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/dlazyai/skills/dlazy-kling-image-o1)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Image files, Image URLs]

**Output Format:** [Generated image assets, returned with image URLs in a JSON response]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Text-to-image or image-to-image; reference images, aspect ratio, and 2K clarity can be specified.]

## Skill Version(s):

1.3.35 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
