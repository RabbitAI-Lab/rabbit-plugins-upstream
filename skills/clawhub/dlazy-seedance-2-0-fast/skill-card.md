## Description:

Helps an agent generate short videos through dLazy's Seedance 2.0 Fast service from text prompts, reference media, or first and last frames.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to request short AI-generated videos from prompts and optional image, video, audio, or frame references.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and referenced local media are sent to a third-party service, and the CLI handles a dLazy API key.

Mitigation: Use only content and credentials you trust dLazy to handle; review the CLI before installation and rotate or revoke the API key if needed.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-seedance-2-0-fast)
- [dLazy CLI repository listed in skill metadata](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown guidance with CLI commands; the CLI returns JSON containing generated media URLs or an asynchronous task ID.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports optional local download of the generated media.]

## Skill Version(s):

1.3.23 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
