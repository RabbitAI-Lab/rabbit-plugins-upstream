## Description: <br>
Converts webm/mp4 video files to optimized GIFs via ffmpeg with configurable quality settings. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and content creators use this skill to convert local webm, mp4, mov, or avi recordings into optimized animated GIFs for demos and documentation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generic trigger words may activate the skill for broader video or optimization requests. <br>
Mitigation: Confirm that the user intends GIF conversion before applying the workflow. <br>
Risk: Conversion commands operate on local input and output file paths. <br>
Mitigation: Validate the source video path and confirm the destination GIF path before running ffmpeg. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-scry-gif-generation) <br>
- [Project homepage from metadata](https://github.com/athola/claude-night-market/tree/master/plugins/scry) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration] <br>
**Output Format:** [Markdown with inline bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces ffmpeg command guidance and verification steps for generating GIF files.] <br>

## Skill Version(s): <br>
1.9.17 (source: evidence.release.version) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
