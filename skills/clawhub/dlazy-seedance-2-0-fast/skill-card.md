## Description:

Generates videos with Seedance 2.0 Fast from text prompts, multimodal references, or first and last frames.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creators use the skill to generate short videos from text prompts, image, video, or audio references, or first and last frames, then retrieve the generated result.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan was partial and noted a mismatch between the advertised video-generation purpose and the visible login command.

Mitigation: Before installing or authenticating, check the expected login flow and CLI behavior against the publisher’s current documentation; treat the benign scan verdict as limited to the scanned content.

Risk: The skill documentation says prompts and local media inputs are sent to dLazy hosted services, and local media is uploaded for processing.

Mitigation: Use only prompts and media suitable for hosted processing, and review the service’s data terms before submitting sensitive material.

## Reference(s):

- [dLazy service](https://dlazy.com)
- [dLazy API key setup](https://dlazy.com/dashboard/organization/api-key)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)
- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-seedance-2-0-fast)

## Skill Output:

**Output Type(s):** [Video asset, JSON]

**Output Format:** [Hosted video result URL with JSON generation status and metadata]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Accepts text prompts, multimodal references, or first and last frames; supports 4–12 second clips at 480p or 720p.]

## Skill Version(s):

1.3.37 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
