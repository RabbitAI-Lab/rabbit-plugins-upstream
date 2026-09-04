## Description:

Generates speech audio from text using Alibaba Cloud DashScope Qwen TTS, with optional Feishu voice-message delivery and an Edge TTS fallback.

This skill is ready for commercial/non-commercial use.

## Publisher:

[lanlan314](https://clawhub.ai/user/lanlan314)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to turn text responses into speech files or Feishu voice messages for Chinese and English voice interactions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Text sent for speech synthesis may include private, business, or credential-like content.

Mitigation: Use only content that is acceptable to send to DashScope and Feishu, and review agent outputs before invoking the speech or send scripts.

Risk: The skill can automatically send generated audio through Feishu using local application credentials.

Mitigation: Configure a dedicated Feishu app and recipient for this workflow, restrict credential scope, and avoid reusing broad existing OpenClaw credentials.

Risk: Scripts may reuse secrets from shell profiles or local OpenClaw configuration.

Mitigation: Prefer explicit environment variables and dedicated credentials, and inspect local credential files before running the send workflow.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/lanlan314/skills/qwen-tts)
- [Qwen TTS API Reference](artifact/references/api.md)
- [Qwen TTS Voice List](artifact/references/voices.md)
- [DashScope Console](https://dashscope.console.aliyun.com)
- [DashScope Multimodal Generation API](https://dashscope.aliyuncs.com/api/v1/services/aigc/multimodal-generation/generation)
- [Feishu Tenant Token API](https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell and Python command examples; scripts produce local OGG audio files or Feishu audio messages.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires DashScope credentials for Qwen TTS; Feishu sending requires Feishu app and recipient credentials; generated DashScope audio URLs are described as expiring after 24 hours.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
