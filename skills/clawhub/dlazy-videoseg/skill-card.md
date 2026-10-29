## Description:

Video human segmentation tool: invokes Aliyun's async SegmentVideoBody and returns a same-length black/white mask video, suitable for downstream compositing or matting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and video editors can submit a video to create a same-length black-and-white human segmentation mask for compositing or matting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected local videos are uploaded to dLazy media storage and processed by its hosted service.

Mitigation: Send only videos you are comfortable sharing with dLazy, and review its service terms and charges first.

Risk: An exposed dLazy API key could allow use of the account or incur service charges.

Mitigation: Keep the key private and rotate or revoke it from the dLazy dashboard if exposed.

Risk: Some usage examples may be inaccurate.

Mitigation: Check `dlazy videoseg -h` and verify the expected video output before relying on a command example.

## Reference(s):

- [dLazy CLI source (listed by the skill)](https://github.com/dlazy-ai/cli)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Video mask, JSON]

**Output Format:** [JSON result with a hosted mask video URL or asynchronous task information; optionally a saved video file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Same-duration black-and-white human segmentation mask for downstream compositing or matting.]

## Skill Version(s):

1.3.36 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
