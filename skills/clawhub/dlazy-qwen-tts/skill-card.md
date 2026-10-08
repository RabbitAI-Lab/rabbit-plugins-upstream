## Description:

Generates speech from text with Qwen3-TTS using preset voices or a voice designed from a natural-language description.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to turn text into speech with a preset or custom-described voice through dLazy's hosted service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Text prompts are sent to dLazy's hosted API.

Mitigation: Avoid sending sensitive text unless the service's data handling is acceptable for the use case.

Risk: Use requires a third-party account and a dLazy API key that may be saved locally.

Mitigation: Protect the key, use per-invocation credentials if preferred, and rotate or revoke it if exposed.

Risk: The skill's sample output describes an image despite its text-to-speech purpose.

Mitigation: Verify the actual response type and result URL before parsing or using generated audio.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-qwen-tts)
- [dLazy CLI repository (linked in skill metadata; skill import provenance unavailable)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, Text]

**Output Format:** [Markdown with shell commands and generated-result links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The CLI returns JSON containing a result URL or an asynchronous task ID; a local download can be requested.]

## Skill Version(s):

1.3.26 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
