## Description:

ElevenLabs text-to-sound model generates 1-22 second short sound effects from a description for foley, ambience, alerts, and game SFX.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, creators, and external users use this skill to ask an agent to generate short sound effects through the dLazy ElevenLabs SFX CLI from a text prompt.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on an external @dlazy/cli package and hosted dLazy service.

Mitigation: Review and trust the package and service before installation or use, and keep the CLI pinned to the documented version unless deliberately upgrading.

Risk: Prompts and explicitly provided media paths may be sent to dLazy, and generated outputs may be hosted on files.dlazy.com.

Mitigation: Avoid sending sensitive prompts or media unless that data handling is acceptable for the user's organization and use case.

Risk: Using dlazy login or dlazy auth set stores an API key in local configuration.

Mitigation: Protect the local config file, prefer scoped keys, and rotate or revoke keys from the dLazy dashboard when access changes.

Risk: The artifact documentation shows image output examples for an audio sound-effects skill.

Mitigation: Treat the output example as a documentation defect and verify actual returned audio assets during release validation.

## Reference(s):

- [Skill page](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-sfx)
- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Files, Guidance]

**Output Format:** [JSON responses and generated audio asset URLs, with optional saved files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires npm or npx, a dLazy API key, and network access to dLazy service endpoints.]

## Skill Version(s):

1.3.17 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
