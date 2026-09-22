## Description:

Video human segmentation tool that invokes Aliyun's async SegmentVideoBody service through the dLazy CLI and returns a same-length black/white mask video for downstream compositing or matting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and video-production agents use this skill to submit a video URL or local video path to dLazy and receive a segmentation mask asset for downstream compositing or matting workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow sends videos, parameters, and generated assets to the third-party dLazy service.

Mitigation: Use the skill only for content approved for dLazy processing and confirm that the dLazy service terms and data handling meet the deployment requirements.

Risk: The dLazy CLI may store an API key in the local user configuration.

Mitigation: Prefer scoped organization keys, rotate or revoke keys from the dLazy dashboard when needed, and use per-invocation environment variables where persistent local credentials are not desired.

Risk: The artifact documentation has rough edges around exact command arguments and output media type.

Mitigation: Run `dlazy videoseg -h` before use and validate expected inputs and returned asset types in a dry run or low-risk test.

Risk: Installing the pinned package globally persists a third-party binary on the host.

Mitigation: Review the pinned package or source before installation, or use the documented `npx @dlazy/cli@1.2.3` form to avoid a persistent global install.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-videoseg)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The invoked CLI returns hosted media URLs for generated mask assets and may return async task metadata when no-wait mode is used.]

## Skill Version(s):

1.3.20 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
