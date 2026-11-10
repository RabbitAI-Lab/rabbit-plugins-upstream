## Description:

Generates ElevenLabs eleven_v3 dialogue audio with up to ten voices, assigning a voice to each line and supporting expressive audio tags.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers can create multi-speaker dialogue audio for character scenes, podcasts, and short skits by assigning voices and optional delivery tags to dialogue lines.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Using the skill requires dLazy login or API-key setup, which scanners reported did not clearly match the dialogue-generation purpose.

Mitigation: Before installing or authorizing the CLI, confirm that the dLazy authentication flow is expected for the audio-generation task.

Risk: Security scan coverage was partial because several referenced local paths could not be resolved.

Mitigation: Review the relevant CLI authentication steps and service documentation before use; use an organization-scoped key that can be rotated or revoked.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-dialogue)
- [dLazy CLI homepage (skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Audio, Hosted audio URLs, Audio files]

**Output Format:** [Generated dialogue audio, returned as a hosted URL or saved audio file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Accepts up to 20 dialogue lines and 10 unique voices; asynchronous generation can return a task ID.]

## Skill Version(s):

1.3.38 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
