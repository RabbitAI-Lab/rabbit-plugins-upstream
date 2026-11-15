## Description:

This skill describes a workflow for extracting a source video's first frame and audio, using video understanding to form a prompt, and returning a Seedance 2.0 replication bundle.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers can use this skill to prepare a Seedance 2.0 replication bundle from a reference video, including its first frame, audio, and generated video.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review reports a partial scan and a mismatch between the advertised video workflow and the visible login setup.

Mitigation: Review the CLI installation and account setup details before use, as advised by the security guidance.

Risk: The documented workflow sends prompts to dLazy's hosted API and uploads local media files to its media storage.

Mitigation: Use only media and prompts that are appropriate to share with the hosted service.

## Reference(s):

- [dLazy website](https://dlazy.com)
- [CLI project page listed in skill metadata](https://github.com/dlazy-ai/cli)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [JSON, Image, Audio, Video]

**Output Format:** [JSON result with generated asset URLs; asynchronous requests may return a task identifier and status]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The described bundle includes a first-frame image, audio, and video; available outputs depend on task completion.]

## Skill Version(s):

1.3.40 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
