## Description: <br>
Local speech-to-text with MLX Whisper (Apple Silicon optimized, no API key). <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kevin37li](https://clawhub.ai/user/kevin37li) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent users use this skill to transcribe, translate, or generate subtitles from local audio and video files with MLX Whisper on Apple Silicon Macs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill relies on the mlx-whisper pip package and selected Hugging Face model sources. <br>
Mitigation: Install only when those package and model sources are trusted for the intended environment. <br>
Risk: Audio or video files may contain sensitive content. <br>
Mitigation: Only provide local media files that are intended for transcription or translation. <br>
Risk: Model downloads can be large and are cached on local disk. <br>
Mitigation: Choose a model size appropriate for the task and monitor the Hugging Face cache location. <br>


## Reference(s): <br>
- [MLX Whisper examples](https://github.com/ml-explore/mlx-examples/tree/main/whisper) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, text, files] <br>
**Output Format:** [Markdown with inline bash commands and generated text or subtitle files from mlx_whisper] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires the mlx_whisper CLI, Apple Silicon hardware, and downloaded model files cached locally.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
