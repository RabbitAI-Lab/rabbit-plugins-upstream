## Description: <br>
Generates MeloTTS metadata.list files from .wav audio and matching .txt transcripts, with optional Whisper transcription when transcript files are missing. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[wangminrui2022](https://clawhub.ai/user/wangminrui2022) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and voice model builders use this skill to prepare MeloTTS training or fine-tuning datasets by pairing audio files with transcripts, speaker labels, language codes, and optional Whisper-generated text. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can modify Python environments and install or upgrade large ML packages. <br>
Mitigation: Run it in an isolated disposable environment and review dependency changes before reuse. <br>
Risk: Whisper mode may download models and write generated transcript files in the provided text directory. <br>
Mitigation: Confirm the input, transcript, model, and output paths before execution, especially when using --use_whisper. <br>
Risk: The skill probes local GPU details and writes logs, transcripts, and metadata locally. <br>
Mitigation: Use a workspace that does not contain sensitive unrelated files and inspect generated logs and metadata before sharing. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/wangminrui2022/skills/melo-tts-metadata-creator) <br>
- [Publisher profile](https://clawhub.ai/user/wangminrui2022) <br>


## Skill Output: <br>
**Output Type(s):** [Files, Text, Shell commands, Configuration instructions] <br>
**Output Format:** [metadata.list text file with pipe-delimited rows plus Markdown command guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Rows use audio path, speaker, language, and transcript fields separated by pipe characters; optional Whisper mode may also write generated .txt transcript files.] <br>

## Skill Version(s): <br>
1.0.8 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
