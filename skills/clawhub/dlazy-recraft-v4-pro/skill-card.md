## Description:

Generates 4MP high-resolution raster images for print-ready assets and large-format use.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to invoke the dLazy Recraft V4 Pro image-generation CLI for high-resolution raster image creation. It supports prompt-based generation, optional asynchronous execution, and saving generated assets locally.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill relies on an external npm CLI and dLazy cloud API.

Mitigation: Review the linked dLazy CLI source before installation and prefer the pinned npx invocation when avoiding a persistent global binary.

Risk: Prompts and files passed to generation fields may be sent to dLazy cloud services.

Mitigation: Avoid sending sensitive content unless approved for the service, and treat generated URLs as externally hosted outputs.

Risk: API credentials can be persisted in the local dLazy CLI config.

Mitigation: Use a revocable dLazy API key, rotate or revoke keys when needed, or provide DLAZY_API_KEY per invocation to reduce local credential persistence.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-recraft-v4-pro)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Configuration instructions]

**Output Format:** [JSON result containing generated image URLs, with optional saved PNG assets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires npm or npx and a dLazy API key; supports asynchronous task IDs and local asset saving through the CLI.]

## Skill Version(s):

1.3.13 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
