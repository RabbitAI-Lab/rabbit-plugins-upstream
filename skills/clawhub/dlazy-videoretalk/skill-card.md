## Description:

Tongyi VideoRetalk takes a talking-person video and replacement audio and generates a video with the speaker's mouth movements matched to the audio, optionally using a reference face image to select a person in multi-face videos.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers can submit a talking-person video and replacement audio for lip synchronization, optionally selecting the target face when a video contains multiple people. The skill returns the generated video or an asynchronous task result through dLazy's hosted service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review noted a mismatch between the lip-sync description and the reported login setup, and some referenced material could not be resolved, so the scan evidence is incomplete.

Mitigation: Review the authentication setup and referenced material before installation; keep the dLazy API key private and rotate or revoke it if exposed.

## Reference(s):

- [CLI project listed in skill metadata](https://github.com/dlazy-ai/cli)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Video files, JSON]

**Output Format:** [Generated video file or hosted result URL with JSON task/result metadata]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Cloud-generated lip-synced video; optional reference face image and asynchronous task ID.]

## Skill Version(s):

1.3.42 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
