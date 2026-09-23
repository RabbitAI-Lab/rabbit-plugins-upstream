## Description:

Image Replicate analyzes a source image's visuals, composition, colors, lighting, and style, builds a replication prompt, and hands it off to Seedream 4.5 to generate a new image in the same style.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, creators, and agent users use this skill to invoke the dLazy image-replicate CLI for reference-image style replication and image generation through the dLazy hosted service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, parameters, and referenced local media may be sent to dLazy API and storage endpoints.

Mitigation: Use only data approved for dLazy cloud processing and avoid sensitive images or prompts unless that transfer is authorized.

Risk: Authentication can store a dLazy API key in the local CLI configuration.

Mitigation: Use the DLAZY_API_KEY environment variable for per-invocation authentication when persistent local key storage is not acceptable, and rotate or revoke keys from the dLazy dashboard when needed.

Risk: The skill installs or invokes a pinned third-party npm CLI package.

Mitigation: Review the pinned @dlazy/cli package and linked source before use in environments with strict supply-chain controls.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-image-replicate)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [shell commands, configuration, JSON, guidance]

**Output Format:** [Markdown guidance with bash commands and JSON output examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return image output URLs hosted by files.dlazy.com or an async task identifier when --no-wait is used.]

## Skill Version(s):

1.3.20 (source: server release metadata; artifact frontmatter reports 1.3.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
