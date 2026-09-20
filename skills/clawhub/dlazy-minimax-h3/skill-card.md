## Description:

MiniMax Hailuo omni-modal video model with native stereo audio, producing 5-15 second clips at up to 2K, with support for text-to-video, first/last frame transitions, and multi-asset references for character and scene consistency.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to invoke the dLazy MiniMax H3 video-generation CLI for text-to-video, frame-transition, and multi-asset reference workflows. It returns generation status and hosted media outputs, with an optional local save path for the generated asset.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and media paths may be uploaded to dLazy services for cloud generation.

Mitigation: Avoid sending sensitive prompts or media unless the user has approved that data sharing and the service terms are acceptable.

Risk: The dLazy login flow may store an API key in local CLI configuration.

Mitigation: Use DLAZY_API_KEY for per-invocation credentials when tighter control is needed, and rotate or revoke keys from the dLazy dashboard.

Risk: The skill installs or runs a pinned third-party CLI package.

Mitigation: Confirm trust in the pinned dLazy CLI package and service before installation or execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-minimax-h3)
- [dLazy homepage](https://dlazy.com)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files]

**Output Format:** [JSON response with generated media URLs; optional downloaded media file when a save path is provided]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports asynchronous task IDs when no-wait mode is used.]

## Skill Version(s):

1.2.15 (source: server release evidence; artifact frontmatter shows 1.2.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
