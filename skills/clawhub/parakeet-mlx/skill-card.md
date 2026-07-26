## Description: <br>
Local speech-to-text with Parakeet MLX (ASR) for Apple Silicon (no API key). <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kylehowells](https://clawhub.ai/user/kylehowells) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers, researchers, and content teams use this skill to transcribe local audio on Apple Silicon with the Parakeet MLX CLI. It helps an agent install the required CLI, run transcription commands, and choose txt, srt, vtt, json, or combined outputs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill installs and runs third-party local tooling and relies on a first-run model download. <br>
Mitigation: Before installing, confirm that the parakeet-mlx package, ffmpeg installation path, and Hugging Face model source are trusted. <br>
Risk: Audio files may contain sensitive content. <br>
Mitigation: Run transcription only on files the user intends to process, and account for the local Hugging Face model cache. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/kylehowells/skills/parakeet-mlx) <br>
- [Parakeet MLX project homepage](https://github.com/senstella/parakeet-mlx) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands; transcription outputs can be txt, srt, vtt, or json.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Apple Silicon, the parakeet-mlx CLI, and ffmpeg; models download from Hugging Face on first use.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
