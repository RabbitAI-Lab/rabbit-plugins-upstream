## Description:

Generate images from text prompts or reference images using Doubao Seedream 5.0 Lite through dLazy.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to generate images from text or transform reference images with the hosted Seedream 5.0 Lite service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and provided local images may be sent to dLazy's hosted service.

Mitigation: Review prompts and files for sensitive content before submitting them.

Risk: Logging in can save an API key on the local machine.

Mitigation: Use a per-invocation environment variable if local key storage is not desired.

## Reference(s):

- [dLazy CLI project (release metadata link)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)
- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-seedream-5-0-lite)

## Skill Output:

**Output Type(s):** [Images, JSON]

**Output Format:** [JSON with generated image URLs; optional downloaded image file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports asynchronous generation and optional local saving.]

## Skill Version(s):

1.3.31 (source: server-resolved ClawHub release; artifact frontmatter says 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
