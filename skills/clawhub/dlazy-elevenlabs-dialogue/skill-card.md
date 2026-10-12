## Description:

Helps agents generate multi-voice ElevenLabs eleven_v3 dialogue through dLazy, assigning voices to individual lines and supporting expressive audio tags.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to produce multi-character dialogue audio for podcasts, skits, and character scenes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Dialogue text, parameters, and provided media paths may be sent to dLazy's cloud service.

Mitigation: Avoid sensitive material and review any media paths before invoking the skill.

Risk: The skill requires a dLazy API key and an external CLI installation.

Mitigation: Review the pinned CLI package before installing, use a revocable key, and keep credentials private.

Risk: Some documented examples use flags or output types that do not match the dialogue command.

Mitigation: Check `dlazy elevenlabs-dialogue -h` and the model documentation before running examples.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-dialogue)
- [dLazy ElevenLabs Dialogue documentation](https://dlazy.com/en-US/docs/models/audio/elevenlabs-dialogue)
- [dLazy CLI package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy CLI source (not verified skill provenance)](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Text with shell commands and JSON result guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Invoking the CLI returns an audio result URL or an asynchronous task ID; results can optionally be saved locally.]

## Skill Version(s):

1.3.27 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
