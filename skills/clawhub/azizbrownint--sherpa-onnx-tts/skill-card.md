## Description:

Local text-to-speech via sherpa-onnx (offline, no cloud).

This skill is ready for commercial/non-commercial use.

## Publisher:

[azizbrownint](https://clawhub.ai/user/azizbrownint)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to generate speech audio locally from text with sherpa-onnx, without sending text to a cloud TTS service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill downloads and runs a native sherpa-onnx runtime under the user's normal account.

Mitigation: Install only trusted k2-fsa/sherpa-onnx release artifacts and verify release hashes or signatures where available before use.

Risk: The wrapper launches the native runtime with the process environment, which may include sensitive credentials.

Mitigation: Run the skill from an agent process with a minimal environment and avoid exposing unrelated secrets during TTS generation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/azizbrownint/skills/sherpa-onnx-tts)
- [sherpa-onnx runtime for macOS](https://github.com/k2-fsa/sherpa-onnx/releases/download/v1.13.2/sherpa-onnx-v1.13.2-osx-universal2-shared.tar.bz2)
- [sherpa-onnx runtime for Linux x64](https://github.com/k2-fsa/sherpa-onnx/releases/download/v1.13.2/sherpa-onnx-v1.13.2-linux-x64-shared.tar.bz2)
- [sherpa-onnx runtime for Windows x64](https://github.com/k2-fsa/sherpa-onnx/releases/download/v1.13.2/sherpa-onnx-v1.13.2-win-x64-shared-MD-Release.tar.bz2)
- [Piper en_US lessac high voice model](https://github.com/k2-fsa/sherpa-onnx/releases/download/tts-models/vits-piper-en_US-lessac-high.tar.bz2)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Files, Guidance]

**Output Format:** [Markdown with inline bash and JSON5 code blocks; command execution can produce a WAV audio file.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SHERPA_ONNX_RUNTIME_DIR and SHERPA_ONNX_MODEL_DIR; optional flags select model, tokens, data directory, and output path.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
