## Description:

语音克隆、文字转语音（同步/异步）、语音识别等多端点 AI 语音能力，支持 Live 异步 TTS、克隆音色、同步/异步文字转语音、语音转文字和音色列表，需要使用者自己的 api.a7w.cn API Key。

This skill is ready for commercial/non-commercial use.

## Publisher:

[2253128](https://clawhub.ai/user/2253128)

### License/Terms of Use:

MIT

## Use Case:

Developers, creators, and agents use this skill to call a7w voice APIs for text-to-speech, asynchronous long-form speech generation, voice cloning, speech transcription, and voice model lookup from command-line or agent workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles API keys and paid API usage for a third-party voice service.

Mitigation: Use a dedicated low-balance API key, keep it in the local config or A7W_API_KEY environment variable, and do not commit credentials.

Risk: The bundled client can be pointed at a custom host through A7W_HOST or --host.

Mitigation: Only configure hosts you trust, and prefer the documented api.a7w.cn service unless there is a reviewed operational reason to change it.

Risk: Voice cloning and speech recognition may involve sensitive or unauthorized voice samples.

Mitigation: Upload only authorized material, avoid private voice samples unless required and approved, and review generated audio for content and consent risks.

Risk: Generated audio URLs and callback destinations may expose sensitive output or workflow metadata.

Mitigation: Treat returned audio URLs, task IDs, and callback URLs as sensitive and restrict sharing to intended recipients.

## Reference(s):

- [Getting Started](references/getting-started.md)
- [General Notes](references/通用说明.md)
- [TTS Live API](references/api-tts_live.md)
- [Voice Clone API](references/api-clone_voice.md)
- [TTS API](references/api-tts.md)
- [TTS Async API](references/api-tts_async.md)
- [STT API](references/api-stt.md)
- [List Voices API](references/api-list_voices.md)
- [a7w Compute Market](https://api.a7w.cn/)
- [ClawHub Skill Page](https://clawhub.ai/2253128/skills/sanjianke-voice-tts-studio)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return task IDs, generated audio URLs, transcription text, voice model IDs, and saved JSON output when the client is run with an output path.]

## Skill Version(s):

1.0.6 (source: server release metadata; artifact frontmatter says 1.0.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
