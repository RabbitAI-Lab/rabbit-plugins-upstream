## Description:

Analyzes a reference image's composition, color, lighting, and style to generate a similar image with Seedream 4.5.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to generate images matching the visual style of reference images through dLazy's hosted image service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected local media may be sent to dLazy's cloud service.

Mitigation: Review prompts and media for sensitive information before submitting them.

Risk: Authentication stores a dLazy API key on the user's device.

Mitigation: Protect local credentials and rotate or revoke the key through dLazy if needed.

Risk: Running the skill installs or executes a third-party npm CLI.

Mitigation: Review the CLI before use; use the pinned npx invocation to avoid a persistent global installation.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-image-replicate)
- [dLazy CLI homepage (declared in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, Image links]

**Output Format:** [Markdown with commands and generated image URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated images can be downloaded locally; asynchronous requests may return a task ID first.]

## Skill Version(s):

1.3.30 (source: server-resolved ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
