## Description:

Video human segmentation tool: invokes Aliyun's async SegmentVideoBody and returns a same-length black/white mask video, suitable for downstream compositing or matting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and video editors use this skill to create a same-duration black-and-white human-segmentation mask from a video for compositing or matting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review reports that the CLI login and authentication commands do not clearly match the video-segmentation purpose, and the external CLI package behavior was not inspected.

Mitigation: Review the CLI package and its referenced source before installing or providing an API key.

Risk: The skill uploads local video inputs to dLazy media storage for hosted processing.

Mitigation: Use only footage you are authorized to share with the service, and avoid sending sensitive videos unless that transfer is acceptable.

## Reference(s):

- [dLazy CLI project (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Files, JSON]

**Output Format:** [JSON response containing a mask video asset URL]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The mask video matches the input duration; asynchronous jobs may return a task ID before the asset is ready.]

## Skill Version(s):

1.3.40 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
