## Description: <br>
PureVocals-UVR-Automator helps an agent extract vocals from individual audio files or folders using UVR/audio-separator models while preserving directory structure. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[wangminrui2022](https://clawhub.ai/user/wangminrui2022) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to separate vocals from songs or audio collections for karaoke, cover-song preparation, music production, and audio cleanup workflows. It is intended for local processing of user-selected audio files or recursively selected folders. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can create a Python environment and download large ML, audio, ffmpeg, and model packages during execution. <br>
Mitigation: Run it in an isolated environment or container and review the first-run install and download behavior before using it on production machines. <br>
Risk: Recursive folder processing can read many audio files and write generated outputs, logs, and cached models under local paths. <br>
Mitigation: Review input and output paths carefully, use sample mode for trial runs, and limit folder scope to the intended audio collection. <br>
Risk: The security scan summary states that the tool automatically changes Python environments and downloads software without clear user approval. <br>
Mitigation: Require explicit operator approval before dependency installation or model downloads and prefer a disposable runtime for untrusted releases. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/wangminrui2022/skills/purevocals-uvr-automator) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/wangminrui2022) <br>
- [UVR public model releases](https://github.com/TRvlvr/model_repo/releases/tag/all_public_uvr_models) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Files, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and generated WAV audio files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Processes supported audio files from a single path or recursive folder input and writes extracted vocals to the requested output directory.] <br>

## Skill Version(s): <br>
1.0.7 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
