## Description:

MiniMax Hailuo omni-modal video model with native stereo audio, producing 5-15 second clips at up to 2K, with support for text-to-video, first/last frame transitions, and multi-asset references for character and scene consistency.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, creators, and agent users use this skill to generate short MiniMax H3 videos from text prompts, paired frames, or media references through the dLazy CLI and hosted API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected image, video, or audio files may be sent to the third-party dLazy cloud API for generation.

Mitigation: Use only content that is approved for third-party processing, and avoid sending sensitive or unauthorized media.

Risk: Authentication can store a dLazy API key in a local user configuration file.

Mitigation: Protect the local config file, prefer per-invocation environment variables when appropriate, and rotate or revoke keys when access changes.

Risk: The skill depends on a third-party CLI and hosted API outside NVIDIA control.

Mitigation: Use the pinned CLI version or on-demand npx invocation, and review the third-party CLI/package before deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-minimax-h3)
- [dLazy CLI project](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [JSON, Files, Shell commands, Configuration]

**Output Format:** [JSON result envelope with generated media URLs; optional local media file when saving is requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Async runs may return a generation ID for later polling.]

## Skill Version(s):

1.2.8 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
