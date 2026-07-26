## Description: <br>
Analyzes short videos by extracting keyframes, transcribing speech, reviewing visual elements, and generating Chinese HTML reports with reusable AI video prompts, subtitle timelines, production guidance, compliance checks, and 10-second adaptation plans. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[pdxingqq](https://clawhub.ai/user/pdxingqq) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Content creators, marketing teams, and developers use this skill to inspect short videos, reconstruct scripts and storyboards, and prepare Chinese prompts, subtitles, HTML reports, and reference images for secondary creation workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The workflow runs local ffmpeg and Whisper automation over user-provided videos and writes extracted frames, transcripts, HTML reports, and reference images. <br>
Mitigation: Use a dedicated input folder, temporary directory, and output directory so generated files stay isolated from unrelated personal or production files. <br>
Risk: The workflow may reorganize processed originals into a processed-video folder. <br>
Mitigation: Run the skill on copies when originals must remain untouched, and review output and archive paths before execution. <br>
Risk: Some scripts include hard-coded Windows and WorkBuddy paths for Python, ffmpeg, video inputs, and output directories. <br>
Mitigation: Review and update path constants and ffmpeg configuration for the local environment before running batch or one-shot processing. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/pdxingqq/skills/short-video-reverse-engineer) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, Files, Shell commands, Configuration, Guidance] <br>
**Output Format:** [HTML reports, JSON summaries and configuration, JPEG reference images, and text guidance with shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs are generated locally from user-provided video files and include Chinese prompt text and 9:16 short-video adaptation guidance.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
