## Description:

1MP raster image generation with refined design judgment for everyday creative work and fast iteration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, designers, and developers use this skill to generate 1MP raster images through the dLazy Recraft V4 CLI workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and media files explicitly passed to the CLI may be sent to dLazy's cloud service.

Mitigation: Avoid passing sensitive private content unless the user intends to upload it to dLazy.

Risk: Authentication can persist an API key in the local dLazy configuration file.

Mitigation: Use the per-invocation DLAZY_API_KEY environment variable when persistent local credentials are not desired.

Risk: A global CLI install persists the dLazy CLI on the system.

Mitigation: Use the pinned npx invocation when a non-global install path is preferred.

## Reference(s):

- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-recraft-v4)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Files, Guidance]

**Output Format:** [JSON responses with generated image URLs and optional downloaded image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports asynchronous task IDs, local save paths, aspect ratio selection, and dry-run cost estimates.]

## Skill Version(s):

1.3.12 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
