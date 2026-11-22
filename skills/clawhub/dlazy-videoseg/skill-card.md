## Description:

Segments people in a video and returns a same-length black-and-white mask video for compositing or matting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and video editors can use the skill to create human-segmentation masks for video compositing and matting workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan was partial and could not resolve the external CLI package; it also reported a mismatch between the declared segmentation purpose and visible CLI commands.

Mitigation: Review the pinned CLI package and its permissions before installing, and confirm its commands and outputs meet your needs.

Risk: Video inputs and request details are sent to dLazy's hosted service for processing.

Mitigation: Review the service terms and submit only video content authorized for external processing.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-videoseg)
- [dLazy](https://dlazy.com)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Video mask assets, JSON]

**Output Format:** [JSON result containing a generated black-and-white mask video asset]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The mask video is intended for downstream compositing or matting; asynchronous requests can return a task identifier before the asset is ready.]

## Skill Version(s):

1.3.43 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
