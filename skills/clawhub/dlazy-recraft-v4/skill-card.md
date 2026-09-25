## Description:

1MP raster image generation with refined design judgment for everyday creative work and fast iteration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate 1MP raster images through the dLazy Recraft V4 CLI from text prompts and supported aspect-ratio options.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and any input files selected by the user can be uploaded to dLazy hosted services.

Mitigation: Avoid sending sensitive or restricted content unless the service is approved for that data.

Risk: Authentication can store a dLazy API key in the local user configuration.

Mitigation: Use per-invocation environment variables or npx when local persistence is not desired, and rotate or revoke keys if exposed.

Risk: Generated result URLs are hosted by dLazy media storage.

Mitigation: Treat generated URLs and downloaded assets according to the user's data retention and sharing policy.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-recraft-v4)
- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Images, JSON, Shell commands, Guidance]

**Output Format:** [JSON result containing hosted PNG image output metadata, with optional local image download when --save is used.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a dLazy API key; prompts and selected input files are sent to dLazy hosted endpoints.]

## Skill Version(s):

1.3.20 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
