## Description:

Alibaba Bailian qwen3-tts text-to-speech lets users choose curated system voices, including dialects, or design a custom voice from a natural-language description.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other users can turn text into speech with Qwen TTS, selecting a built-in voice or describing a custom voice and language. The skill sends requests through the dLazy hosted service and returns generated audio results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Text prompts are sent to the dLazy hosted service, and generation uses account credits.

Mitigation: Review dLazy's privacy terms before sending sensitive text, and check account credit usage.

Risk: The CLI stores a dLazy API key in local configuration when users sign in or save a key.

Mitigation: Protect the saved key and rotate or revoke it from the dLazy dashboard if it is exposed.

## Reference(s):

- [dLazy CLI package on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Audio, JSON]

**Output Format:** [Generated audio asset URL with JSON result and task status metadata]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Asynchronous requests can return a generation ID before the audio result is ready.]

## Skill Version(s):

1.3.36 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
