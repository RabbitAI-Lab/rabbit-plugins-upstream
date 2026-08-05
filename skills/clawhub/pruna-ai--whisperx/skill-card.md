## Description: <br>
Use when someone needs word-level timestamps from audio for lyric alignment, cut-safe line boundaries, or caption source timing before burn-in with video editing. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[pruna-ai](https://clawhub.ai/user/pruna-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and content-production agents use this skill to turn audio into timestamped transcript artifacts for lyric alignment, caption timing, and downstream video-editing workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The workflow sends selected audio to an external Replicate model and requires a Replicate API token. <br>
Mitigation: Confirm the audio is appropriate to upload to Replicate and handle the API token through the prerequisite API guidance before running the workflow. <br>
Risk: Installing the full Pruna skill suite can add capabilities beyond this WhisperX workflow. <br>
Mitigation: Review prerequisite PrunaAI skills before installation, and install only the needed prerequisite skills when a narrower setup is preferred. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/pruna-ai/skills/whisperx) <br>
- [Replicate model: victor-upmeet/whisperx](https://replicate.com/victor-upmeet/whisperx) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, text, files] <br>
**Output Format:** [Markdown guidance with inline shell commands; generated transcript outputs are JSON and SRT files when the workflow is executed.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a Replicate API token and an HTTPS audio input URL. Optional language, word-alignment, initial prompt, and diarization settings affect transcript detail.] <br>

## Skill Version(s): <br>
1.0.9 (source: server release metadata and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
