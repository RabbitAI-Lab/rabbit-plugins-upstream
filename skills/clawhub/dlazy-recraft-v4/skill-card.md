## Description:

Generates 1MP raster images from prompts using dLazy's hosted Recraft V4 service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to generate raster images for everyday creative work and rapid iteration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and any local media supplied to the command are sent to dLazy's cloud service, which also hosts generated assets.

Mitigation: Avoid submitting sensitive prompts or media without approval for cloud processing and hosting.

Risk: Authentication can store a dLazy API key in local CLI configuration.

Mitigation: Protect local credentials or use the per-invocation environment-variable option; rotate or revoke keys if exposed.

Risk: Using the external npm CLI introduces a third-party software dependency.

Mitigation: Review the linked package and source before installation when supply-chain assurance is required.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-recraft-v4)
- [dLazy CLI source linked in skill metadata](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Images, JSON]

**Output Format:** [JSON response with hosted image URLs; optional downloaded image file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Prompt and aspect ratio are configurable; asynchronous generation is supported.]

## Skill Version(s):

1.3.30 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
