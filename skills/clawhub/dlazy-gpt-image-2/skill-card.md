## Description:

Generates images from text prompts and edits or combines images using reference inputs through the dLazy service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to generate images from prompts or edit and combine images with reference inputs through the dLazy CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and reference images supplied to the CLI may be uploaded to the hosted dLazy service.

Mitigation: Avoid sending sensitive prompts or images unless their upload to dLazy is acceptable.

Risk: Login may persist a dLazy API key locally.

Mitigation: Use a per-run DLAZY_API_KEY if persistent storage is undesirable, and rotate or revoke keys when needed.

Risk: The skill relies on an external npm CLI.

Mitigation: Review the CLI source and package before installing or running it.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-gpt-image-2)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown guidance and CLI commands; the CLI returns JSON with generated image URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated images can be downloaded to a local path; asynchronous requests may return a generation ID.]

## Skill Version(s):

1.3.26 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
