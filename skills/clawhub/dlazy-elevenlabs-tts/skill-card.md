## Description:

Generates ElevenLabs eleven_v3 speech from text with multilingual voice choices and controls for stability, similarity, and style.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use the skill to generate multilingual spoken audio for dubbing, audiobooks, and character dialogue.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The documented dLazy authentication steps may not match expectations for an ElevenLabs speech skill.

Mitigation: Confirm the intended provider and authentication flow before setting up credentials.

Risk: The partial scan did not establish how the CLI handles credentials.

Mitigation: Review the CLI's credential handling and confirm you trust the service before providing an API key.

Risk: Unusual whitespace was flagged in the Chinese guide.

Mitigation: Review the Chinese guide's formatting before relying on or redistributing it.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-tts)
- [dLazy CLI package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Audio, JSON]

**Output Format:** [Generated audio asset with a JSON result envelope]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Voice, language, stability, similarity, and style options; asynchronous generation is supported.]

## Skill Version(s):

1.3.40 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
