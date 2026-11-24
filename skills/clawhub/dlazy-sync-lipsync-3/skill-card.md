## Description:

Given an input video and audio, this skill uses fal.ai sync-lipsync v3 to generate a video in which the speaker's lip movements match the audio.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and media creators can use the skill to synchronize a speaker's mouth movements in a supplied video with supplied audio for dubbing, localization, or virtual presenter re-syncing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan marked the skill benign with medium confidence but did not demonstrate the advertised lip-sync workflow, and some references were unavailable for review.

Mitigation: Review the CLI installation details and relevant references, then confirm the dLazy login and API-key setup before use.

Risk: The skill sends prompts and supplied media to dLazy's hosted API and media storage.

Mitigation: Use only prompts and media that are appropriate to send to the dLazy service.

## Reference(s):

- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy](https://dlazy.com)
- [dLazy API key setup](https://dlazy.com/dashboard/organization/api-key)

## Skill Output:

**Output Type(s):** [Video files, Shell commands, Configuration instructions, JSON result and status data]

**Output Format:** [Generated video asset with JSON result or asynchronous task status]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Accepts video and audio inputs; supports sync modes and optional asynchronous execution.]

## Skill Version(s):

1.3.43 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
