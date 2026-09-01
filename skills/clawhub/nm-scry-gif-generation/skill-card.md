## Description:

Converts webm/mp4 video files to optimized GIFs via ffmpeg with configurable quality settings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[athola](https://clawhub.ai/user/athola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and technical content authors use this skill to convert local webm, mp4, mov, or avi recordings into shareable animated GIFs with selectable ffmpeg quality and optimization settings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad trigger terms such as gif, ffmpeg, video, conversion, and optimization may activate the skill outside explicit video-to-GIF requests.

Mitigation: Review activation context before use and continue only when the user is asking for GIF generation or video-to-GIF conversion.

Risk: ffmpeg commands operate on local input and output paths.

Mitigation: Confirm the input and output paths before running ffmpeg and install ffmpeg only through a trusted package manager if it is missing.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-scry-gif-generation)
- [OpenClaw homepage](https://github.com/athola/claude-night-market/tree/master/plugins/scry)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration]

**Output Format:** [Markdown with inline bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces ffmpeg command guidance and validation steps for local video-to-GIF conversion; the agent does not directly embed generated GIF bytes in its response.]

## Skill Version(s):

1.9.19 (source: evidence.release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
