## Description:

MiniMax Hailuo omni-modal video model with native stereo audio, producing 5-15 second clips at up to 2K, with text-to-video, first/last frame transitions, and multi-asset references for character and scene consistency.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to generate short videos through the dLazy hosted MiniMax H3 service from prompts, frame inputs, or multiple image, video, and audio references. It is suited for text-to-video and reference-guided video generation workflows that need command-line invocation from an agent.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected local media paths are sent to the dLazy hosted API for generation.

Mitigation: Only provide prompts and files intended for upload to the dLazy service.

Risk: Generated outputs are hosted by dLazy and returned as remote URLs.

Mitigation: Review generated content and storage expectations before sharing URLs or using outputs in sensitive workflows.

Risk: Authentication can store a dLazy API key in ~/.dlazy/config.json.

Mitigation: Use per-invocation DLAZY_API_KEY or npx when avoiding persistent local configuration, and rotate or revoke keys from the dLazy dashboard when needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-minimax-h3)
- [dLazy homepage](https://dlazy.com)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands; command execution returns JSON containing generated media URLs or async task status.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated outputs are hosted by dLazy, and the --save option can download the returned asset to a local path.]

## Skill Version(s):

1.2.9 (source: server release metadata; artifact frontmatter reports 1.2.3 for the pinned dLazy CLI install spec)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
