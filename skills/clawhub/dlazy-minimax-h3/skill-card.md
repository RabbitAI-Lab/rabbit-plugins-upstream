## Description:

MiniMax Hailuo omni-modal video model with native stereo audio, producing 5-15 second clips at up to 2K, with support for text-to-video, first/last frame transitions, and multi-asset references for character and scene consistency.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, developers, and agents use this skill to generate short videos through the dLazy-hosted MiniMax H3 CLI from text prompts, frame references, or multi-asset image, video, and audio inputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: This skill uses a third-party npm CLI and hosted dLazy service.

Mitigation: Review the referenced CLI package and source before installation, and use the pinned package version declared by the skill.

Risk: Prompts and local media paths supplied to image, video, or audio fields may be uploaded to dLazy services.

Mitigation: Avoid sending sensitive prompts or media unless the user accepts dLazy service handling for that content.

Risk: Login can store a dLazy API key in the local CLI configuration.

Mitigation: Use DLAZY_API_KEY for single-run authentication when persistence is not desired, and rotate or revoke keys from the dLazy dashboard when needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-minimax-h3)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [Markdown guidance with CLI commands and JSON response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The CLI can return generated asset URLs, async task IDs, and optionally save output assets to a local path.]

## Skill Version(s):

1.2.17 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
