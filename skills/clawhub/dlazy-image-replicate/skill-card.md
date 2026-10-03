## Description:

Analyzes a reference image's composition, colors, lighting, and style to generate a new image in a similar style using Seedream 4.5.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to generate a new image inspired by the visual style of a supplied reference image through dLazy's hosted service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected local media are sent to dLazy's cloud service, and generated images are hosted by dLazy.

Mitigation: Only submit media and prompts you are comfortable sharing with dLazy.

Risk: Authentication can store an API key locally.

Mitigation: Protect local credentials and rotate or revoke the key through the dLazy dashboard if needed.

Risk: A global CLI installation persists on the device.

Mitigation: Use the documented pinned npx command if a persistent global installation is not desired.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-image-replicate)
- [dLazy CLI (declared in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Images, JSON]

**Output Format:** [JSON containing a generated image URL; optional downloaded image file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Asynchronous requests may initially return a task ID instead of an image URL.]

## Skill Version(s):

1.3.25 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
