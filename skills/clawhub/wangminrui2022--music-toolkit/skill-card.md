## Description: <br>
Music Toolkit records system audio playback, saves WAV or MP3 output, and can trim silence from recordings for OpenClaw agents. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[wangminrui2022](https://clawhub.ai/user/wangminrui2022) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and end users use this OpenClaw skill to record computer playback for a requested duration, write audio files to a chosen output directory, and optionally trim silence or prepare music recordings for splitting workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill records system audio and includes keyboard monitoring to stop recording. <br>
Mitigation: Run it only after explicit user consent, keep recording duration bounded, and confirm the output directory before execution. <br>
Risk: The skill can install Python packages, create or use a virtual environment, and download FFmpeg locally. <br>
Mitigation: Prefer an isolated environment, review installation paths first, and approve dependency or FFmpeg downloads before running the scripts. <br>
Risk: Recordings, logs, virtual environment files, dependencies, and FFmpeg binaries may be written to local storage. <br>
Mitigation: Confirm where files will be written and remove recordings, logs, and downloaded tools when they are no longer needed. <br>


## Reference(s): <br>
- [Music Toolkit on ClawHub](https://clawhub.ai/wangminrui2022/skills/music-toolkit) <br>
- [OpenClaw project](https://github.com/openclaw/openclaw) <br>
- [FFmpeg downloads](https://ffmpeg.org/download.html) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Files, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with shell commands and generated WAV or MP3 audio files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses duration, save directory, filename prefix, auto-trim, silence threshold, and minimum silence length parameters.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
