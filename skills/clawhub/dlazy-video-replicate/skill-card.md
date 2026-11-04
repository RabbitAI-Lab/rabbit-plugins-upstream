## Description:

Analyzes a source video to produce a Seedance 2.0 replication bundle containing a first frame, audio, and video.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Video creators and editors can use this skill to analyze a reference video and prepare a Seedance 2.0 bundle with a first frame, audio, and video.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Source video and prompts are sent to dLazy for processing, and local media files are uploaded to its media storage.

Mitigation: Submit only media you are comfortable uploading to dLazy.

Risk: Login stores a dLazy API key in the local CLI configuration.

Mitigation: Keep the local configuration protected and rotate or revoke the key if needed.

Risk: The external CLI package and hosted service have not been fully audited.

Mitigation: Review the pinned CLI package and service terms before processing sensitive media.

Risk: Processing consumes credits.

Mitigation: Check credit costs before running a video task.

## Reference(s):

- [dLazy service](https://dlazy.com)
- [CLI repository listing](https://github.com/dlazy-ai/cli)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)
- [API key setup](https://dlazy.com/dashboard/organization/api-key)
- [Credit settings](https://dlazy.com/dashboard/organization/settings?tab=credits)

## Skill Output:

**Output Type(s):** [Images, Audio, Video, JSON metadata]

**Output Format:** [JSON response with generated media URLs and optional saved media files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Media is processed by the hosted dLazy service; local media supplied to the CLI is uploaded for processing.]

## Skill Version(s):

1.3.37 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
