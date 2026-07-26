## Description: <br>
Analyze video files by extracting keyframes with ffmpeg and using vision to understand content. Supports single and batch processing. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[safety1956](https://clawhub.ai/user/safety1956) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and analysts use this skill to extract representative frames and video metadata from single videos or directories, then produce concise visual analysis reports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may read user-selected video files or directories and write extracted JPEG frames and metadata to an output folder. <br>
Mitigation: Use it only on intended input paths and review the generated output folder for sensitive frames or metadata before sharing or retaining results. <br>
Risk: The documented cleanup command deletes the selected output directory recursively. <br>
Mitigation: Verify the exact output directory before running cleanup commands. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, files, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and generated JPEG frames plus metadata text files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Frame extraction density adapts to video duration; batch analysis writes per-video output folders.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
