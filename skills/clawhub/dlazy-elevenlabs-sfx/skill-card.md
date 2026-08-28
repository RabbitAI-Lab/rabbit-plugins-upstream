## Description:

ElevenLabs text-to-sound model that generates 1-22 second sound effects from a description for foley, ambience, alerts, and game SFX.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and content creators use this skill to ask an agent to generate short sound effects through the dLazy CLI and ElevenLabs SFX model. It is suited for creating foley, ambience, alerts, and game audio assets from text prompts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and any explicitly provided media paths are sent to dLazy-hosted API and file services.

Mitigation: Use the skill only with content appropriate for dLazy-hosted processing, and avoid sending sensitive prompts or media unless the user accepts that service boundary.

Risk: The skill requires a dLazy API key for authenticated API calls.

Mitigation: Use the documented login or per-invocation environment variable flow, and rotate or revoke the key from the dLazy dashboard if exposure is suspected.

Risk: A global CLI install persists a third-party command on the user's system.

Mitigation: Use the documented npx invocation for on-demand execution when a persistent global CLI install is not desired.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-sfx)
- [dLazy CLI Source](https://github.com/dlazyai/cli)
- [dLazy CLI npm Package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy Homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [CLI command guidance and JSON result metadata with generated asset URLs; optional downloaded media file when --save is used.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a dLazy API key and uses the pinned @dlazy/cli 1.2.3 package.]

## Skill Version(s):

1.3.8 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
