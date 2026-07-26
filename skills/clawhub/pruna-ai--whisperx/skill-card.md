## Description: <br>
Use when an agent needs word-level timestamps from audio for lyric alignment, caption timing, or video-edit cut boundaries. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[pruna-ai](https://clawhub.ai/user/pruna-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, media creators, and agents use this skill to transcribe audio with word-level timing for lyric-synced edits, captions, and cut alignment. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Audio is sent to Replicate for transcription and may involve paid API usage. <br>
Mitigation: Confirm external processing is acceptable, verify REPLICATE_API_TOKEN is configured, and avoid sensitive audio unless that processing is approved. <br>
Risk: Optional prerequisite skills and full-suite installation can expand the agent workflow beyond transcription. <br>
Mitigation: Review prerequisite skills before installation and load only the skills needed for the task. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/pruna-ai/skills/whisperx) <br>
- [Replicate model page: victor-upmeet/whisperx](https://replicate.com/victor-upmeet/whisperx) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and references to JSON and SRT transcript outputs] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires REPLICATE_API_TOKEN and an HTTPS audio_file; align_output enables word-level timing.] <br>

## Skill Version(s): <br>
1.0.7 (source: server release metadata and artifact metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
