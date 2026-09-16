## Description:

ElevenLabs text-to-sound model that generates 1-22 second short sound effects from a description for foley, ambience, alerts, and game SFX.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to ask an agent to generate short sound effects from text prompts through the dLazy CLI and hosted API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a dLazy API key that may be stored in local CLI configuration or supplied through an environment variable.

Mitigation: Use a revocable API key, restrict access to local configuration files, and rotate the key if the configuration may have been exposed.

Risk: The skill relies on the external @dlazy/cli npm package and sends prompts or provided media paths to hosted dLazy services.

Mitigation: Review and trust the pinned CLI package before use, prefer npx for temporary execution when appropriate, and avoid sending sensitive prompts or files.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-sfx)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated sound effects are returned as hosted output URLs and can be saved locally with the CLI.]

## Skill Version(s):

1.3.15 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
