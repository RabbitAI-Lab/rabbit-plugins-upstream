## Description:

Segments people from a video through dLazy's hosted video-segmentation service and returns a same-length black-and-white mask video for downstream compositing or matting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and video-production users create a human-segmentation mask video for compositing or background-removal workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected videos are uploaded to dLazy for cloud processing and may contain sensitive footage.

Mitigation: Review the service's privacy and retention terms and avoid submitting sensitive footage unless approved.

Risk: Authentication may save an organization API key in the local CLI configuration.

Mitigation: Restrict access to the local configuration or use the documented DLAZY_API_KEY environment-variable option.

Risk: Video processing may consume paid organization credits.

Mitigation: Check the cost estimate with --dry-run and confirm credit availability before processing.

Risk: Some usage examples may be inconsistent.

Mitigation: Check the current videoseg help output before invoking the command.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-videoseg)
- [dLazy CLI package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Video, JSON]

**Output Format:** [JSON result with output asset URL; optionally a saved mask-video file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The mask video matches the source duration; asynchronous runs may return a task ID.]

## Skill Version(s):

1.3.34 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
