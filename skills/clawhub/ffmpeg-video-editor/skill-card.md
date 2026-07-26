## Description: <br>
Generate FFmpeg commands from natural language video editing requests for cutting, trimming, converting, compressing, changing aspect ratio, extracting audio, and related video operations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mahmoudadelbghany](https://clawhub.ai/user/mahmoudadelbghany) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers, creators, and technical users use this skill to translate everyday video editing requests into ready-to-run FFmpeg command suggestions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated FFmpeg commands include `-y`, which overwrites output files by default. <br>
Mitigation: Review input and output filenames before running commands, and remove `-y` when existing files should not be overwritten. <br>
Risk: The skill provides command templates and does not install or verify FFmpeg itself. <br>
Mitigation: Install FFmpeg from a trusted source and review generated commands before execution. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/mahmoudadelbghany/skills/ffmpeg-video-editor) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown with inline bash code blocks and brief explanatory text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands include generated or assumed filenames when the user does not provide an output path.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
