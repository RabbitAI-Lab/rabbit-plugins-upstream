## Description:

Image super-resolution tool that enhances image clarity and detail and returns an enhanced image URL for restoring or upscaling low-resolution assets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to run dLazy image super-resolution from an agent workflow, sending an image URL or local image path to the dLazy CLI and receiving an enhanced image URL or saved output file.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Input images or local media paths may be uploaded to dLazy's hosted service and outputs may be hosted by dLazy.

Mitigation: Avoid sending sensitive media unless the user accepts the service exposure; review dLazy terms before commercial use.

Risk: Authentication can save a dLazy API key in the local CLI configuration.

Mitigation: Use DLAZY_API_KEY for per-invocation credentials when persistence is not desired, and rotate or revoke keys from the dLazy dashboard when needed.

Risk: The skill depends on a third-party npm CLI and paid cloud service.

Mitigation: Use the pinned npx invocation or review the dLazy CLI source before installing globally.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-superres)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON CLI responses containing generated image URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The CLI can return hosted output URLs, asynchronous task IDs, or save enhanced image files when --save is used.]

## Skill Version(s):

1.3.20 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
