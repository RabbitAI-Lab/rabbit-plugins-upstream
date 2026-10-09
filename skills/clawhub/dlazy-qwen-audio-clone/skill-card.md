## Description:

Helps users clone a custom voice from a clean voice sample for later text-to-speech use through dLazy's Qwen audio-cloning service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to submit an authorized voice sample and create a reusable custom voice for text-to-speech.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Voice cloning without the speaker's permission can misuse their identity.

Mitigation: Use only voice samples you have permission to clone.

Risk: Voice samples are uploaded to a hosted service, and a saved API key persists locally.

Mitigation: Confirm the sample can be shared with dLazy and consider a per-invocation key or npx if you do not want persistent credentials or a global install.

Risk: Copied examples and output details in the skill documentation may not match the voice-cloning command.

Mitigation: Review the CLI package before installing and check `dlazy qwen-audio-clone -h` for current options.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-qwen-audio-clone)
- [dLazy CLI source listed in skill metadata](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, Text]

**Output Format:** [Markdown guidance and CLI commands; service responses in JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The service creates a reusable custom voice from a submitted sample; actual response fields should be checked with CLI help.]

## Skill Version(s):

1.3.25 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
