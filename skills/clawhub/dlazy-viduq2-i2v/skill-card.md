## Description:

Turns still images into dynamic videos with the Vidu Q2 image-to-video model.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to turn supplied images and prompts into generated videos through the dLazy-hosted Vidu Q2 service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, parameters, and selected media files are sent to dLazy's hosted service.

Mitigation: Only provide media and information you are comfortable uploading to dLazy.

Risk: Installing the CLI adds a third-party package, and use requires a dLazy API key.

Mitigation: Review the pinned package before installing, use npx to avoid a persistent global install, and rotate or revoke the API key when no longer needed.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-viduq2-i2v)
- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with shell commands and JSON response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands can return a generated media URL or an asynchronous task ID; an optional flag saves the result locally.]

## Skill Version(s):

1.3.27 (source: ClawHub release metadata; skill files list 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
