## Description:

Local text-to-speech using Qwen3-TTS with mlx_audio (macOS Apple Silicon) or qwen-tts (Linux/Windows). Privacy-first offline TTS with natural, realistic voice cloning and voice design. Use for local, secure, high-quality multilingual speech synthesis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[irachex](https://clawhub.ai/user/irachex)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and technical users use this skill to set up and run local Qwen3-TTS on macOS Apple Silicon, Linux, or Windows for speech synthesis with preset voices, voice design, and consented voice cloning.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Python packages and model downloads introduce dependency and model supply-chain risk.

Mitigation: Install in an isolated virtual environment or container, pin dependency and model versions where possible, and verify sources before use.

Risk: Sensitive text may appear in local command output or retained console logs during synthesis.

Mitigation: Control console logging, avoid processing highly sensitive text where logs are retained, and redact or disable command echoes when needed.

Risk: Voice cloning can be misused to imitate a speaker without consent.

Mitigation: Use reference audio only with explicit permission from the speaker and review generated audio before distribution.

Risk: Privacy claims depend on correct local execution and may not cover dependency installation, model download, or operator logging practices.

Mitigation: Download and validate required models before offline use, restrict network access during sensitive runs, and treat compliance claims as requiring local policy review.

## Reference(s):

- [ClawHub Local TTS Release Page](https://clawhub.ai/irachex/skills/local-tts)
- [macOS mlx_audio Reference](references/macos_mlx_audio.md)
- [Linux/Windows qwen-tts Reference](references/linux_windows_transformers.md)
- [Privacy & Security Benefits of Local TTS](references/privacy_security.md)
- [FFmpeg Downloads](https://ffmpeg.org/download.html)

## Skill Output:

**Output Type(s):** [Markdown, Code, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown guidance with bash and Python command examples; generated runs may write local WAV audio files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance is platform-specific and depends on local Python packages, model downloads, and available Apple Silicon, CUDA, or CPU hardware.]

## Skill Version(s):

1.0.0 (source: server release metadata and package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
