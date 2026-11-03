## Description:

Video human segmentation tool that calls Aliyun's asynchronous SegmentVideoBody service and returns a same-duration black-and-white mask video for compositing or matting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers can submit a video to create a same-duration black-and-white human-segmentation mask for compositing or matting. The result can be saved locally or passed to a downstream video workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected videos are uploaded to dLazy-hosted storage for processing.

Mitigation: Submit only videos you are authorized to share, and consider their sensitivity before uploading.

Risk: The organization API key can authorize paid processing and access to the dLazy account.

Mitigation: Keep the key private and rotate or revoke it if exposed; use the documented login flow or a protected local configuration.

Risk: Documented command examples may be inconsistent, and processing can incur costs.

Mitigation: Check `dlazy videoseg -h` and use `--dry-run` to review the payload and cost estimate before processing.

## Reference(s):

- [dLazy service homepage](https://dlazy.com)
- [CLI project page listed in skill metadata](https://github.com/dlazy-ai/cli)
- [dLazy CLI package on npm](https://www.npmjs.com/package/@dlazy/cli)
- [ClawHub release page](https://clawhub.ai/dlazyai/skills/dlazy-videoseg)

## Skill Output:

**Output Type(s):** [Video files, JSON]

**Output Format:** [A black-and-white mask video and a JSON result envelope containing output details]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Mask video matches the input duration; it can be downloaded to a local path.]

## Skill Version(s):

1.3.38 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
