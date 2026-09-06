## Description:

小米MiMo语音 is a text-to-speech skill that helps agents convert Chinese or English text into MiMo-generated speech.

This skill is ready for commercial/non-commercial use.

## Publisher:

[lanlan314](https://clawhub.ai/user/lanlan314)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to synthesize natural speech from provided text through Xiaomi MiMo TTS APIs, including local audio generation and optional delivery through Feishu/Lark helper scripts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Text submitted for synthesis is sent to Xiaomi MiMo.

Mitigation: Avoid using the skill with secrets or sensitive text unless that data sharing is acceptable.

Risk: Bundled helper scripts can upload and send generated audio through Feishu/Lark without clear user-facing scope or confirmation.

Mitigation: Review or remove Feishu/Lark helper scripts before use, and require explicit confirmation before sending generated audio to any recipient.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/lanlan314/skills/mimo-tts)
- [MiMo API key console](https://platform.xiaomimimo.com/#/console/api-keys)
- [MiMo API base URL](https://api.xiaomimimo.com/v1)
- [MiMo audio speech endpoint](https://api.xiaomimimo.com/v1/audio/speech)
- [MiMo chat completions endpoint](https://api.xiaomimimo.com/v1/chat/completions)

## Skill Output:

**Output Type(s):** [text, shell commands, code, configuration, files]

**Output Format:** [Markdown guidance with bash and Python commands; scripts produce local WAV or OGG audio files and JSON or plain-text status output.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires MIMO_API_KEY. Some helper scripts also rely on ffmpeg, lark-cli, and FEISHU_USER_OPEN_ID for audio conversion and Feishu/Lark delivery.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
