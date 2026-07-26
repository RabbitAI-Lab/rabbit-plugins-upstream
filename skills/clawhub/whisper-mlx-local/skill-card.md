## Description: <br>
Free local speech-to-text for Telegram and WhatsApp using MLX Whisper on Apple Silicon. Private, no API costs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[impkind](https://clawhub.ai/user/impkind) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and OpenClaw users use this skill to transcribe Telegram, WhatsApp, or other local voice-message audio on Apple Silicon Macs without routine paid transcription API calls. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Local and private transcription claims may be undermined if cloud transcription backends are available through environment credentials. <br>
Mitigation: Force the intended local backend and keep OPENAI_API_KEY and GROQ_API_KEY out of the skill environment unless cloud transcription is intentional. <br>
Risk: The local daemon exposes file-path based transcription on localhost and can read paths provided to its endpoint. <br>
Mitigation: Keep CLAWD_WHISPER_URL pointed at localhost, restrict access to the daemon, and stop it when it is not needed. <br>
Risk: The large-file helper has unsafe handling for untrusted filenames according to the security guidance. <br>
Mitigation: Avoid using the large-file helper with untrusted filenames until its path handling is fixed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/impkind/skills/whisper-mlx-local) <br>
- [Publisher profile](https://clawhub.ai/user/impkind) <br>
- [Project repository](https://github.com/ImpKind/local-whisper) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, shell commands, configuration] <br>
**Output Format:** [Plain text transcription, optional JSON responses, and Markdown usage guidance with shell and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Transcription output may include backend and model metadata when JSON mode or the local daemon is used.] <br>

## Skill Version(s): <br>
1.5.0 (source: server release metadata and OpenClaw metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
