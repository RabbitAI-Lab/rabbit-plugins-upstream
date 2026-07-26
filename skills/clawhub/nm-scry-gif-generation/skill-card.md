## Description: <br>
Converts webm/mp4 video files to optimized GIFs via ffmpeg with configurable quality settings. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and content creators use this skill to convert local recordings into optimized GIFs with ffmpeg presets, quality options, and output verification steps. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad trigger words can cause the skill to be considered for general video or conversion tasks. <br>
Mitigation: Confirm the task is GIF conversion and review the ffmpeg command before running it. <br>
Risk: The generated ffmpeg commands operate on local input and output paths. <br>
Mitigation: Verify the source video path and destination GIF path before execution. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-scry-gif-generation) <br>
- [OpenClaw homepage](https://github.com/athola/claude-night-market/tree/master/plugins/scry) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with bash command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces ffmpeg command variants and verification steps for user-selected local video files.] <br>

## Skill Version(s): <br>
1.9.16 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
