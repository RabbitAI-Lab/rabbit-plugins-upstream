## Description:

Professional tier of Seedream 5.0 for generating commercial-grade key visuals and brand assets with stronger detail, typography, and complex composition handling.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to invoke dLazy's hosted Seedream 5.0 Pro image generation workflow from an agent, using prompts and optional reference images to produce generated image assets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected local image files are sent to dLazy cloud services for inference and media handling.

Mitigation: Use the skill only with content suitable for dLazy's hosted service and avoid submitting sensitive files unless the user accepts that transfer.

Risk: Authentication can save a dLazy API key in the local CLI configuration.

Mitigation: Prefer DLAZY_API_KEY for temporary use when a persistent key is not desired, and rotate or revoke the key from the dLazy dashboard when needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-seedream-5-0-pro)
- [dLazy CLI repository](https://github.com/dlazyai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, API Calls, Files]

**Output Format:** [JSON responses with generated image URLs and optional saved image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports synchronous waiting, asynchronous task IDs, dry-run cost estimates, reference images, fixed 2k resolution, and common aspect ratios.]

## Skill Version(s):

1.2.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
