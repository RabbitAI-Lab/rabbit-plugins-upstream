## Description:

Generates a lip-synced video by matching a talking person's mouth movements to replacement audio, with an optional reference face image for selecting a person in multi-face videos.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and content creators can use the skill to create a lip-synced video by matching a talking person's video to replacement speech, optionally identifying the target face with a reference image.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review notes that the documented task and the CLI login flow do not clearly match, and its benign verdict is not a guarantee of safety.

Mitigation: Before installing and logging in to the pinned CLI, review its behavior and confirm how its authentication supports this task.

Risk: Local media supplied to the skill may be uploaded to dLazy-hosted storage for processing.

Mitigation: Only submit media you are authorized to share with the service, and review the provider's terms before uploading sensitive material.

## Reference(s):

- [CLI repository listed in skill metadata](https://github.com/dlazy-ai/cli)
- [CLI package on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)
- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-videoretalk)

## Skill Output:

**Output Type(s):** [Video, JSON, Shell commands]

**Output Format:** [Generated video URL or saved media file, with a JSON CLI response]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a dLazy API key. Local video, audio, and reference image paths may be uploaded to dLazy-hosted media storage.]

## Skill Version(s):

1.3.38 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
