## Description:

Video human segmentation tool: invokes Aliyun's async SegmentVideoBody and returns a same-length black-and-white mask video for downstream compositing or matting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creators use this skill to send a video to dLazy's hosted video segmentation service and receive a same-length black-and-white mask video for compositing or matting workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected videos and related parameters are sent to dLazy's hosted service.

Mitigation: Confirm the user is comfortable uploading the selected media before invoking the service.

Risk: A stored dLazy API key may remain in the local CLI configuration.

Mitigation: Use npx or the DLAZY_API_KEY environment variable for per-invocation authentication when persistence is not desired, and rotate or revoke keys from the dLazy dashboard when needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-videoseg)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, JSON, Files, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return a hosted output URL, save the generated mask asset locally when requested, or return an async task identifier when no-wait mode is used.]

## Skill Version(s):

1.3.12 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
