## Description:

Converts text into high-quality, expressive speech using Kling TTS through the dLazy CLI and hosted API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to have an agent invoke the dLazy CLI for Kling text-to-speech generation, including authentication setup and voice, speed, format, and async options.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: User-provided text is sent to dLazy's hosted API for speech generation.

Mitigation: Avoid sending sensitive text unless dLazy processing is acceptable for the intended use case.

Risk: `dlazy login` stores an API key in the user's local CLI configuration.

Mitigation: Use organization key rotation or revocation when needed, and remove local credentials when the skill is no longer in use.

Risk: A global CLI install persists the pinned dLazy package on the system.

Mitigation: Use the documented `npx @dlazy/cli@1.2.3` alternative when a non-persistent invocation is preferred.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-keling-tts)
- [dLazy CLI Source](https://github.com/dlazyai/cli)
- [dLazy CLI npm Package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy Homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline bash commands and JSON result examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Invokes a cloud TTS API through the pinned @dlazy/cli package and may return hosted result URLs or async task status.]

## Skill Version(s):

1.3.7 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
