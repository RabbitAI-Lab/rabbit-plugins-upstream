## Description:

Audio generation skill. Automatically selects the best dlazy CLI audio/TTS model based on the prompt.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creators use this skill to generate speech, dialogue, music, and sound effects from prompts by selecting a suitable dLazy audio model.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and supplied media are sent to dLazy services, and generated results are hosted there.

Mitigation: Use the service only when you accept dLazy processing those prompts and media; review the service terms before sending sensitive content.

Risk: The CLI stores an organization API key in its local configuration, and generation uses service credits.

Mitigation: Protect the local configuration, rotate or revoke the key when needed, and check available credits before generation.

## Reference(s):

- [dLazy CLI repository (metadata link)](https://github.com/dlazy-ai/cli)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Audio, URLs]

**Output Format:** [Generated audio files hosted at URLs, with JSON response metadata]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Available formats and characteristics depend on the selected audio model.]

## Skill Version(s):

1.3.36 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
