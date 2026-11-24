## Description:

This skill submits video for human segmentation and returns a same-length black-and-white mask video for compositing or matting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and video editors can create a human-segmentation mask for a video and use it in compositing or matting workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review reports a mismatch between the stated segmentation purpose and visible login or authentication commands; the CLI package was not inspected and scan coverage is partial.

Mitigation: Review the CLI package and confirm its behavior before installing or using it.

Risk: The skill documentation says local video files and request parameters are sent to dLazy-hosted services.

Mitigation: Submit only videos you are authorized to upload, and review the service terms before processing sensitive footage.

## Reference(s):

- [CLI repository listed in skill metadata](https://github.com/dlazy-ai/cli)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [API calls, JSON, Files]

**Output Format:** [JSON task result with a hosted media URL or asynchronous task status; the result asset can be saved as a local file.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The declared result is a same-length black-and-white human-segmentation mask video.]

## Skill Version(s):

1.3.44 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
