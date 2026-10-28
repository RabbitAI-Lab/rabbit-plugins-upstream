## Description:

Generates 10–300 seconds of original music from a natural-language prompt using the ElevenLabs music_v1 model.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and content creators use natural-language prompts to generate original music for background tracks, advertisements, and short-form video. The skill returns generated audio through the dLazy hosted service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and any supplied media are sent to dLazy hosted services, and generation may use account credits.

Mitigation: Only submit content you are comfortable sharing with the service; use the dry-run option to preview the request and cost estimate.

Risk: Login stores an API key in the local dLazy CLI configuration.

Mitigation: Protect the local configuration and rotate or revoke the key when it is no longer needed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-music)
- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy API key dashboard](https://dlazy.com/dashboard/organization/api-key)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Audio files, JSON]

**Output Format:** [Generated audio asset URL and JSON result metadata]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Audio duration is configurable from 10 to 300 seconds; asynchronous mode can return a generation task identifier before the audio is ready.]

## Skill Version(s):

1.3.35 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
