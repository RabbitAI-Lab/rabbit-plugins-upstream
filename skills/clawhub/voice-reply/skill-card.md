## Description: <br>
Local text-to-speech using Piper voices via sherpa-onnx, running fully offline with no API keys and producing Telegram-compatible voice note output. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[stolot0mt0m](https://clawhub.ai/user/stolot0mt0m) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and OpenClaw users use this skill to turn text responses into local spoken audio replies, including German and English voice notes for Telegram-style delivery. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The installer performs privileged system installation and downloads upstream binaries and voice models. <br>
Mitigation: Review scripts/install.sh before use, install only when the publisher and upstream sherpa-onnx release source are trusted, and verify release checksums where possible. <br>
Risk: Unsigned downloaded binaries under /opt may be unacceptable on managed or high-assurance systems. <br>
Mitigation: Use an isolated environment or an approved internal packaging workflow before deploying the skill on sensitive systems. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/stolot0mt0m/skills/voice-reply) <br>
- [sherpa-onnx](https://github.com/k2-fsa/sherpa-onnx) <br>
- [Piper](https://github.com/rhasspy/piper) <br>
- [Piper Voice Samples](https://rhasspy.github.io/piper-samples/) <br>
- [Thorsten Voice](https://github.com/thorstenMueller/Thorsten-Voice) <br>


## Skill Output: <br>
**Output Type(s):** [text, audio, shell commands, configuration] <br>
**Output Format:** [Plain text media marker plus an OGG Opus audio file path.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires local sherpa-onnx, Piper voice models, ffmpeg, and SHERPA_ONNX_DIR/PIPER_VOICES_DIR.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
