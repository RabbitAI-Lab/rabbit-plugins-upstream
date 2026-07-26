## Description: <br>
Generates SRT subtitles from video or audio, with Hebrew and English transcription, Hebrew-to-English translation, and optional burned-in captions for social-media video. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ngutman](https://clawhub.ai/user/ngutman) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers, creators, and media operators use this skill to run local transcription workflows that produce transcripts, SRT captions, or hardcoded subtitles for selected media files. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill runs local video-processing commands and can write output files next to the input media or to a specified path. <br>
Mitigation: Run it only on media files you choose, review output paths before execution, and avoid elevated privileges. <br>
Risk: Transcription models may be downloaded or cached during use. <br>
Mitigation: Use it only in environments where model downloads and local cache storage are acceptable. <br>
Risk: Temporary subtitle files may create shared-machine risk where /tmp file races matter. <br>
Mitigation: Avoid running it on shared machines with sensitive media unless the temporary-file behavior has been reviewed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ngutman/skills/video-subtitles) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, files, guidance] <br>
**Output Format:** [Plain text transcripts, SRT subtitle files, MP4 video files, and Markdown guidance with shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create output files next to the input or at a user-specified path; may download and cache transcription models.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
