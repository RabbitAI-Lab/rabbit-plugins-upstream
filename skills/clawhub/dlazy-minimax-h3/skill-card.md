## Description:

MiniMax Hailuo omni-modal video model with native stereo audio, producing 5-15 second clips at up to 2K, with text-to-video, first/last frame transition, and multi-asset reference modes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate short MiniMax Hailuo video clips through the dLazy CLI, including text-to-video, frame transition, and referenced-media workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected image, video, or audio paths may be sent to dLazy cloud services for generation.

Mitigation: Avoid submitting sensitive prompts or media unless the user accepts dLazy service handling for that content.

Risk: `dlazy login` stores an API key in local CLI configuration.

Mitigation: Use `npx @dlazy/cli@1.2.3` or the `DLAZY_API_KEY` environment variable when less persistent local credential storage is preferred.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-minimax-h3)
- [Publisher profile](https://clawhub.ai/user/dlazyai)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON result examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return hosted output URLs or an asynchronous generation task ID; the CLI can save generated media to a local path.]

## Skill Version(s):

1.2.7 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
