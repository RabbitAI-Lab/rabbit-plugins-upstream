## Description: <br>
Downloads videos from supported URLs and transcribes spoken content into timestamped segments and full text using yt-dlp and openai-whisper. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xunx33](https://clawhub.ai/user/xunx33) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, content operators, and agents use this skill to download online videos and generate timestamped transcripts plus copyable full text for editing, review, or reuse. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The transcription helper is reported to execute generated Python containing user-provided prompt text, which could allow crafted input to run local code. <br>
Mitigation: Review before installing, use only trusted inputs, and patch the helper so prompts are passed as data rather than embedded in executable Python. <br>
Risk: Global yt-dlp configuration can affect download behavior across sessions. <br>
Mitigation: Prefer skill-scoped environment variables and output paths, and enable global yt-dlp configuration only when that cross-session behavior is intended. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Terminal output with timestamped transcript segments and full plain text.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May save downloaded video files to the configured download directory.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
