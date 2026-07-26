## Description: <br>
Use when footage needs color correction, white-balance or exposure repair, Log-to-Rec.709 conversion, named creative looks, skin-tone review, or a portable .cube LUT for a cut-as-code delivery. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[whitetowerai](https://clawhub.ai/user/whitetowerai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Video editors, content creators, and agent workflows use this skill to assess source footage, tune a corrective base, compare named looks, record a selection rationale, bake a portable .cube LUT, and apply the chosen grade to final video. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill runs local ffmpeg and Python media-processing commands and reads or writes files in the video project. <br>
Mitigation: Install only when local media processing is acceptable, and review input and output paths before running commands. <br>
Risk: Generated media outputs can overwrite prior generated outputs because the scripts use overwrite flags for media generation. <br>
Mitigation: Use explicit project output directories, keep original source assets separate from generated paths, and check paths before execution. <br>
Risk: Representative-frame and skin-crop heuristics can select a poor review frame for multi-shot or off-center footage. <br>
Mitigation: Review the generated contact sheet and skin-tone check, and provide explicit frame-time or face-crop options when needed. <br>
Risk: Applying a grade changes video pixels and re-encodes the video stream. <br>
Mitigation: Retain source media, choose CRF and preset deliberately, and verify duration, fps, dimensions, audio, and spot frames before delivery. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/whitetowerai/skills/video-color-grade) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with JSON plans, shell commands, review media paths, generated .cube LUTs, and graded video outputs] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces durable grade plans, selected-look notes, review images, optional preview clips, a selected LUT, and graded video files when the bundled scripts are run.] <br>

## Skill Version(s): <br>
1.0.1 (source: server evidence release.version) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
