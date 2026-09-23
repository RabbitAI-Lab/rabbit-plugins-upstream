## Description:

Uploads a clean voice sample through the dLazy CLI to create an ElevenLabs Instant Voice Cloning voice for use with ElevenLabs text-to-speech.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to invoke dLazy's ElevenLabs voice-cloning command with an audio sample, voice name, and optional description to create a reusable custom TTS voice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Voice samples are sensitive biometric data and may be uploaded to dLazy services.

Mitigation: Use the skill only with clear authorization from the voice owner and treat uploaded audio as sensitive data.

Risk: The dLazy API key may be stored locally or passed through the environment.

Mitigation: Review the dLazy CLI/source before installing, store keys only in approved environments, and rotate or revoke keys when needed.

Risk: The supplied documentation contains stale image and prompt examples that may confuse users.

Mitigation: Confirm current command flags with `dlazy elevenlabs-voice-clone -h` and prefer the documented voice-cloning parameters.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-voice-clone)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [shell commands, JSON, guidance]

**Output Format:** [JSON responses and Markdown guidance with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return hosted output URLs or an asynchronous task identifier for later polling.]

## Skill Version(s):

1.3.17 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
