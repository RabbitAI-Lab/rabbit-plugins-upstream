## Description:

Guides agents in generating ElevenLabs eleven_v3 speech with curated multilingual voices and adjustable voice controls through dLazy.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to prepare voiceovers, audiobooks, and character dialogue with a choice of voices and speech-style controls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Speech prompts and voice settings are sent to the dLazy hosted service.

Mitigation: Confirm that sharing the intended content with dLazy is acceptable before invoking the service.

Risk: Authentication requires a dLazy API key that may be stored locally.

Mitigation: Protect the key, avoid exposing it in shared commands or logs, and rotate it if compromised.

Risk: The documented TTS response example incorrectly depicts image output.

Mitigation: Check the actual returned media type and URL before using or sharing generated output.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-tts)
- [dLazy CLI repository](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance covers voice selection, synthesis settings, and retrieving generated speech or an asynchronous task result.]

## Skill Version(s):

1.3.29 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
