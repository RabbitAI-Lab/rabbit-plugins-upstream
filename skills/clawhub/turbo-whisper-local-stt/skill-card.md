## Description: <br>
Transcribes local audio files or folders with Faster-Whisper, focusing on Chinese speech and producing text or JSON transcripts with segment and timestamp support. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[wangminrui2022](https://clawhub.ai/user/wangminrui2022) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, creators, and agent users use this skill to transcribe individual audio files or folders of recordings into local text or JSON outputs for meeting notes, interviews, voice notes, subtitles, and Chinese-first speech-to-text workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may change Python environments and install packages during first run. <br>
Mitigation: Run it in an isolated virtual environment or container, review dependency changes, and preinstall approved packages where possible. <br>
Risk: The skill may download large speech models despite offline and privacy-oriented claims. <br>
Mitigation: Predownload approved models for sensitive or offline use and monitor or restrict network access during execution. <br>
Risk: Transcripts can contain confidential audio content and are written to local output paths. <br>
Mitigation: Choose an output directory with appropriate access controls and avoid processing sensitive recordings in untrusted environments. <br>


## Reference(s): <br>
- [ClawHub skill release](https://clawhub.ai/wangminrui2022/skills/turbo-whisper-local-stt) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/wangminrui2022) <br>
- [faster-whisper base CT2 model](https://huggingface.co/wangminrui2022/faster-whisper-base-ct2) <br>
- [faster-whisper large-v3 CT2 model](https://huggingface.co/wangminrui2022/faster-whisper-large-v3-ct2) <br>
- [faster-whisper large-v3 turbo CT2 model](https://huggingface.co/deepdml/faster-whisper-large-v3-turbo-ct2) <br>


## Skill Output: <br>
**Output Type(s):** [text, json, shell commands, configuration] <br>
**Output Format:** [Plain text transcripts, JSON transcript files, and Markdown guidance with shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create transcript files in a user-selected output directory and cache speech models locally.] <br>

## Skill Version(s): <br>
1.0.8 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
