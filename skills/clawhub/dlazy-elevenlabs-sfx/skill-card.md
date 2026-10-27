## Description:

ElevenLabs text-to-sound model — generates 1–22s short sound effects from a description, suitable for foley, ambience, alerts, and game SFX.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, game creators, and audio practitioners use this skill to generate short sound effects from text descriptions for foley, ambience, alerts, and games.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and supplied media are sent to dLazy for cloud processing.

Mitigation: Use the skill only with prompts and media you are comfortable processing through dLazy's service.

Risk: Generation uses organization credits, and the API key is stored locally.

Mitigation: Review the cost estimate before generation, protect the locally stored key, and rotate or revoke it when no longer needed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-sfx)
- [dLazy CLI source repository](https://github.com/dlazy-ai/cli)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Audio, JSON]

**Output Format:** [JSON result containing generated sound-effect asset URLs; optionally a saved audio file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Sound effects are 1–22 seconds; asynchronous requests may initially return a task identifier.]

## Skill Version(s):

1.3.33 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
