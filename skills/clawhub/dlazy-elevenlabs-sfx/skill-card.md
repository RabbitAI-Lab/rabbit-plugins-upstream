## Description:

Generates short sound effects from text descriptions using the ElevenLabs text-to-sound model through dLazy.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to request short foley, ambience, alert, and game sound effects from text prompts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and explicitly supplied media may be sent to dLazy, and generated files are hosted by dLazy.

Mitigation: Send only material approved for the hosted service and review its data-handling terms before use.

Risk: The third-party npm CLI executes locally and login stores an API key in local configuration.

Mitigation: Review the pinned CLI package before installing, protect the local configuration, and rotate exposed keys.

Risk: The example response shows image/png instead of an audio output.

Mitigation: Verify the returned media type before relying on the example, and correct the documentation.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-sfx)
- [dLazy CLI package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy CLI source referenced by skill metadata (not verified release provenance)](https://github.com/dlazy-ai/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Text with shell commands and JSON response guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The CLI returns a hosted result URL for generated sound effects; optional --save downloads the asset locally.]

## Skill Version(s):

1.3.32 (source: server-resolved ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
