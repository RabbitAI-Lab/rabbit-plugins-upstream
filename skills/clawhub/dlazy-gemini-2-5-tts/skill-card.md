## Description:

Generate multilingual, highly natural audio using Gemini 2.5 text-to-speech.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to generate Mandarin or English speech from text prompts through the dLazy Gemini 2.5 TTS command, returning hosted output URLs or async task status.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and explicitly provided media files are sent to the dLazy cloud service.

Mitigation: Confirm the user is comfortable sharing the prompt and any referenced files with dLazy before invoking the TTS command.

Risk: The dLazy CLI can store an API key in the local user configuration.

Mitigation: Use the per-invocation DLAZY_API_KEY option when persistent local credential storage is not appropriate.

Risk: The skill depends on a pinned third-party npm package and hosted API endpoints.

Mitigation: Review the pinned npm package or source and allow api.dlazy.com and files.dlazy.com only in environments that approve those dependencies.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-gemini-2-5-tts)
- [dLazy CLI homepage](https://github.com/dlazyai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Audio URLs, Configuration guidance]

**Output Format:** [Markdown instructions with bash commands and JSON CLI responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated media is hosted on files.dlazy.com; --no-wait can return an async task ID for polling.]

## Skill Version(s):

1.3.7 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
