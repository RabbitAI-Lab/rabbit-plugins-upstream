## Description:

Analyzes a reference image's composition, colors, lighting, and style to generate a new image in a similar style using Seedream 4.5.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to generate an image that follows the visual style of a reference image through the dLazy service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and provided media may be sent to dLazy, and generated images are hosted by dLazy.

Mitigation: Only provide content approved for the external service and review outputs before sharing them.

Risk: The CLI may save an API key locally.

Mitigation: Protect local credentials and rotate or revoke the key from the dLazy dashboard if needed.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-image-replicate)
- [dLazy CLI homepage (skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package (skill metadata)](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Image, JSON, Shell commands]

**Output Format:** [JSON containing a generated image URL, with optional local image download]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Asynchronous requests may return a task ID for later polling.]

## Skill Version(s):

1.3.27 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
