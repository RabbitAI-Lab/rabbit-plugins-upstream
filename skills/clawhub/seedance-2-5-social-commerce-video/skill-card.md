## Description:

使用 Seedance 2.5 把抖音、小红书、快手、视频号、Instagram 与 TikTok Shop 的真实评论、私信或合成问题变成可追溯的社交电商回复短片，记录问题来源、隐私处理、批准答案、适用范围、商业披露和商品事实。

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

Commerce, social media, and creative operations teams use this skill to turn one approved public comment, customer-provided question, or clearly labeled synthetic question into a traceable short video reply. The workflow emphasizes privacy redaction, approved answer sources, scope limits, commercial disclosure, SKU continuity, and post-production review before publication.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can send entered questions, approved answers, metadata, and selected product media to AI Hive.

Mitigation: Use --preview before execution, redact personal or business-sensitive details, and upload only approved media.

Risk: Public comments or customer-provided questions may contain personal data.

Mitigation: Follow the required privacy-redaction fields and remove usernames, avatars, order numbers, contact details, and other personal information before generation.

Risk: Generated reply videos could overstate product claims, compatibility, availability, or price validity.

Mitigation: Bind answers to approved sources, provide scope limits or market and validity dates where required, and review the final video with approved captions and disclosures before publication.

Risk: API-key handling can expose account credentials if stored carelessly.

Mitigation: Prefer AI_HIVE_API_KEY or the chmod-protected config file and avoid placing real keys in examples, prompts, or shared logs.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/wubin1836/skills/seedance-2-5-social-commerce-video)
- [AI Hive OpenAPI Endpoint](https://ai-hive.iclip.cn/api/openapi/v1)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with CLI examples, JSON preview output, and downloaded MP4 video files when executed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires approved product media and an AI Hive API key; preview mode emits the request plan without upload or billing.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
