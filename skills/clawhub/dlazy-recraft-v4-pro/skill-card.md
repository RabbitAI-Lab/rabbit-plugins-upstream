## Description:

Generates 4MP raster images from prompts for print-ready and large-format assets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and designers use this skill to generate high-resolution raster images for print-ready and large-format projects through the dLazy service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and explicitly supplied media may be sent to the external dLazy cloud service.

Mitigation: Avoid submitting sensitive prompts or media unless approved for external processing.

Risk: Authentication can store a dLazy API key on the local machine.

Mitigation: Protect the local key and rotate or revoke it in the dLazy dashboard when needed.

Risk: Installing the external CLI globally leaves a persistent tool on the machine.

Mitigation: Use the pinned npx invocation if a global installation is unnecessary.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-recraft-v4-pro)
- [dLazy CLI repository (linked in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [JSON responses, Image URLs, Image files]

**Output Format:** [JSON result containing an image URL; optional downloaded image file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports aspect-ratio selection and asynchronous generation.]

## Skill Version(s):

1.3.25 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
