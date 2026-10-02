## Description:

Helps agents generate short MiniMax H3 videos with stereo audio from text, first and last frames, or reference media through dLazy.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to request short videos from text prompts, frame transitions, or image, video, and audio references through the dLazy service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing and running a third-party CLI involves trusting its package and account service.

Mitigation: Review the dLazy CLI package and service before installing; use the on-demand npx option if a persistent global install is unnecessary.

Risk: Prompts and media explicitly provided for generation are sent to dLazy.

Mitigation: Avoid submitting confidential or unauthorized content; confirm that sharing the selected media with dLazy is acceptable.

Risk: CLI login or key setup stores a dLazy API key locally.

Mitigation: Protect local credentials and use a per-invocation API key when persistent storage is undesirable.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-minimax-h3)
- [dLazy CLI homepage (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, Text]

**Output Format:** [Markdown guidance with shell examples and JSON result summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include generated video URLs or an asynchronous task ID.]

## Skill Version(s):

1.2.21 (source: ClawHub release evidence; bundled skill frontmatter lists 1.2.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
