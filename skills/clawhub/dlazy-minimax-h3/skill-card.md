## Description:

MiniMax Hailuo omni-modal video model with native stereo audio, producing 5-15 second clips at up to 2K. Supports text-to-video, first/last frame transitions and multi-asset references for character and scene consistency.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creative teams use this skill to generate short MiniMax Hailuo videos from text prompts, first and last frames, or reference images, videos, and audio.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security assessment has medium confidence and partial coverage; the CLI implementation and referenced external components were not verified, and the guidance notes a 4K discrepancy.

Mitigation: Before installing, review the package details and disclosed dLazy service use, and confirm resolution support if 4K output matters.

## Reference(s):

- [dLazy CLI project page (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI package on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service homepage](https://dlazy.com)
- [dLazy API service](https://api.dlazy.com)
- [dLazy media hosting service](https://files.dlazy.com)

## Skill Output:

**Output Type(s):** [Video/media assets, JSON]

**Output Format:** [Hosted video asset URLs with JSON result metadata]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated clips are typically 5-15 seconds; the release summary describes output up to 2K.]

## Skill Version(s):

1.2.35 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
