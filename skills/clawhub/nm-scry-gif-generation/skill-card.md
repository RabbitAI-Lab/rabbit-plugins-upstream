## Description: <br>
Converts webm/mp4 video files to optimized GIFs via ffmpeg with configurable quality settings. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to convert webm, mp4, mov, or avi recordings into shareable GIFs with selectable frame rate, scale, palette, and dithering settings. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generic video or conversion requests may activate the skill more broadly than intended. <br>
Mitigation: Confirm that the user wants video-to-GIF conversion before applying the skill. <br>
Risk: Generated ffmpeg commands may use unintended input or output paths. <br>
Mitigation: Review the command paths with the user before execution and verify the produced GIF file afterward. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-scry-gif-generation) <br>
- [Metadata homepage](https://github.com/athola/claude-night-market/tree/master/plugins/scry) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands] <br>
**Output Format:** [Markdown with inline bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces ffmpeg command guidance and output verification steps for GIF files.] <br>

## Skill Version(s): <br>
1.9.17 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
