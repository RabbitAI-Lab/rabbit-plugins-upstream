## Description:

Uses Tongyi VideoRetalk to generate a talking-person video whose mouth movements match a supplied voice track, with an optional reference face image to select a person.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators and developers can use this skill to synchronize a speaker's mouth movements in a video with a replacement voice track. They can provide a reference face image when the video contains multiple people.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Video, audio, and optional face images supplied from local paths are uploaded to dLazy-hosted services for processing.

Mitigation: Use only media you are comfortable uploading and have permission to process.

Risk: The CLI stores API credentials locally, and video generation may incur service costs.

Mitigation: Prefer device-code login over sharing a key in chat, revoke or rotate saved keys when needed, and check generation costs before submitting.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-videoretalk)
- [CLI project page (listed in skill metadata; provenance unavailable)](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Video, JSON]

**Output Format:** [Generated video asset link with JSON task and result metadata]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Video and audio inputs are required; an optional reference face image can select the target person.]

## Skill Version(s):

1.3.35 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
