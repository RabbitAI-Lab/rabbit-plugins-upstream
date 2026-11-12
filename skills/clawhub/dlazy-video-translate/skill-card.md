## Description:

Transcribes videos with word-level timings, translates subtitles, burns them into the video, and optionally adds a fitted dubbing track.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators and teams use the skill to create translated subtitles and optionally dubbed versions of existing videos.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow can overwrite existing files with its output names.

Mitigation: Review the output filenames and work in a dedicated directory or back up files before running the workflow.

Risk: The workflow stores a dLazy API key in the user's CLI configuration when using the recommended login flow.

Mitigation: Review the local configuration file's access and use a per-invocation DLAZY_API_KEY environment variable if preferred.

Risk: Audio and local media files are uploaded to dLazy media storage for processing.

Mitigation: Only submit media you are authorized to share with the service.

## Reference(s):


## Skill Output:

**Output Type(s):** [Files]

**Output Format:** [MP4 video and SRT subtitle files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Subtitles are produced by default; a fitted dubbed audio track is optional.]

## Skill Version(s):

1.0.31 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
