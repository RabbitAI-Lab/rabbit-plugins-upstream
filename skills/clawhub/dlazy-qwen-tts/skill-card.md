## Description:

Generate speech from text with Alibaba Bailian Qwen3-TTS using preset voices, including dialects, or custom voices described in natural language.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to turn text into speech with a preset voice or a voice designed from a description, through the dLazy service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Speech prompts are sent to the dLazy cloud service.

Mitigation: Avoid submitting sensitive text without approval for third-party processing.

Risk: Authentication setup may save an API key on the local device.

Mitigation: Protect the local configuration and rotate or revoke the key if exposed.

Risk: The example response shows an image rather than an audio result.

Mitigation: Check the actual output type and asset before relying on the example.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-qwen-tts)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, Configuration instructions]

**Output Format:** [Markdown with shell commands and references to generated speech assets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The CLI returns an asset URL or saves a result locally; asynchronous requests return a task ID.]

## Skill Version(s):

1.3.27 (source: ClawHub release metadata; artifact frontmatter lists 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
