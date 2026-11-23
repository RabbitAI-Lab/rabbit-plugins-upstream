## Description:

Generates high-fidelity vector illustrations and design assets from text prompts using Recraft V4 Pro Vector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and designers can create detailed vector illustrations and visual assets from text prompts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Security guidance notes that the reviewed material includes CLI login and API-key setup steps that do not fully match the stated vector-generation purpose, and inspection coverage is partial.

Mitigation: Review the pinned CLI and its authentication flow before installing or using the skill.

Risk: Prompts and local files supplied for generation are sent to dLazy's hosted API and media storage.

Mitigation: Avoid submitting sensitive prompts or files unless their transfer to the service is acceptable.

## Reference(s):

- [dLazy CLI repository link](https://github.com/dlazy-ai/cli)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Image files, JSON]

**Output Format:** [JSON response with generated image metadata and a hosted image URL; optionally a locally saved image file.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Prompt-based generation with optional aspect ratio, asynchronous task ID, and local save path.]

## Skill Version(s):

1.3.42 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
