## Description:

Guides an agent through planning a short film with key stills, generating Kling 4 takes, and editing the strongest clips into a cinematic video.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vargai](https://clawhub.ai/user/vargai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and their agents use this workflow to plan and produce short films, music videos, sketches, trailers, and story videos with Kling 4, using image references to guide shots and FFmpeg to assemble the edit.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup instructions use an installer without a pinned version.

Mitigation: Verify the installer source and selected version before installing.

Risk: Cast photos and other identifiable references may be sent to external generation services.

Mitigation: Check which services receive the images and confirm that sharing them is acceptable before use.

Risk: The security scan was partial because a referenced local path was missing.

Mitigation: Resolve the missing reference and rerun the scan before relying on its assessment.

## Reference(s):

- [VARG Kling 4 keyframe film guide](https://varg.ai/how-to/skills/kling-4-keyframe-film)
- [Example Kling 4 short film](https://www.youtube.com/watch?v=WzXKggH-0Io)
- [ClawHub skill release](https://clawhub.ai/vargai/skills/kling-4-keyframe-film)

## Skill Output:

**Output Type(s):** [Guidance, Text prompts, API Calls, Shell commands, Video files]

**Output Format:** [Markdown guidance with text prompts and Bash commands; resulting cinematic MP4]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Typical finished film is 60–90 seconds; generation cost varies with settings and retries.]

## Skill Version(s):

1.0.6 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
