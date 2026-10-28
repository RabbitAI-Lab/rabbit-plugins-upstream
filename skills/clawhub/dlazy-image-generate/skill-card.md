## Description:

Automatically selects a suitable dLazy CLI image model based on the prompt.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate or edit images, upscale or vectorize visual assets, and pass generated image URLs between dLazy model commands.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and any supplied reference media are sent to dLazy for processing, and generated media is hosted there.

Mitigation: Only submit prompts and media you are comfortable uploading to the service.

Risk: Image generation may incur service charges.

Mitigation: Consider the expected generation cost and available credits before starting a workflow.

Risk: The CLI saves the dLazy API key in the local user configuration unless another supported method is used.

Mitigation: Keep the configuration and API key private, and rotate or revoke the key if it is exposed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-image-generate)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Image files, Image URLs, SVG files, JSON]

**Output Format:** [Hosted image or SVG URLs in a JSON response envelope]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated assets may be raster images or vector graphics; input media can be supplied as references.]

## Skill Version(s):

1.3.36 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
