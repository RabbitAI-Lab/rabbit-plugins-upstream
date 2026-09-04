## Description:

Generates 4MP high-resolution raster images suitable for print-ready assets and large-format use.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to request hosted Recraft V4 Pro image generation through the dLazy CLI, producing high-resolution raster image assets from prompts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and explicitly passed local files may be uploaded to dLazy for hosted image generation.

Mitigation: Avoid sending sensitive prompts or files unless that use is acceptable for the user's organization and the dLazy service terms.

Risk: Generated results are hosted by dLazy and returned as file URLs.

Mitigation: Review generated URLs and downloaded assets before sharing or using them in production workflows.

Risk: Authentication stores a dLazy API key in local CLI configuration unless supplied per invocation.

Mitigation: Use per-invocation credentials when appropriate and rotate or revoke the key from the dLazy dashboard if access changes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-recraft-v4-pro)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON output examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated image results are returned as hosted file URLs, with optional local saving through the dLazy CLI.]

## Skill Version(s):

1.3.12 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
