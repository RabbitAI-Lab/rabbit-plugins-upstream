## Description: <br>
Turn your AI into JARVIS with offline voice output, metallic audio processing, and a high-humor personality profile. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[globalcaos](https://clawhub.ai/user/globalcaos) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and OpenClaw users use this skill to make an agent speak short responses through a JARVIS-style local voice command and apply a dry-wit conversational style across sessions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Automatic background shell command execution may run more often than intended. <br>
Mitigation: Review the jarvis script before use, keep the command fixed, and enable the skill only for intended sessions. <br>
Risk: Reply text may be passed to local voice tooling or the SkillBoss TTS service. <br>
Mitigation: Avoid speaking sensitive content and use a mute or session-only control when handling private material. <br>
Risk: Persistent workspace prompt templates can change agent behavior across future sessions. <br>
Mitigation: Install templates only in workspaces where persistent JARVIS-style behavior is desired, and remove or disable them when normal agent behavior is needed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/globalcaos/skills/jarvis-voice) <br>
- [Piper en_GB Alan voice model download](https://github.com/k2-fsa/sherpa-onnx/releases/download/tts-models/vits-piper-en_GB-alan-medium.tar.bz2) <br>
- [LIMBIC humor research note](https://github.com/globalcaos/tinkerclaw/blob/main/AI_reports/humor-embeddings-paper-draft.md) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown instructions with inline shell commands and workspace prompt templates] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Linux, ffmpeg, aplay, SHERPA_ONNX_TTS_DIR, and the sherpa-onnx-tts skill; spoken text should stay within the skill's length and language limits.] <br>

## Skill Version(s): <br>
2.2.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
