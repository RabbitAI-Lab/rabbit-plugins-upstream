## Description:

语音克隆、文字转语音（同步/异步）、语音识别等多端点 AI 语音能力。

This skill is ready for commercial/non-commercial use.

## Publisher:

[2253128](https://clawhub.ai/user/2253128)

### License/Terms of Use:

MIT

## Use Case:

External users and developers use this skill to call a7w voice APIs for text-to-speech, asynchronous speech synthesis, speech-to-text, voice listing, and voice cloning workflows. It is intended for users who bring their own api.a7w.cn API key and accept that calls may consume account points.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API keys, voice samples, STT audio, and TTS text are sensitive and are sent to the a7w service during calls.

Mitigation: Install only if the a7w service is trusted, keep keys in local config or environment variables, and avoid overriding the host unless the endpoint is fully controlled and trusted.

Risk: Voice cloning can misuse a person's voice or source audio.

Mitigation: Clone voices only with consent and review generated audio for legal, copyright, and content-policy compliance before publishing or distributing it.

Risk: API calls can spend points from the user's account, and repeated asynchronous submissions may create avoidable costs.

Mitigation: Review parameters and account balance before submitting jobs, avoid duplicate submissions, and check task status before retrying.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/2253128/skills/sanjianke-voice-tts-studio)
- [Getting started](references/getting-started.md)
- [Text-to-speech API](references/api-tts.md)
- [Live text-to-speech API](references/api-tts_live.md)
- [Asynchronous text-to-speech API](references/api-tts_async.md)
- [Speech-to-text API](references/api-stt.md)
- [Voice cloning API](references/api-clone_voice.md)
- [List voices API](references/api-list_voices.md)
- [a7w compute marketplace](https://api.a7w.cn/)
- [AI plugin marketplace](https://aigc.a7w.cn/)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, JSON, API Calls]

**Output Format:** [Markdown guidance with inline shell commands and JSON API payloads or responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write JSON results to a user-specified output file when the client is called with an output path.]

## Skill Version(s):

1.0.5 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
