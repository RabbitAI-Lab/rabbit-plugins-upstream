## Description:

Generate multilingual, highly natural audio using Gemini 2.5 text-to-speech.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and content creators use this skill to generate Chinese or English speech from prompts with Gemini 2.5 TTS and select a supported voice. The generated audio is hosted by dLazy and returned through the CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and generation parameters are sent to the dLazy hosted service for processing.

Mitigation: Avoid submitting sensitive content unless remote processing is appropriate.

Risk: Using the external dLazy CLI and service requires trust and generation may consume paid credits.

Mitigation: Review the pinned CLI package before installation and check account credits before generating audio.

Risk: The CLI requires an API key that is saved in local configuration when using its login or auth commands.

Mitigation: Protect the API key and rotate or revoke it if it may have been exposed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-gemini-2-5-tts)
- [dLazy](https://dlazy.com)
- [dLazy CLI package on npm](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Audio, JSON]

**Output Format:** [Hosted audio URL in a JSON response]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Chinese or English speech with a selectable voice; generated audio is hosted by dLazy.]

## Skill Version(s):

1.3.34 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
