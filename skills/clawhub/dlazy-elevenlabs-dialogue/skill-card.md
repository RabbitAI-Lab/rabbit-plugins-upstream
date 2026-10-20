## Description:

Generates multi-voice dialogue audio from lines of text using ElevenLabs eleven_v3 through dLazy.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to turn scripted conversations into character dialogue, podcast segments, and short audio scenes with distinct voices.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Dialogue text and any supplied files are sent to dLazy's hosted service.

Mitigation: Share only content appropriate for the hosted service and review its terms before sending sensitive material.

Risk: Persistent CLI installation or saved credentials may not suit every environment.

Mitigation: Consider the pinned on-demand CLI and an environment-provided API key instead of a global install or saved key.

Risk: Documented arguments and output examples are inconsistent with the described audio workflow.

Mitigation: Check the installed CLI help and test the expected output before relying on the examples.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-dialogue)
- [dLazy CLI source (listed in skill metadata; import provenance unavailable)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Text instructions and JSON response with a link to generated audio]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports distinct voices per line and optional download of generated audio.]

## Skill Version(s):

1.3.31 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
