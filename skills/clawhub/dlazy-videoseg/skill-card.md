## Description:

Video Segmentation uses the dLazy CLI to invoke Aliyun SegmentVideoBody and return same-length black-and-white human mask videos for downstream compositing or matting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, video teams, and agents use this skill to generate human segmentation masks from input videos through the dLazy cloud CLI. The masks can support downstream compositing, matting, and video editing workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing or running a third-party CLI can introduce supply-chain risk.

Mitigation: Review the dLazy CLI source or npm package before use, and prefer the pinned npx invocation for one-off runs.

Risk: The skill requires a dLazy API key and may read credentials from local config or environment variables.

Mitigation: Limit exposure of credentials, avoid sharing unrelated environment variables, and rotate or revoke the dLazy API key if compromise is suspected.

Risk: Local media paths supplied to video fields may be uploaded to dLazy media storage for processing.

Mitigation: Only pass files intended for cloud processing and confirm the workflow is appropriate for sensitive media.

Risk: The artifact examples use --prompt even though the command options require --video.

Mitigation: Use dlazy videoseg --video with a URL or local video path, and run dlazy videoseg -h to confirm current options.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-videoseg)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [CLI JSON responses with generated video-mask URLs or saved media files, usually summarized in Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a dLazy API key; async runs may return a generateId for later polling.]

## Skill Version(s):

1.3.16 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
