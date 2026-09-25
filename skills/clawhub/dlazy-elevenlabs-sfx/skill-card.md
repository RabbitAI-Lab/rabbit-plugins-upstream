## Description:

Generates short ElevenLabs sound effects from a text prompt through the dLazy CLI and hosted API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, creators, and agents use this skill to request 1-22 second foley, ambience, alert, or game sound effects from a text description and retrieve the generated asset.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and referenced media may be sent to a third-party cloud service.

Mitigation: Use the skill only for content that is appropriate to send to dLazy, and review applicable service terms before production use.

Risk: The dLazy API key is stored locally or supplied through an environment variable.

Mitigation: Protect the local config and environment, rotate or revoke keys from the dLazy dashboard when needed, and avoid exposing keys in logs or shared prompts.

Risk: The artifact's output-format example describes an image/png result even though the skill generates sound effects.

Mitigation: Validate returned output type, MIME type, and saved file extension before wiring the result into downstream automation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-sfx)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, JSON, Files, Guidance]

**Output Format:** [CLI commands and JSON responses containing generated asset URLs, with optional saved audio files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires npm or npx, a dLazy API key, and network access to api.dlazy.com and files.dlazy.com.]

## Skill Version(s):

1.3.20 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
