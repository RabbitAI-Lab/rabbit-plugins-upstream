## Description: <br>
Audio-Segmenter helps agents split a single audio file or a folder of audio files into fixed-duration segments while preserving the source folder structure. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[wangminrui2022](https://clawhub.ai/user/wangminrui2022) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to split long audio files or folders into fixed-duration clips for speech datasets, karaoke or cover preparation, and audio asset organization. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can automatically install Python packages and change Python tooling during execution. <br>
Mitigation: Run it only in an isolated environment where automatic package installation and toolchain changes are acceptable. <br>
Risk: The skill can download FFmpeg automatically before processing audio. <br>
Mitigation: Use a trusted network environment or preinstall and review FFmpeg before running the skill. <br>
Risk: Recursive folder processing can read many local audio files and write generated output files and logs. <br>
Mitigation: Use non-sensitive input directories, set an explicit output directory, and review generated files before reuse. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/wangminrui2022/skills/audio-segmenter) <br>
- [Publisher profile](https://clawhub.ai/user/wangminrui2022) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Files, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and generated audio segment files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Accepts an input path, segment duration, optional output directory, and optional recursive mode; writes audio clips and logs.] <br>

## Skill Version(s): <br>
1.1.9 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
