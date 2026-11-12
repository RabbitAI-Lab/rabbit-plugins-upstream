## Description:

Generates images from text prompts using Jimeng through dLazy.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers provide a text prompt, optionally with reference images, to generate Jimeng images and retrieve or save the resulting image assets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review is partial with medium confidence and flags a dlazy login step whose link to the image-generation task is not demonstrated, along with unresolved references.

Mitigation: Review the referenced CLI package and unresolved runtime details before installing, and confirm that the login flow is expected before using it.

Risk: Prompts and supplied reference media are sent to dLazy's hosted service; local media files are uploaded for processing.

Mitigation: Avoid sending sensitive prompts or media unless their use with the service is approved.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/dlazyai/skills/dlazy-jimeng-t2i)
- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Images, JSON]

**Output Format:** [JSON result with generated image URLs and metadata; optionally saved image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return an asynchronous task ID when --no-wait is used; --save can write the generated image to a local file.]

## Skill Version(s):

1.3.39 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
