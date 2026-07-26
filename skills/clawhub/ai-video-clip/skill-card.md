## Description: <br>
AI Video Clip Assistant helps agents transcribe media, build edit decision lists, render clips with FFmpeg, generate or burn subtitles, run quality checks, and export videos for social formats. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dwan25744](https://clawhub.ai/user/dwan25744) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Video creators, editors, and agents use this skill to automate local video editing workflows: transcribing source media, generating reviewable EDL JSON, rendering final clips, adding subtitles, checking output quality, and exporting platform-specific versions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill runs FFmpeg and media-processing scripts over user-controlled local paths, which can affect files outside the intended project if paths or filenames are not reviewed. <br>
Mitigation: Use a dedicated project folder, process only media you trust, review paths before running commands, and avoid unusual or untrusted filenames. <br>
Risk: Generated EDL JSON can produce incorrect, misleading, or unwanted edits if accepted without review. <br>
Mitigation: Preview and review generated EDL files before rendering, use dry-run modes when available, and keep source media unchanged. <br>
Risk: Optional diarization and external model workflows can introduce token and model-dependency risks. <br>
Mitigation: Enable diarization only when the Hugging Face dependency and token handling are understood, and keep tokens out of shared artifacts and logs. <br>


## Reference(s): <br>
- [FFmpeg command reference](references/ffmpeg_cheatsheet.md) <br>
- [ClawHub skill page](https://clawhub.ai/dwan25744/skills/ai-video-clip) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands, JSON EDL files, subtitle files, quality reports, and rendered video files produced by local scripts.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs depend on user-provided local media, FFmpeg, optional ASR models, optional Hugging Face token-backed diarization, and user review of generated EDL JSON before rendering.] <br>

## Skill Version(s): <br>
2.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
