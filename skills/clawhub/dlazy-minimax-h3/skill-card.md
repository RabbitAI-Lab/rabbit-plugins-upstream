## Description:

Generates short videos with MiniMax Hailuo from text prompts, frame transitions, or reference media through dLazy.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to request short AI-generated videos from text prompts, frame transitions, or reference images, video, and audio.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and supplied media are sent to dLazy for generation.

Mitigation: Only submit prompts and media you are comfortable uploading; review the service terms.

Risk: Authentication saves an API key in local CLI configuration.

Mitigation: Protect the local account and rotate or revoke the key if needed.

Risk: Installing the CLI runs third-party software.

Mitigation: Review the CLI source before installation; use the pinned on-demand npx command to avoid a persistent global install.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-minimax-h3)
- [dLazy CLI repository (listed in skill metadata; not verified skill provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, JSON]

**Output Format:** [Markdown instructions and JSON CLI responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses include generated media URLs or an asynchronous task ID; files can be saved locally.]

## Skill Version(s):

1.2.25 (source: ClawHub release; skill frontmatter and pinned CLI specify 1.2.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
