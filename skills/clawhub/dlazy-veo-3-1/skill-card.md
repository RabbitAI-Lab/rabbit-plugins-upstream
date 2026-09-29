## Description:

Guides an agent in generating cinematic videos from text or images using Google Veo 3.1 through dLazy's hosted service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to guide video generation from text prompts, reference images, or existing video through dLazy's hosted Veo 3.1 service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and supplied media may be sent to dLazy's hosted service, and generated files are hosted there.

Mitigation: Submit only media and prompts you are permitted to share with dLazy; review the service terms before use.

Risk: Logging in can persist an API key locally, and a global CLI installation persists on the device.

Mitigation: Use a per-invocation environment variable for the key and the pinned npx command if you prefer not to save a credential or install the CLI globally.

## Reference(s):

- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)
- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-veo-3-1)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The guided CLI invocation returns generated media URLs or an asynchronous task ID.]

## Skill Version(s):

1.3.21 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
