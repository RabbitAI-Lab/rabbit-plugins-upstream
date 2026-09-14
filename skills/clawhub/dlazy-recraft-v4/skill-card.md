## Description:

1MP raster image generation with refined design judgment for everyday creative work and fast iteration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, designers, and creative agents use this skill to call dLazy's hosted Recraft V4 image-generation CLI and produce 1MP raster images from prompts with selectable aspect ratios.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The dLazy CLI receives prompts, explicit media inputs, and request parameters sent for hosted image generation.

Mitigation: Avoid sending sensitive prompts or media unless the deployment is approved for dLazy's hosted service and data handling requirements.

Risk: Authentication can store a dLazy API key in the local CLI configuration.

Mitigation: Use per-invocation DLAZY_API_KEY where persistent local storage is not acceptable, and rotate or revoke organization keys when needed.

Risk: Installing the global npm package creates normal supply-chain trust in the pinned dLazy CLI package.

Mitigation: Use the documented npx @dlazy/cli@1.2.3 path for on-demand execution and review the linked source or package before use in restricted environments.

## Reference(s):

- [dLazy CLI Source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm Package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy CLI Homepage](https://github.com/dlazy-ai/cli)
- [dLazy Website](https://dlazy.com)
- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-recraft-v4)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Files, JSON, Guidance]

**Output Format:** [JSON result containing image output URLs, with optional saved PNG files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports asynchronous generation IDs, polling, timeout control, dry-run estimates, and local save paths.]

## Skill Version(s):

1.3.16 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
