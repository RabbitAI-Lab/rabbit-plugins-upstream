## Description: <br>
This skill analyzes short videos by extracting audio, key frames, transcript segments, and OCR subtitles into an aligned timeline, then helps generate rewritten viral-video scripts. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[fanyangwuye](https://clawhub.ai/user/fanyangwuye) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External creators, marketers, and developers use this skill to break down viral short videos, inspect timing and visual/text cues, and produce alternate scripts for reuse or adaptation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: First run may download Python packages and large OCR/transcription models and create several gigabytes of local files. <br>
Mitigation: Run it in a dedicated workspace with adequate disk space and review network access expectations before execution. <br>
Risk: Downloaded or user-provided videos, extracted audio, frames, and transcripts may contain private or copyrighted content. <br>
Mitigation: Use a dedicated output folder and process only content the user is authorized to download, store, and transform. <br>


## Reference(s): <br>
- [Prompt templates](references/prompt_templates.md) <br>
- [ClawHub skill page](https://clawhub.ai/fanyangwuye/skills/video-vl-replicate) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and generated JSON analysis files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The pipeline writes analysis.json plus intermediate audio and frame files in the selected work directory.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
