## Description:

Synchronizes a speaker's mouth movements in a video to a supplied audio track, with an optional reference face image for selecting a person in multi-face videos.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to synchronize a person's mouth movements in an existing video with a new voice track. A reference face image can identify the intended person when a video contains multiple faces.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected video, audio, or reference image files are uploaded to dLazy's hosted service for processing.

Mitigation: Submit only media you are permitted to share and comfortable sending to the service.

Risk: The skill requires a dLazy API key and generation may incur costs.

Mitigation: Keep the API key private and check the command's cost estimate before generating.

Risk: Some usage examples may not match the command's supported options.

Mitigation: Check `dlazy videoretalk -h` for the current supported arguments.

## Reference(s):

- [dLazy](https://dlazy.com)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)
- [Video Retalk on ClawHub](https://clawhub.ai/dlazyai/skills/dlazy-videoretalk)

## Skill Output:

**Output Type(s):** [Video]

**Output Format:** [Generated video asset, returned as a URL or saved locally]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Optional reference face image; generation may complete asynchronously.]

## Skill Version(s):

1.3.36 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
