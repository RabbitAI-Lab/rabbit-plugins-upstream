## Description:

Synthesizes text into natural-sounding speech using Doubao TTS through dLazy's hosted service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other users can turn Chinese or English text into spoken audio, choosing a voice and playback speed for their application.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Text prompts are sent to dLazy's hosted service.

Mitigation: Avoid submitting sensitive text unless its disclosure to dLazy is acceptable.

Risk: The CLI may save an API key in local configuration.

Mitigation: Keep the key secret and use a per-session DLAZY_API_KEY on shared machines.

Risk: Running an external npm CLI introduces supply-chain exposure.

Mitigation: Review the package and its source before installing or running it.

Risk: Default voice settings may not match the intended language or speaker.

Mitigation: Choose the language and voice explicitly before generating audio.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-doubao-tts)
- [dLazy CLI source linked in skill metadata](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON responses, Audio files]

**Output Format:** [CLI guidance and JSON results with hosted media links or a saved local file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Asynchronous requests return a task ID for later polling.]

## Skill Version(s):

1.3.21 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
