## Description:

ElevenLabs Instant Voice Cloning (IVC) uploads a clean voice sample to create a custom voice for use with ElevenLabs text-to-speech.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and content-production agents use this skill to call the dLazy CLI for ElevenLabs voice cloning, providing an audio sample, voice name, and optional description to create a reusable custom voice. It is intended for voices the user owns or is explicitly authorized to clone.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uploads sensitive voice samples to dLazy and ElevenLabs-backed hosted services.

Mitigation: Use only audio from voices the user owns or is explicitly authorized to clone, and avoid uploading private or regulated recordings without appropriate approval.

Risk: The dLazy API key is stored locally or supplied through an environment variable.

Mitigation: Store keys only in the documented user config or environment, keep filesystem permissions restricted to the OS user, and rotate or revoke keys from the dLazy dashboard if exposure is suspected.

Risk: The skill documentation contains mismatched image and prompt examples for a voice-cloning workflow.

Mitigation: Verify the live `dlazy elevenlabs-voice-clone -h` output and prefer the documented voice-clone flags, especially `--audio_url`, before executing commands.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-voice-clone)
- [dLazy CLI homepage](https://github.com/dlazyai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy API key dashboard](https://dlazy.com/dashboard/organization/api-key)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON command results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return an asynchronous task identifier when invoked with --no-wait.]

## Skill Version(s):

1.3.7 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
