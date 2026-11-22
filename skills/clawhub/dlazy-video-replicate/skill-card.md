## Description:

Video replicate tool: extracts the first frame and audio from the source video, runs video understanding for a prompt, and returns a Seedance 2.0 replicate bundle (first frame + audio + video).

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to analyze a source video and request a Seedance 2.0 replication bundle containing a first frame, audio, video, and a descriptive prompt.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release scan was benign with medium confidence and partial coverage; it did not confirm the advertised video replication workflow.

Mitigation: Check the CLI's current behavior and inspect generated outputs before relying on them.

Risk: Source video files and prompts may be sent to dLazy's hosted API, and local media files are uploaded to its media storage.

Mitigation: Avoid submitting sensitive media or prompts unless the service is approved for that content.

## Reference(s):

- [Video Replicate skill release](https://clawhub.ai/dlazyai/skills/dlazy-video-replicate)
- [CLI project page listed in skill metadata](https://github.com/dlazy-ai/cli)
- [dLazy CLI package on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Images, Audio, Video, Text, JSON]

**Output Format:** [JSON result containing generated asset URLs and metadata]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [An asynchronous request may initially return a task ID without generated assets.]

## Skill Version(s):

1.3.42 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
