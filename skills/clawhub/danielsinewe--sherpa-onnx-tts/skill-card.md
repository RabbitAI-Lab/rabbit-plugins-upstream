## Description:

Local text-to-speech via sherpa-onnx (offline, no cloud).

This skill is ready for commercial/non-commercial use.

## Publisher:

[danielsinewe](https://clawhub.ai/user/danielsinewe)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to run offline text-to-speech locally through the sherpa-onnx CLI, including configuring runtime and model paths and producing WAV audio from text.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill downloads and extracts third-party native runtime archives without pinned checksums.

Mitigation: Use only trusted sherpa-onnx release assets and verify hashes or signatures independently before installation when stronger supply-chain assurance is required.

Risk: The skill depends on local runtime and model directory environment variables.

Mitigation: Set SHERPA_ONNX_RUNTIME_DIR and SHERPA_ONNX_MODEL_DIR to trusted local paths before running the wrapper.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/danielsinewe/skills/sherpa-onnx-tts)
- [sherpa-onnx runtime release v1.12.23 for macOS](https://github.com/k2-fsa/sherpa-onnx/releases/download/v1.12.23/sherpa-onnx-v1.12.23-osx-universal2-shared.tar.bz2)
- [sherpa-onnx runtime release v1.12.23 for Linux x64](https://github.com/k2-fsa/sherpa-onnx/releases/download/v1.12.23/sherpa-onnx-v1.12.23-linux-x64-shared.tar.bz2)
- [sherpa-onnx runtime release v1.12.23 for Windows x64](https://github.com/k2-fsa/sherpa-onnx/releases/download/v1.12.23/sherpa-onnx-v1.12.23-win-x64-shared.tar.bz2)
- [Piper en_US lessac high TTS model archive](https://github.com/k2-fsa/sherpa-onnx/releases/download/tts-models/vits-piper-en_US-lessac-high.tar.bz2)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON5 configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can guide local generation of WAV audio through the sherpa-onnx CLI.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
