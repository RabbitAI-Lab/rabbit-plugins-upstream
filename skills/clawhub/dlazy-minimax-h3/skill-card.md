## Description:

Generates short MiniMax H3 videos from text prompts, frame transitions, or image, video, and audio references through the dLazy service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to request short videos from prompts, first and last frames, or reference media using a dLazy account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and supplied media are sent to dLazy for cloud processing.

Mitigation: Only submit prompts and files you are comfortable sharing with dLazy; review its service terms before use.

Risk: The CLI stores an API key locally and requires installing third-party software.

Mitigation: Review the CLI source before installation, use the pinned on-demand npx command if preferred, protect the key, and rotate or revoke it if needed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-minimax-h3)
- [dLazy CLI source (skill metadata link; import provenance unavailable)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON results, Video links, Configuration guidance]

**Output Format:** [CLI commands and JSON responses with generated-media URLs or an asynchronous task ID]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Optional local download of the generated video.]

## Skill Version(s):

1.2.27 (source: ClawHub release evidence; skill files list 1.2.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
