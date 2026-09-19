## Description:

MiniMax Hailuo omni-modal video model with native stereo audio, producing 5-15 second clips at up to 2K, with support for text-to-video, first/last-frame transitions, and multi-asset references for character and scene consistency.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to invoke dLazy's MiniMax H3 video-generation CLI for text prompts, frame transitions, and image/video/audio reference-based generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends prompts and user-selected media files to dLazy-hosted services for generation.

Mitigation: Use it only with content approved for dLazy processing, and avoid submitting sensitive prompts or media unless the user accepts that service flow.

Risk: Authentication uses a dLazy API key that may be saved in the local CLI configuration.

Mitigation: Use OS account protections for the config file, prefer per-invocation environment keys when appropriate, and rotate or revoke the key from the dLazy dashboard if exposure is suspected.

Risk: A global npm install persists a third-party CLI binary on the system.

Mitigation: Use the pinned npx command for on-demand execution when a persistent global binary is not desired.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-minimax-h3)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON result examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The CLI can return completed output URLs or an asynchronous generateId for later polling.]

## Skill Version(s):

1.2.14 (source: server release metadata; artifact frontmatter and install spec reference dLazy CLI 1.2.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
