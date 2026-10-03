## Description:

Generates 1–22-second sound effects from text descriptions using ElevenLabs through the dLazy CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to generate short foley, ambient, alert, and game sound effects from text prompts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and explicitly supplied media files are sent to the dLazy cloud service.

Mitigation: Avoid sending sensitive prompts or media unless the service's handling is acceptable for the task.

Risk: The third-party CLI can store a dLazy API key in local configuration.

Mitigation: Review the pinned CLI before installation, protect the key, and use a per-invocation environment variable when local storage is undesirable.

Risk: The documented image/PNG output example may mislead users about generated audio output.

Mitigation: Confirm the actual output format before relying on the example or processing the result.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-sfx)
- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Files]

**Output Format:** [JSON result with a hosted sound-effect URL; optional downloaded asset]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Async mode returns a task ID; the documented PNG example does not match the sound-effect use case.]

## Skill Version(s):

1.3.24 (source: ClawHub release metadata; skill frontmatter lists 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
