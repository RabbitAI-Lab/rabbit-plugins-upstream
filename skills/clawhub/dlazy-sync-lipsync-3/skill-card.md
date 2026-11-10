## Description:

Given an input video and audio, this skill uses fal.ai sync-lipsync v3 to generate a video with lip movements matched to the audio.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers can provide a video and an audio track to create a lip-synchronized video for dubbing, localization, or virtual presenters.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The scanner did not verify the lip-sync capability and did not inspect the external CLI.

Mitigation: Review the CLI and dLazy service details before installing the CLI or entering an API key.

Risk: Video and audio files supplied by local path are uploaded to dLazy media storage for processing.

Mitigation: Only submit media you are authorized to share, and confirm the service's handling terms before uploading sensitive content.

## Reference(s):


## Skill Output:

**Output Type(s):** [Video, JSON]

**Output Format:** [Generated video asset URL and JSON task or result details]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The generated media is hosted by dLazy; asynchronous jobs may return a task identifier before the result is ready.]

## Skill Version(s):

1.3.38 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
