## Description:

Uses the dLazy image-generation service to create or edit images from prompts and optional reference images, with controls for aspect ratio and quality.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to generate or edit detailed images with prompts, reference images, and selectable aspect ratios and quality levels.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected reference images are sent to dLazy services, and generated files may be hosted there.

Mitigation: Avoid submitting sensitive prompts or images; review the service terms before use.

Risk: Signing in stores a dLazy API key in the local user configuration.

Mitigation: Protect access to the user configuration and rotate or revoke the key if exposed.

## Reference(s):

- [dLazy CLI source repository](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Image links, JSON results]

**Output Format:** [JSON containing generated image URLs; optionally a saved image file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Asynchronous requests can initially return a task ID instead of an image.]

## Skill Version(s):

1.2.13 (source: ClawHub release; embedded skill frontmatter lists 1.2.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
