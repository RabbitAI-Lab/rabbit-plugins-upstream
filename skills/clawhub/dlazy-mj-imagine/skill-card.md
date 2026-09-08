## Description:

Generates Midjourney-style images through the dLazy CLI with aspect ratio, bot type, and grid or U1-U4 output controls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to request stylized image generations through the dLazy hosted API, including aspect-ratio selection, Midjourney or Niji bot selection, upscale output selection, saving, and async polling.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing or running a third-party npm CLI can introduce supply-chain exposure.

Mitigation: Review the referenced dLazy CLI source or npm package before use, prefer the pinned @dlazy/cli@1.2.3 invocation, and avoid running npm as an administrator.

Risk: The skill requires a dLazy API key for hosted image generation.

Mitigation: Use a revocable dLazy API key, keep it in the CLI configuration or environment variable as documented, and rotate or revoke it from the dLazy dashboard when needed.

Risk: Prompts and referenced media files are sent to dLazy hosted endpoints for generation.

Mitigation: Only pass prompts and media files that are intended for upload to the hosted service.

## Reference(s):

- [dLazy CLI repository](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-mj-imagine)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON result examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The invoked CLI returns hosted image output URLs, or an async generateId when --no-wait is used.]

## Skill Version(s):

1.3.13 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
