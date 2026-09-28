## Description:

Analyzes a reference image's composition, color, lighting, and style to generate a new image in a similar style with Seedream 4.5.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to generate images based on the visual style of a reference image through dLazy's hosted service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and user-supplied media may be sent to dLazy's hosted service.

Mitigation: Confirm the content is suitable for upload before providing it to the skill.

Risk: The CLI can store a dLazy API key locally.

Mitigation: Protect local credentials and rotate or revoke the key from the dLazy dashboard if needed.

Risk: A globally installed CLI remains on the system after use.

Mitigation: Use the pinned npx invocation if a persistent global binary is not desired.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-image-replicate)
- [dLazy CLI repository (listed in release metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Image URLs, JSON metadata]

**Output Format:** [JSON response with an image URL and MIME type; optional downloaded image file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Asynchronous requests may return a task ID before the image is ready.]

## Skill Version(s):

1.3.23 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
