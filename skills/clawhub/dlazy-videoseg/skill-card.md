## Description:

Produces same-length black-and-white human segmentation mask videos by calling dLazy's hosted Aliyun SegmentVideoBody workflow for downstream compositing or matting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, creators, and video-production agents use this skill to submit a video to dLazy and receive a same-length human segmentation mask for compositing or matting workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on a third-party npm CLI and hosted dLazy services.

Mitigation: Use the pinned CLI version with npx or an isolated non-privileged environment, and review the linked package or source before deployment.

Risk: Input videos may be uploaded to dLazy media storage for processing.

Mitigation: Only submit videos approved for upload to dLazy and suitable for processing by the configured organization account.

Risk: Authentication stores a dLazy API key in local CLI configuration or uses DLAZY_API_KEY.

Mitigation: Protect the local config and environment, use least-privileged organization keys where available, and rotate or revoke keys from the dLazy dashboard when needed.

Risk: The security scan notes command/output inconsistencies in the docs.

Mitigation: Run `dlazy videoseg -h` before use and validate required options and result shape in the current CLI version.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-videoseg)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [Markdown guidance with bash commands and JSON CLI output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a dLazy API key; input video files may be uploaded to dLazy-hosted services; results can be returned as URLs or saved locally.]

## Skill Version(s):

1.3.17 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
