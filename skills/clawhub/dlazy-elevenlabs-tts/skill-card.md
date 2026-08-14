## Description:

ElevenLabs eleven_v3 text-to-speech with 12 curated multilingual voices and stability, similarity, and style controls for dubbing, audiobooks, and character dialog.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate text-to-speech audio through the dLazy-hosted ElevenLabs TTS workflow, choosing built-in or custom voices and controlling stability, similarity, and style settings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and any media paths provided to the CLI may be sent to dLazy-hosted services.

Mitigation: Review the dLazy CLI and service terms before use, avoid sending sensitive content unless approved, and prefer DLAZY_API_KEY when avoiding saved local credentials.

Risk: The published output-format example is unreliable for an audio-generation skill.

Mitigation: Validate real command output before building automations that depend on specific output types or MIME values.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-tts)
- [dLazy CLI source](https://github.com/dlazyai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, JSON, Guidance]

**Output Format:** [Markdown guidance with CLI commands and JSON result data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a dLazy API key; async mode can return a generateId for later polling.]

## Skill Version(s):

1.3.6 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
