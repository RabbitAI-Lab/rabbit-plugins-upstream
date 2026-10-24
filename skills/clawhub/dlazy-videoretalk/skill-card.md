## Description:

Aligns a talking-person video with replacement speech audio, with an optional reference face image to select a person in multi-face videos.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and content creators use this skill to match a talking person's video to new speech audio. An optional reference face image can identify the target when the video contains multiple people.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local video, audio, and reference-image files are uploaded to dLazy media storage for processing.

Mitigation: Only submit media you are comfortable uploading, and review dLazy privacy terms and generation costs before use.

Risk: The CLI stores an organization API key in local configuration.

Mitigation: Protect the saved API key and rotate or revoke it if exposed.

Risk: Some generic prompt and image-output examples may not match the lip-sync task.

Mitigation: Check the command's current help and options before running it.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-videoretalk)
- [dLazy CLI project](https://github.com/dlazy-ai/cli)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Video, JSON, Shell commands]

**Output Format:** [A generated lip-synced video with a JSON CLI response containing result metadata and a media URL]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Asynchronous runs may initially return a task identifier instead of a completed media result.]

## Skill Version(s):

1.3.33 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
