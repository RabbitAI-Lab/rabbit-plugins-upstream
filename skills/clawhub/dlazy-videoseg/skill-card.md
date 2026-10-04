## Description:

Helps agents use dLazy's cloud service to segment people in a video and obtain a same-length black-and-white mask video for compositing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers can request a human-segmentation mask for a video to use in subsequent compositing or matting workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Videos provided to the cloud service may be uploaded to dLazy storage.

Mitigation: Confirm that sharing the video with dLazy is acceptable before submitting it.

Risk: Logging in can save an API key locally.

Mitigation: Protect the local account and rotate or revoke the key if it is exposed.

Risk: The documented --prompt examples and image/png sample conflict with the described video-mask workflow.

Mitigation: Check the CLI help and actual result before relying on example commands or output types.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-videoseg)
- [dLazy CLI source (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown guidance with CLI examples and a JSON response containing a mask-video URL]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Asynchronous requests can return a task ID for later status checks; the result can be saved locally.]

## Skill Version(s):

1.3.26 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
