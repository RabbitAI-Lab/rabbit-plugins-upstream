## Description:

Generates stylized images from text prompts with configurable aspect ratio, bot type, and grid or selected-image output.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to generate artistic, strongly stylized images from prompts, choosing an aspect ratio and grid or individual image output.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and any local media supplied to the skill are sent to dLazy's hosted service.

Mitigation: Review prompts and file paths before use; avoid sending sensitive material.

Risk: Login or key setup stores an API key locally, and global CLI installation persists on the device.

Mitigation: Use the on-demand npx option if a global CLI is unnecessary, and rotate or revoke the key from dLazy when needed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-mj-imagine)
- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Images, JSON]

**Output Format:** [JSON result with hosted image URL; optional downloaded image file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports aspect ratio, bot type, grid or U1–U4 selection, and asynchronous results.]

## Skill Version(s):

1.3.30 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
