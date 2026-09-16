## Description:

ElevenLabs Instant Voice Cloning (IVC) uploads a clean voice sample to clone a custom voice usable with ElevenLabs TTS.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to invoke dLazy's ElevenLabs voice-cloning workflow from an agent, supplying an audio sample, voice name, and optional description to create a reusable cloned voice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Voice cloning can involve consent, privacy, and impersonation risks.

Mitigation: Only upload voice samples you own or have explicit permission to use, and do not use cloned voices for impersonation or deceptive content.

Risk: Audio inputs and generated results are sent to dLazy-hosted services.

Mitigation: Avoid submitting sensitive audio and review dLazy service terms before use.

Risk: The scanner reports misleading command and output examples in the artifact.

Mitigation: Review the command help with `dlazy elevenlabs-voice-clone -h` and validate expected outputs before relying on examples.

Risk: Global CLI installation and persisted API keys can broaden local exposure.

Mitigation: Prefer `npx` or a least-privilege environment, protect stored API keys, and verify the npm package and source before running.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-voice-clone)
- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, JSON]

**Output Format:** [Markdown guidance with shell commands and JSON API result examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return hosted result URLs or an asynchronous task identifier when invoked with no-wait behavior.]

## Skill Version(s):

1.3.15 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
