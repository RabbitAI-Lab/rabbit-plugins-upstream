## Description:

ElevenLabs Instant Voice Cloning (IVC) uploads a clean voice sample to clone a custom voice usable with ElevenLabs TTS.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creators use this skill to invoke dLazy's ElevenLabs voice-cloning workflow from an agent, supplying a voice sample, name, and optional description to create a reusable custom TTS voice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive voice samples and API credentials are processed by dLazy infrastructure through a third-party CLI.

Mitigation: Install only after reviewing and trusting the dLazy CLI and service; prefer on-demand npx or an isolated environment, and rotate or revoke any exposed API key.

Risk: Voice cloning can create consent and biometric-privacy risk when samples are not owned by the user or lack explicit informed consent.

Mitigation: Use the skill only for voices the user owns or has explicit informed consent to clone, and review applicable policy requirements before uploading audio or using generated voices.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-voice-clone)
- [dLazy homepage](https://dlazy.com)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance, JSON, files]

**Output Format:** [Markdown guidance with shell commands and JSON response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires npm or npx, a dLazy API key, and an audio URL or local audio path.]

## Skill Version(s):

1.3.13 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
