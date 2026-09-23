## Description:

Generates 4MP high-resolution raster images with Recraft V4 Pro for print-ready assets and large-scale use.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to ask an agent to invoke the dLazy CLI for Recraft V4 Pro image generation, including synchronous generation, async task polling, and optional local saving of generated PNG assets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a third-party dLazy CLI and hosted API for generation.

Mitigation: Review the dLazy CLI/package before installation and only use the service under terms acceptable for the intended workload.

Risk: Prompts and any referenced local media files may be sent to api.dlazy.com or files.dlazy.com.

Mitigation: Only provide prompts and files that are approved for upload to dLazy-hosted services.

Risk: Authentication stores a dLazy API key locally or accepts one through DLAZY_API_KEY.

Mitigation: Protect the local configuration and rotate or revoke the key from the dLazy dashboard when access changes.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-recraft-v4-pro)
- [dLazy CLI Homepage](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm Package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy Website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, JSON, Files]

**Output Format:** [Markdown guidance with shell commands and JSON command output; generated image assets may be returned as hosted URLs or saved files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires npm or npx, a dLazy API key, network access to api.dlazy.com and files.dlazy.com, and may upload prompts or referenced local media files to dLazy.]

## Skill Version(s):

1.3.19 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
