## Description:

Generates ElevenLabs eleven_v3 speech from text with multilingual voice selection and controls for stability, similarity, and style.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use the skill to generate multilingual voiceovers, audiobook narration, and character dialogue from text, choosing a voice and adjusting speech style.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts are sent to dLazy for hosted processing.

Mitigation: Submit only content you are comfortable sharing with dLazy.

Risk: Speech generation uses account credits.

Mitigation: Run --dry-run to check the estimated cost before generating audio.

Risk: The CLI stores the API key in local user configuration.

Mitigation: Protect access to the saved key and rotate or revoke it if exposed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-tts)
- [dLazy CLI project page (skill metadata homepage)](https://github.com/dlazy-ai/cli)
- [dLazy CLI package on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Audio, Audio asset URLs]

**Output Format:** [JSON result containing generated audio asset URLs; optionally a saved audio file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Asynchronous mode can return a task ID before the audio asset is ready.]

## Skill Version(s):

1.3.35 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
