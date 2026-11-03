## Description:

Creates speech from text with Alibaba Bailian Qwen3-TTS, using a curated voice or a voice described in natural language.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other agent users can turn text into speech with Qwen3-TTS, choosing a supported system voice or describing a custom voice. The skill can return the generated audio as a hosted result or save it locally.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Text and any selected media are sent to dLazy for cloud processing.

Mitigation: Avoid sending sensitive content unless its use with the service is appropriate.

Risk: The CLI stores an API key locally, and anyone with access to it may be able to use the associated account.

Mitigation: Protect the saved key and rotate or revoke it from the dLazy dashboard if needed.

Risk: Speech generation can consume account credits.

Mitigation: Review the prompt and cost estimate with the documented dry-run option before generating when cost is a concern.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-qwen-tts)
- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI on npm (listed in skill metadata)](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Audio, JSON, Shell commands]

**Output Format:** [Generated audio asset or hosted audio URL with JSON result metadata; the skill is invoked with CLI commands.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Speech is generated from text; results may be asynchronous and can be saved to a local path.]

## Skill Version(s):

1.3.37 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
