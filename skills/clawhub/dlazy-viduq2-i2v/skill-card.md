## Description:

Converts a static image into a dynamic video with the Vidu Q2 image-to-video model.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creators use it to animate still images into short videos from a prompt and reference image or first and last frames. Use requires a dLazy API key, and supplied media is sent to dLazy's hosted service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan reports a mismatch between the skill's video-generation description and a CLI login command, and says some references were unresolved.

Mitigation: Review the supplied CLI/package references and confirm the command behavior before installing or invoking the skill.

Risk: Prompts and local media supplied for generation are sent to dLazy's hosted API and media storage.

Mitigation: Avoid sending confidential images, audio, or prompts unless their use with the hosted service is acceptable.

## Reference(s):

- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI package on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Video, JSON]

**Output Format:** [Generated video asset URL with JSON result metadata]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Accepts a prompt and reference image(s) or first and last frames, with options for duration, aspect ratio, resolution, and audio.]

## Skill Version(s):

1.3.40 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
