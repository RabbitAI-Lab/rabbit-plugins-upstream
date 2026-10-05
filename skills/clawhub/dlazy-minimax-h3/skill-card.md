## Description:

Guides agents to generate short MiniMax H3 videos with audio from text, frame transitions, or reference media through the dLazy CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to request short videos from text prompts, first and last frames, or image, video, and audio references.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and supplied media are sent to dLazy-hosted services.

Mitigation: Avoid submitting sensitive content unless you accept dLazy's handling of it.

Risk: Authentication can save a dLazy API key in local CLI configuration.

Mitigation: Protect the local key and rotate or revoke it if exposed.

Risk: Using the external CLI introduces package supply-chain exposure.

Mitigation: Review the CLI package before installing and use the pinned npx option if a global install is unnecessary.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-minimax-h3)
- [dLazy CLI repository](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell commands and result links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated asset URLs or asynchronous task IDs may be returned by the CLI.]

## Skill Version(s):

1.2.22 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
