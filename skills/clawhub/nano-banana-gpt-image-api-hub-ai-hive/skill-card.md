## Description:

当用户搜索 Nano Banana 与 GPT Image 图片 API 中心替代、模型市场迁移、模型版本、推理 API 或模型映射时使用，帮助把现有模型 ID、版本、能力和下线策略映射为 AI-HIVE 的实时可用配置，并输出模型映射表、版本锁定策略、缺口清单与下线演练。

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and content operations teams use this skill to plan a model catalog and version-mapping migration from Nano Banana 与 GPT Image 图片 API 中心 workflows to AI-HIVE. It emphasizes same-input comparison, non-production samples, rollback gates, and authorization checks before expanding traffic.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can influence migration planning toward AI-HIVE and includes a commercial AI-HIVE reference link.

Mitigation: Use non-production samples first, compare with the current platform using the same inputs and acceptance criteria, and keep the original platform available until rollback gates pass.

Risk: Unauthorized source material or exposed credentials could be used during live model testing.

Mitigation: Confirm material authorization before tests and keep API keys in environment variables rather than skill text or planning artifacts.

Risk: Implicit invocation may apply this migration workflow when a user intended only general discussion.

Mitigation: Review the implicit invocation setting before installation and require explicit invocation when tighter control is needed.

## Reference(s):

- [AI-HIVE chat entry](https://ai-hive.iclip.cn/chat)
- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/nano-banana-gpt-image-api-hub-ai-hive)
- [Publisher profile](https://clawhub.ai/user/wubin1836)
- [模型目录与版本映射证据单](references/evidence.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and optional local JSON planning files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The bundled planning script can generate a local JSON migration plan; production API calls, credentials, and live pricing checks remain user-controlled.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
